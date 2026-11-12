"""
Pure classification helpers: tags, categories and "is this a dev job?".

Everything in this module is a pure function (no network, no I/O) so the rules
that decide whether the public API is useful can be unit tested with frozen
fixtures. See tests/test_classify.py.
"""

from __future__ import annotations

import html
import re
from collections.abc import Iterable, Sequence

# --------------------------------------------------------------------------- #
# Tech tag vocabulary (canonical term -> how it is displayed)
# --------------------------------------------------------------------------- #
# Only terms listed here survive as tags. Anything else coming from a source's
# raw tags ("Medical", "Travel", "Exec", ...) is dropped, which is what kept
# listings like "Registered Nurse" tagged as Education/Marketing.
TECH_TAGS: dict[str, str] = {
    "ai": "AI",
    "ml": "ML",
    "llm": "LLM",
    "nlp": "NLP",
    "rag": "RAG",
    "machine learning": "Machine Learning",
    "deep learning": "Deep Learning",
    "computer vision": "Computer Vision",
    "mlops": "MLOps",
    "python": "Python",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "react": "React",
    "react native": "React Native",
    "next.js": "Next.js",
    "vue": "Vue",
    "angular": "Angular",
    "svelte": "Svelte",
    "node": "Node",
    "node.js": "Node",
    "django": "Django",
    "fastapi": "FastAPI",
    "flask": "Flask",
    "golang": "Go",
    "go": "Go",
    "rust": "Rust",
    "java": "Java",
    "spring": "Spring",
    "c#": "C#",
    ".net": ".NET",
    "php": "PHP",
    "laravel": "Laravel",
    "ruby": "Ruby",
    "rails": "Rails",
    "elixir": "Elixir",
    "scala": "Scala",
    "sql": "SQL",
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "mysql": "MySQL",
    "mongodb": "MongoDB",
    "redis": "Redis",
    "kafka": "Kafka",
    "aws": "AWS",
    "gcp": "GCP",
    "azure": "Azure",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "terraform": "Terraform",
    "graphql": "GraphQL",
    "grpc": "gRPC",
    "tailwind": "Tailwind",
    "css": "CSS",
    "html": "HTML",
    "flutter": "Flutter",
    "swift": "Swift",
    "kotlin": "Kotlin",
    "android": "Android",
    "ios": "iOS",
    "devops": "DevOps",
    "sre": "SRE",
    "security": "Security",
    "blockchain": "Blockchain",
    "web3": "Web3",
    "unity": "Unity",
    "unreal": "Unreal",
    "salesforce": "Salesforce",
    "wordpress": "WordPress",
    "shopify": "Shopify",
    "supabase": "Supabase",
    "firebase": "Firebase",
    "figma": "Figma",
}


def _tag_pattern(term: str) -> re.Pattern[str]:
    """Whole-term match that also works for terms with dots hashes and pluses."""
    return re.compile(
        r"(?<![A-Za-z0-9])" + re.escape(term) + r"(?![A-Za-z0-9+#])",
        re.IGNORECASE,
    )


_TAG_PATTERNS: dict[str, re.Pattern[str]] = {
    term: _tag_pattern(term) for term in TECH_TAGS
}
# "go" is the language, not the English verb: only accept it capitalised.
_TAG_PATTERNS["go"] = re.compile(r"(?<![A-Za-z0-9])Go(?![A-Za-z0-9+#])")

# --------------------------------------------------------------------------- #
# Category rules (first match wins, so order matters)
# --------------------------------------------------------------------------- #
_CATEGORY_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("Fullstack", (r"\bfull[\s\-]?stack\b",)),
    (
        "AI / Data",
        (
            r"\bai\b",
            r"\bml\b",
            r"\bllm\b",
            r"\bnlp\b",
            r"\brag\b",
            r"\bgenai\b",
            r"\bmachine learning\b",
            r"\bdeep learning\b",
            r"\bcomputer vision\b",
            r"\bdata scien",
            r"\bdata engineer",
            r"\bdata analyst",
            r"\bdata platform\b",
            r"\bmlops\b",
            r"\bprompt engineer",
        ),
    ),
    (
        "DevOps / Cloud",
        (
            r"\bdevops\b",
            r"\bsre\b",
            r"\bsite reliability\b",
            r"\bcloud\b",
            r"\binfrastructure\b",
            r"\bkubernetes\b",
            r"\bterraform\b",
            r"\bplatform engineer",
            r"\baws\b",
            r"\bazure\b",
            r"\bgcp\b",
            r"\bsecurity engineer",
            r"\bsecurity\b",
            r"\bcybersecurity\b",
            r"\bcloudops\b",
            r"\bsystems? (engineer|administrator|admin)\b",
            r"\bnetwork engineer\b",
            r"\bit (systems|infrastructure|operations)\b",
        ),
    ),
    (
        "Mobile",
        (
            r"\bios\b",
            r"\bandroid\b",
            r"\bflutter\b",
            r"\breact native\b",
            r"\bmobile\b",
            r"\bswift\b",
            r"\bkotlin\b",
        ),
    ),
    (
        "Frontend",
        (
            r"\bfront[\s\-]?end\b",
            r"\breact\b",
            r"\bvue\b",
            r"\bangular\b",
            r"\bsvelte\b",
            r"\bui\/ux\b",
            r"\bui\b",
            r"\bux\b",
            r"\btailwind\b",
            r"\bcss\b",
            r"\bhtml\b",
            r"\bweb designer\b",
            r"\baccessibility\b",
        ),
    ),
    (
        "Backend",
        (
            r"\bback[\s\-]?end\b",
            r"\bdjango\b",
            r"\bfastapi\b",
            r"\bflask\b",
            r"\bgolang\b",
            r"\brust\b",
            r"\bjava\b",
            r"\bspring\b",
            r"\brails\b",
            r"\bnode\b",
            r"\bphp\b",
            r"\blaravel\b",
            r"\bsql\b",
            r"\bpostgres",
            r"\bmicroservices\b",
            r"\bapi\b",
            r"\bgo\b",
            r"\barchitect\b",
        ),
    ),
)
_CATEGORY_PATTERNS = tuple(
    (category, tuple(re.compile(p) for p in patterns))
    for category, patterns in _CATEGORY_RULES
)
DEFAULT_CATEGORY = "General"

# --------------------------------------------------------------------------- #
# Dev job detection
# --------------------------------------------------------------------------- #
_NON_DEV_PATTERNS = tuple(
    re.compile(p)
    for p in (
        # health / care
        r"\bnurse",
        r"\bphysician",
        r"\btherapist\b",
        r"\bclinician\b",
        r"\bmedical\b",
        r"\bpatient",
        r"\bendocrinolog",
        r"\btelehealth\b",
        r"\bpharmac",
        r"\bdentist\b",
        # finance / admin
        r"\baccountant\b",
        r"\bbookkeep",
        r"\bpayroll\b",
        r"\bauditor\b",
        # sales / growth
        r"\brecruit",
        r"\bsourcer\b",
        r"\bsales\b",
        r"\baccount executive\b",
        r"\bbusiness development\b",
        r"\bmedia buyer\b",
        r"\bpaid media\b",
        r"\bmarketing\b",
        r"\bsocial media\b",
        r"\bcommunity manager\b",
        # support / ops that is not engineering
        r"\bcustomer (service|support) (rep|agent|associate|specialist|advocate)\b",
        r"\bsupport (specialist|agent|associate|representative)\b",
        r"\bhelp desk\b",
        r"\bdata entry\b",
        r"\bvirtual assistant\b",
        # product / management
        r"\bproduct (manager|management|owner)\b",
        r"\bdirector of product\b",
        r"\bproject manager\b",
        r"\bprogram manager\b",
        # content / design
        r"\bcopywriter\b",
        r"\bcontent (writer|reviewer|moderator)\b",
        r"\bgraphic designer\b",
        r"\bproduct designer\b",
        # misc
        r"\bcoordinator\b",
        r"\bexecutive assistant\b",
        r"\bcoach\b",
        r"\bparalegal\b",
        r"\blawyer\b",
        r"\battorney\b",
    )
)

_DEV_TITLE_PATTERNS = tuple(
    re.compile(p)
    for p in (
        r"\bengineer",
        r"\bdeveloper\b",
        r"\bprogrammer\b",
        r"\bdevops\b",
        r"\bsre\b",
        r"\barchitect\b",
        r"\bsoftware\b",
        r"\bfront[\s\-]?end\b",
        r"\bback[\s\-]?end\b",
        r"\bfull[\s\-]?stack\b",
        r"\bdata (engineer|scientist|analyst)\b",
        r"\bmachine learning\b",
        r"\bml engineer\b",
        r"\bai (engineer|developer)\b",
        r"\bqa\b",
        r"\bquality assurance\b",
        r"\btest (engineer|automation)\b",
        r"\bsys(tem)?s? ?admin",
        r"\bsecurity (engineer|analyst)\b",
        r"\bmobile\b",
        r"\bios\b",
        r"\bandroid\b",
        r"\btech(nical)? lead\b",
        r"\bhead of (engineering|technology)\b",
        r"\bengineering manager\b",
        r"\bcto\b",
        r"\bunity\b",
        r"\bgame developer\b",
        r"\bblockchain\b",
        r"\bkubernetes\b",
        r"\bplatform (engineer|team)\b",
        r"\bsolutions engineer\b",
        r"\bwordpress\b",
        r"\bweb developer\b",
    )
)

# Tags that mean "this is a software role", as opposed to a technology tag.
_ROLE_TAGS = frozenset(
    {
        "dev",
        "developer",
        "engineer",
        "engineering",
        "software",
        "programming",
        "backend",
        "frontend",
        "fullstack",
        "full stack",
        "devops",
        "sre",
        "data",
        "ml",
        "ai",
        "mobile",
        "ios",
        "android",
        "qa",
        "security",
    }
)


# --------------------------------------------------------------------------- #
# Text helpers
# --------------------------------------------------------------------------- #
def normalize(text: str | None) -> str:
    """Lowercase, collapse whitespace, strip."""
    return re.sub(r"\s+", " ", text or "").strip().lower()


def clean_html(text: str | None) -> str:
    """Strip tags, decode entities, repair mojibake, collapse whitespace."""
    no_tags = re.sub(r"<[^>]+>", " ", text or "")
    cleaned = re.sub(r"\s+", " ", html.unescape(no_tags)).strip()
    return repair_mojibake(cleaned)


# ``â€”`` / ``Ãº`` style corruption: UTF-8 bytes that an upstream decoded as
# latin-1 and then re-encoded. RemoteOK does this to some titles.
_MOJIBAKE = re.compile(r"[\u00c2\u00c3\u00e2][\u0080-\u00bf]")


def repair_mojibake(text: str) -> str:
    """Undo a double encoding when the input clearly looks corrupted."""
    if not text or not _MOJIBAKE.search(text):
        return text
    try:
        fixed = text.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text
    return (
        fixed if len(_MOJIBAKE.findall(fixed)) < len(_MOJIBAKE.findall(text)) else text
    )


def shorten(text: str, limit: int) -> str:
    """Truncate on a word boundary with an ellipsis."""
    text = (text or "").strip()
    if len(text) <= limit:
        return text
    cut = text[: limit - 1].rsplit(" ", 1)[0] or text[: limit - 1]
    return cut.rstrip(" ,.;:-") + "\u2026"


def _matches(patterns: Iterable[re.Pattern[str]], text: str) -> bool:
    return any(p.search(text) for p in patterns)


def _dedupe(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            out.append(value)
    return out


# --------------------------------------------------------------------------- #
# Public API
# --------------------------------------------------------------------------- #
def extract_tags(
    text: str,
    seed_tags: Sequence[str] | None = None,
    limit: int = 5,
) -> list[str]:
    """Pick up to ``limit`` canonical tech tags for a listing.

    ``text`` is the title (the strongest signal) and ``seed_tags`` are the tags
    the source already assigned (e.g. RemoteOK), trusted but restricted to the
    vocabulary. Job descriptions are deliberately ignored: every description
    these days mentions "AI", and mining them labelled plain React roles as
    AI/ML jobs.
    """
    seeds = {normalize(t) for t in (seed_tags or [])}
    primary = text or ""

    picked = _dedupe(
        display
        for term, display in TECH_TAGS.items()
        if term in seeds or _TAG_PATTERNS[term].search(primary)
    )

    return picked[:limit]


def detect_category(
    title: str,
    tags: Sequence[str] | None = None,
    hints: Sequence[str] | None = None,
) -> str:
    """Bucket a listing into one of the dashboard categories.

    ``hints`` are the source's own tags (RemoteOK exposes role words such as
    ``backend`` or ``devops``). They are only used to disambiguate generic
    titles like "Staff Software Engineer", never to override the title.
    """
    haystack = normalize(f"{title} {' '.join(tags or [])}")
    for category, patterns in _CATEGORY_PATTERNS:
        if _matches(patterns, haystack):
            return category

    hinted = normalize(" ".join(hints or []))
    for category, patterns in _CATEGORY_PATTERNS:
        if _matches(patterns, hinted):
            return category
    return DEFAULT_CATEGORY


def is_dev_job(title: str, source_tags: Sequence[str] | None = None) -> bool:
    """True when the listing is a software/IT role.

    RemoteOK returns every remote job on the planet, so this filter is what
    keeps nurses, accountants and sales reps out of a "dev jobs" API.

    Only the title and the tags assigned by the source are considered: mined
    description keywords must never be able to promote a non-dev listing.
    """
    normalized_title = normalize(title)
    if not normalized_title:
        return False
    if _matches(_NON_DEV_PATTERNS, normalized_title):
        return False
    if _matches(_DEV_TITLE_PATTERNS, normalized_title):
        return True

    signal = {normalize(t) for t in (source_tags or [])}
    return len(signal & _ROLE_TAGS) >= 2

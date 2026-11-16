<p align="center">
  <img src="docs/banner.svg" alt="DevJobs Remote — vacantes remotas para developers, foco Latam y Argentina" width="100%">
</p>

<h1 align="center">DevJobs Remote</h1>

<p align="center">
  Monitor de vacantes remotas para developers, con foco en <strong>Latam y Argentina</strong>.<br>
  Pipeline completo en GitHub Actions: sin servidores, sin base de datos y sin claves de API.
</p>

<p align="center">
  <a href="https://leandrocarlino.github.io/dev-remote-jobs-monitor/"><b>Dashboard</b></a> ·
  <a href="https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/jobs.json"><b>API JSON</b></a> ·
  <a href="https://leandrocarlino.github.io/dev-remote-jobs-monitor/feed.xml"><b>RSS</b></a> ·
  <a href="https://github.com/LeandroCarlino/dev-remote-jobs-monitor/issues"><b>Issues</b></a>
</p>

<p align="center">
  <a href="https://github.com/LeandroCarlino/dev-remote-jobs-monitor/actions/workflows/update-jobs.yml"><img alt="Update" src="https://github.com/LeandroCarlino/dev-remote-jobs-monitor/actions/workflows/update-jobs.yml/badge.svg"></a>
  <a href="https://github.com/LeandroCarlino/dev-remote-jobs-monitor/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/LeandroCarlino/dev-remote-jobs-monitor/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://github.com/LeandroCarlino/dev-remote-jobs-monitor/actions/workflows/deploy-pages.yml"><img alt="Deploy" src="https://github.com/LeandroCarlino/dev-remote-jobs-monitor/actions/workflows/deploy-pages.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <img alt="Sin dependencias" src="https://img.shields.io/badge/dependencias-0-emerald.svg">
  <img alt="Python 3.12+" src="https://img.shields.io/badge/python-3.12%2B-3776ab.svg">
</p>

---

## El problema

Las búsquedas remotas globales están llenas de ofertas que no son de desarrollo y de puestos que no admiten Latam. Los tableros locales, en cambio, casi nunca tienen API. Este repo junta **siete fuentes abiertas**, filtra lo que no es un rol técnico, deduce la región y el seniority, y publica todo como **JSON y RSS** que cualquiera puede consumir sin registrarse.

## Qué incluye

| Producto | Datos | Ingeniería |
|:--|:--|:--|
| Dashboard con búsqueda, filtros combinables, orden, favoritos y carga por demanda | 7 fuentes abiertas, deduplicadas y normalizadas | 81 tests offline, cero dependencias |
| Fechas en formato argentino y badge `Nuevo` | API JSON + feed RSS públicos | CI en Python 3.12 y 3.13 |
| Filtro **Latam/AR**, nivel de seniority y badges | Vocabulario controlado de ~75 tecnologías | Guard que impide publicar datos rotos |

## Fuentes

| Fuente | Cobertura | Acceso | Qué aporta |
|:--|:--|:--|:--|
| [RemoteOK](https://remoteok.com) | Global | API JSON | Volumen y salarios en USD |
| [WeWorkRemotely](https://weworkremotely.com) | Global | RSS (Programming / DevOps) | Ofertas de empresas grandes |
| [Remotive](https://remotive.com) | Global | API JSON | Categoría software-dev |
| [Get on Board](https://www.getonbrd.com) | **Latam** | API v0 pública | Chile, Argentina, Colombia, Perú, México y remoto regional |
| [Jobicy](https://jobicy.com) | Global con `geo=latam` | API JSON | Empresas que contratan en Argentina y Latam |
| [Himalayas](https://himalayas.app) | Global | API JSON (cursor) | Sueldos anuales y seniority declarado por el aviso |
| [Working Nomads](https://www.workingnomads.com) | Global | API JSON | Categoría Development, útil para Europa/Latam |

> [!NOTE]
> Todas las vacantes enlazan a la publicación original y cada fuente se acredita acá y en el sitio, como piden sus términos de API. No se scrapea ningún portal que bloquee el acceso automatizado.

<!-- STATS_START -->
### Tecnologías con más demanda hoy

![React](https://img.shields.io/badge/React-37%20vacantes-indigo) ![Python](https://img.shields.io/badge/Python-34%20vacantes-indigo) ![AI](https://img.shields.io/badge/AI-25%20vacantes-indigo) ![Node](https://img.shields.io/badge/Node-25%20vacantes-indigo) ![Java](https://img.shields.io/badge/Java-22%20vacantes-indigo) ![TypeScript](https://img.shields.io/badge/TypeScript-22%20vacantes-indigo) ![Go](https://img.shields.io/badge/Go-22%20vacantes-indigo) ![JavaScript](https://img.shields.io/badge/JavaScript-19%20vacantes-indigo)

<sub>373 ofertas activas · 7 fuentes · 30% con salario publicado · actualizado cada 6 h</sub>
<!-- STATS_END -->

## Últimas vacantes

<!-- JOBS_START -->
*Última actualización automática: **2026-11-16 05:56 UTC** · Ofertas activas: **373***

| Puesto | Empresa | Categoría | Tags | Ubicación | Fecha |
|:-------|:--------|:----------|:-----|:----------|:------|
| **[[Job-32675] Dynamics 365 CRM Senior Software Developer, Brazil](https://himalayas.app/companies/ci-t/jobs/job-32675-dynamics-365-crm-senior-software-developer-brazil?utm_source=api)** | CI&T | `General` | - | Brazil | 16/11/2026 |
| **[[Job-32674] Senior Software Developer (.NET / Azure), Brazil](https://himalayas.app/companies/ci-t/jobs/job-32674-senior-software-developer-net-azure-brazil?utm_source=api)** | CI&T | `DevOps / Cloud` | `.NET` `Azure` | Brazil | 16/11/2026 |
| **[Technical Architect](https://himalayas.app/companies/talan/jobs/technical-architect-3345315981?utm_source=api)** | Talan | `Backend` | - | Albania, Andorra, Austria, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria… | 16/11/2026 |
| **[Sr. Software Engineer, Kotlin Mobile Applications](https://himalayas.app/companies/home-depot-u-s-a-inc/jobs/sr-software-engineer-kotlin-mobile-applications?utm_source=api)** | HOME DEPOT U.S.A., INC. | `Mobile` | `Kotlin` | United States | 16/11/2026 |
| **[Sr. Data Infrastructure Engineer](https://himalayas.app/companies/lyric-inc/jobs/sr-data-infrastructure-engineer?utm_source=api)** | Lyric, Inc. | `DevOps / Cloud` | - | United States | 16/11/2026 |
| **[Sr. BI & Data Analyst - Remote - Canada](https://himalayas.app/companies/sutherland/jobs/sr-bi-data-analyst-remote-canada-8452107661?utm_source=api)** | Sutherland | `AI / Data` | - | Canada | 16/11/2026 |
| **[Sr. Avionics/ Command and Data Handling Engineer](https://himalayas.app/companies/lanteris-space-llc/jobs/sr-avionics-command-and-data-handling-engineer?utm_source=api)** | Lanteris Space LLC | `General` | - | United States | 16/11/2026 |
| **[Software Engineering Intern](https://himalayas.app/companies/bask-health/jobs/software-engineering-intern?utm_source=api)** | Bask Health | `General` | - | United States | 16/11/2026 |
| **[Senior Manager, Software Engineering - AI Developer Productivity (Dev Agents and](https://himalayas.app/companies/samsara/jobs/senior-manager-software-engineering-ai-developer-productivity-dev-agents-and?utm_source=api)** | Samsara | `AI / Data` | `AI` | United States | 16/11/2026 |
| **[Senior Engineer - ESD](https://himalayas.app/companies/megaport/jobs/senior-engineer-esd?utm_source=api)** | Megaport | `General` | - | Canada | 16/11/2026 |
| **[Senior Design Engineer, WebGL & Three.js](https://himalayas.app/companies/bask-health/jobs/senior-design-engineer-webgl-three-js?utm_source=api)** | Bask Health | `General` | - | United States | 16/11/2026 |
| **[Senior Database Engineer — Oracle & Distributed Data Systems (Cleared)](https://himalayas.app/companies/fruition-executive-search/jobs/senior-database-engineer-oracle-distributed-data-systems-cleared?utm_source=api)** | Fruition Executive Search | `General` | - | United States | 16/11/2026 |
| **[Senior Cloud Engineer (Java & AWS) (Remote, Full-Time) [AS314]](https://himalayas.app/companies/smart-working/jobs/senior-cloud-engineer-java-aws-remote-full-time-as314?utm_source=api)** | Smart Working | `DevOps / Cloud` | `Java` `AWS` | India | 16/11/2026 |
| **[Senior Analytics Engineer](https://himalayas.app/companies/booknook-com/jobs/senior-analytics-engineer?utm_source=api)** | BookNook | `General` | - | United States | 16/11/2026 |
| **[Production Support Engineer](https://himalayas.app/companies/bright-vision-technologies/jobs/production-support-engineer-3296959172?utm_source=api)** | Bright Vision Technologies | `General` | - | United States | 16/11/2026 |
| **[Product Engineering Intern](https://himalayas.app/companies/bask-health/jobs/product-engineering-intern?utm_source=api)** | Bask Health | `General` | - | United States | 16/11/2026 |
| **[Power BI Developer / Data Visualization Analyst](https://himalayas.app/companies/osc-global-com/jobs/power-bi-developer-data-visualization-analyst?utm_source=api)** | OSC Global | `General` | - | United States | 16/11/2026 |
| **[Network Vulnerability Remediation Engineer - Mid](https://himalayas.app/companies/leidos/jobs/network-vulnerability-remediation-engineer-mid?utm_source=api)** | Leidos | `General` | - | United States | 16/11/2026 |
| **[Mid-Level Software Engineer - US](https://himalayas.app/companies/lemonedge/jobs/mid-level-software-engineer-us?utm_source=api)** | LemonEdge | `General` | - | United States | 16/11/2026 |
| **[Machine Learning Engineer, Personalization](https://himalayas.app/companies/bask-health/jobs/machine-learning-engineer-personalization?utm_source=api)** | Bask Health | `AI / Data` | `Machine Learning` | United States | 16/11/2026 |
| **[Identity and Access Management (IAM) Systems Engineer II](https://himalayas.app/companies/general-dynamics-information-technology/jobs/identity-and-access-management-iam-systems-engineer-ii?utm_source=api)** | General Dynamics Information Technology | `DevOps / Cloud` | - | United States | 16/11/2026 |
| **[Fullstack .Net Cloud AWS](https://himalayas.app/companies/tecdata-engineering/jobs/fullstack-net-cloud-aws?utm_source=api)** | TECDATA ENGINEERING | `Fullstack` | `.NET` `AWS` | Spain | 16/11/2026 |
| **[Full-Stack Developer - Next.js & Python](https://himalayas.app/companies/pavago/jobs/full-stack-developer-next-js-python-7154751416?utm_source=api)** | Pavago | `Fullstack` | `Python` `Next.js` | Pakistan | 16/11/2026 |
| **[Full Stack Product Engineer, Merchant Platform](https://himalayas.app/companies/bask-health/jobs/full-stack-product-engineer-merchant-platform?utm_source=api)** | Bask Health | `Fullstack` | - | United States | 16/11/2026 |
| **[Frontend Engineer, New Grad](https://himalayas.app/companies/bask-health/jobs/frontend-engineer-new-grad?utm_source=api)** | Bask Health | `Frontend` | - | United States | 16/11/2026 |

<!-- JOBS_END -->

---

## Cómo funciona

```
cron cada 6 h ──► update-jobs.yml
                    ├─ unittest (81 tests, sin red)
                    ├─ src/main.py ──► fetcher.py ──► classify.py
                    │                   (HTTP + parse)  (tags, categoría, región, filtro)
                    ├─ guard: aborta si hay <20 ofertas o una caída >50 %
                    └─ commit de data/*.json + data/feed.xml + README

push a main ────────► ci.yml (tests en 3.12 y 3.13)
                    └─ deploy-pages.yml (web/ + data/ ──► GitHub Pages)
```

- `data/` es la **única fuente de verdad**. `web/` no guarda copias de los datos.
- El deploy copia `data/` junto al `index.html`, así el dashboard usa la misma ruta en local y en producción.
- Si todas las fuentes fallan, el guard aborta **antes** de escribir: la API pública nunca queda vacía.

## API pública

Tres endpoints estáticos, sin token, sin rate limit y con CORS abierto:

| Recurso | URL |
|:--|:--|
| Vacantes | `https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/jobs.json` |
| Estadísticas | `https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/stats.json` |
| Feed RSS | `https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/feed.xml` |

```bash
curl -s https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/jobs.json \
  | jq '.[0]'
```

```js
const jobs = await (
  await fetch('https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/jobs.json')
).json();

const latam = jobs.filter(j => j.region === 'argentina' || j.region === 'latam');
```

### Esquema de `jobs.json`

| Campo | Tipo | Descripción |
|:--|:--|:--|
| `id` | `string` | Hash estable de 12 caracteres (derivado de la URL) |
| `title` | `string` | Puesto |
| `company` | `string` | Empresa |
| `url` | `string` | Link directo a la postulación original |
| `location` | `string` | Ubicación o restricción geográfica tal como la publica la fuente |
| `region` | `string` | `argentina`, `latam`, `worldwide`, `usa`, `canada`, `europe`, `spain`, `apac`, `africa` u `other` |
| `seniority` | `string \| null` | `junior`, `semi`, `senior` o `lead` (null si el aviso no lo indica) |
| `date` | `string` | `YYYY-MM-DD` (ISO 8601, más reciente primero) |
| `category` | `string` | `Frontend`, `Backend`, `Fullstack`, `AI / Data`, `DevOps / Cloud`, `Mobile` o `General` |
| `tags` | `string[]` | Hasta 5 tecnologías del vocabulario controlado |
| `salary` | `string \| null` | Rango salarial cuando la fuente lo publica |
| `source` | `string` | `RemoteOK`, `WeWorkRemotely`, `Remotive`, `Get on Board` o `Jobicy` |

### Recetas

```bash
# Cantidad de vacantes abiertas para Latam/Argentina
curl -s .../data/jobs.json | jq '[.[] | select(.region=="argentina" or .region=="latam")] | length'

# Vacantes con salario publicado, ordenadas de mayor a menor
curl -s .../data/jobs.json | jq '[.[] | select(.salary != null)] | sort_by(.salary) | reverse | .[:5]'

# Ofertas de Go en los últimos 7 días
curl -s .../data/jobs.json | jq --arg d "$(date -d '7 days ago' +%F)" \
  '[.[] | select((.tags | index("Go")) and .date >= $d)]'
```

### Suscripción RSS

El feed trae las últimas 100 vacantes en RSS 2.0. Pegás la URL en Feedly, NetNewsWire, Thunderbird o cualquier lector y recibís las nuevas sin escribir código:

- Web: <https://leandrocarlino.github.io/dev-remote-jobs-monitor/feed.xml>
- Raw: <https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/feed.xml>

## Región, seniority y fechas

La región se deduce de la ubicación, ignorando acentos:

1. **`argentina`** — Argentina, Buenos Aires, CABA, Córdoba, Rosario, Mendoza…
2. **`latam`** — LATAM, Latin America o cualquiera de los países de la región.
3. **`worldwide`** — remoto global, "anywhere"…
4. El resto se reparte entre `usa`, `canada`, `europe`, `spain`, `apac`, `africa` u `other`.

Get on Board es un tablero regional: cuando dice "Remote", se marca `latam` (remoto dentro de Latam), no `worldwide`.

El **seniority** sale de lo que declara la fuente (Himalayas lo publica) y, si no viene, se deduce del título con límites de palabra: `Senior Backend` → senior, `Semi Senior` / `SSR` → semi, `Jr` / `Trainee` → junior, `Staff` / `Tech Lead` / `Engineering Manager` → lead. "Semi Senior" se evalúa antes que "Senior" para no comerse el prefijo.

La API mantiene `date` en ISO 8601 para que sea fácil de ordenar; el dashboard lo muestra como **dd/mm/yyyy**, con la fecha relativa en el tooltip y un badge **Nuevo** para lo publicado en los últimos 2 días.

## El dashboard

- Búsqueda instantánea (con debounce) por puesto, empresa, tecnología o ubicación.
- Filtros combinables de categoría, región (Latam/AR), fuente y **seniority** (junior, semi, senior, lead).
- Orden por fecha, salario o empresa.
- **Carga por demanda**: la página arranca con 40 tarjetas y un botón **Ver las N restantes** que muestra todas de una vez, así el footer queda cerca.
- **Favoritos** en `localStorage`: marcás con la estrella y volvés cuando quieras.
- Botón **volver arriba** al hacer scroll.
- Enlaces directos a cada postulación y badge de la fuente.

## Calidad de datos

| Problema típico | Qué hace este repo |
|:--|:--|
| Se cuelan ofertas que no son de desarrollo | `is_dev_job`: solo roles de software/IT (nunca "Registered Nurse" ni "Accountant") |
| Categorías erróneas por `if "ai" in titulo` | Reglas con límites de palabra: "p**ai**d" ya no cuenta como IA |
| "Fullstack" como cajón de sastre | Fallback explícito `General`, así los filtros sirven |
| Etiquetas basura (`Medical`, `Travel`) | Vocabulario cerrado de ~75 tecnologías |
| Texto mal codificado por la fuente (`â€”`) | Reparación de mojibake en la normalización |
| Un feed roto vacía la API | Guard: aborta sin escribir si hay <20 ofertas o una caída >50 % |
| Sin tests | 81 tests con `unittest` y fixtures congeladas |

## Correr en local

Solo Python 3.12+. No hay `pip install`:

```bash
# Regenera jobs.json, stats.json, feed.xml y la tabla del README
python src/main.py

# Escribe igual aunque el guard se dispare (primera ejecución)
python src/main.py --force

# Tests
python -m unittest discover -s tests -v

# Preview del dashboard (servir la raíz del repo)
python -m http.server 8000
# → http://localhost:8000/web/
```

## Estructura

```
src/
  classify.py   reglas puras: tags, categorías, región y filtro dev (testeable)
  fetcher.py    HTTP + parsers de las 7 fuentes + dedupe
  main.py       orquestación, guard, stats, README y feed RSS
tests/
  test_classify.py     reglas de clasificación y regiones
  test_fetcher.py      parsers con fixtures, dedupe, guard, README y RSS
  test_dependencies.py verifica que no haya imports de terceros
  fixtures/            payloads congelados de las 7 fuentes
web/
  index.html    dashboard estático (Tailwind CDN + Lucide)
data/
  jobs.json     API pública
  stats.json    agregados para el dashboard y los badges
  feed.xml      feed RSS con las últimas 100 ofertas
docs/
  banner.svg    portada del README
.github/workflows/
  update-jobs.yml  cron de 6 h: tests + crawl + commit
  ci.yml           tests en cada push y PR
  deploy-pages.yml publica web/ + data/ en GitHub Pages
```

## Limitaciones

- Solo el ~33 % de las ofertas trae salario: depende de cada fuente.
- La cobertura argentina es limitada: Get on Board publica poco para AR y el resto de los portales locales no tiene feed público (403).
- 4 commits automáticos por día: el histórico crece. Se puede mover la escritura a una rama `data` o hacer squash periódico.
- Las fuentes cambian de formato sin avisar: los parsers fallan suave y el guard evita publicar datos rotos.

## Roadmap

- [x] Campo `seniority` (junior / semi / senior / lead) y filtro en el dashboard.
- [x] Más fuentes abiertas: Himalayas y Working Nomads.
- [ ] Alertas por Telegram o Discord leyendo el JSON.
- [ ] Filtros compartibles por URL (`?region=latam&cat=backend`).
- [ ] Filtro por salario mínimo.
- [ ] PWA instalable con datos offline.

## Contribuir

Los PRs son bienvenidos. Para agregar una fuente nueva:

1. Sumá un `fetch_*` y un `parse_*` en `src/fetcher.py` (el parser tiene que ser puro).
2. Guardá un fixture real en `tests/fixtures/`.
3. Escribí tests de parseo en `tests/test_fetcher.py`.
4. Registrá el colector en `get_all_jobs()`.

Los tests corren sin red, así que el CI no depende de las fuentes.

## Licencia

MIT — ver [LICENSE](LICENSE). Los datos pertenecen a cada tablero de origen; este repo solo los agrega y enlaza.

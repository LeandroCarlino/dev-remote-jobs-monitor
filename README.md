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

![React](https://img.shields.io/badge/React-36%20vacantes-indigo) ![Python](https://img.shields.io/badge/Python-35%20vacantes-indigo) ![AI](https://img.shields.io/badge/AI-30%20vacantes-indigo) ![Go](https://img.shields.io/badge/Go-23%20vacantes-indigo) ![Java](https://img.shields.io/badge/Java-22%20vacantes-indigo) ![Node](https://img.shields.io/badge/Node-21%20vacantes-indigo) ![JavaScript](https://img.shields.io/badge/JavaScript-19%20vacantes-indigo) ![DevOps](https://img.shields.io/badge/DevOps-18%20vacantes-indigo)

<sub>371 ofertas activas · 7 fuentes · 30% con salario publicado · actualizado cada 6 h</sub>
<!-- STATS_END -->

## Últimas vacantes

<!-- JOBS_START -->
*Última actualización automática: **2026-11-12 23:26 UTC** · Ofertas activas: **371***

| Puesto | Empresa | Categoría | Tags | Ubicación | Fecha |
|:-------|:--------|:----------|:-----|:----------|:------|
| **[Técnico/a de Gestión de Compras IT y Licenciamiento de Software](https://himalayas.app/companies/tecdata-engineering/jobs/tecnico-a-de-gestion-de-compras-it-y-licenciamiento-de-software?utm_source=api)** | TECDATA ENGINEERING | `General` | - | Spain | 12/11/2026 |
| **[Telecom Designer (Buildings Engineering)](https://himalayas.app/companies/michael-baker-international/jobs/telecom-designer-buildings-engineering?utm_source=api)** | Michael Baker International | `General` | - | United States | 12/11/2026 |
| **[Technical Solution Architect](https://himalayas.app/companies/description-ciklum/jobs/technical-solution-architect-9842029977?utm_source=api)** | Description Ciklum | `Backend` | - | Bulgaria | 12/11/2026 |
| **[TLI Mobile Engineer (AI-First / React Native)](https://himalayas.app/companies/together-light-inc/jobs/tli-mobile-engineer-ai-first-react-native?utm_source=api)** | Together Light Inc | `AI / Data` | `AI` `React` `React Native` | India, United States | 12/11/2026 |
| **[Staff Software Engineer (m/f/d)](https://himalayas.app/companies/podero/jobs/staff-software-engineer-m-f-d?utm_source=api)** | Podero | `General` | - | Austria | 12/11/2026 |
| **[Software Engineer Front-end](https://www.getonbrd.com/jobs/software-engineer-frontend-capital-express-santiago)** | Capital Express | `Frontend` | - | Chile · No remote | 12/11/2026 |
| **[Software Engineer - Python - Container Images](https://jobicy.com/jobs/150364-software-engineer-python-container-images)** | Canonical | `General` | `Python` | APAC, EMEA, LATAM, Canada, USA | 12/11/2026 |
| **[Software Developer in Test II](https://himalayas.app/companies/alcor/jobs/software-developer-in-test-ii?utm_source=api)** | Alcor | `General` | - | Colombia | 12/11/2026 |
| **[Site Reliability Engineer](https://himalayas.app/companies/pythian/jobs/site-reliability-engineer-9556351920?utm_source=api)** | Pythian | `DevOps / Cloud` | - | United States | 12/11/2026 |
| **[Senior Software Engineer, Developer Enablement](https://jobicy.com/jobs/161529-senior-software-engineer-developer-enablement)** | Fleetio | `General` | - | Canada, Mexico, USA | 12/11/2026 |
| **[Senior Software Engineer Back-end / Tech Lead](https://www.getonbrd.com/jobs/senior-software-engineer-backend-tech-lead-capital-express-santiago)** | Capital Express | `Backend` | - | Chile · No remote | 12/11/2026 |
| **[Senior Security Operations Engineer](https://jobicy.com/jobs/161527-senior-security-operations-engineer-5)** | Fleetio | `DevOps / Cloud` | `Security` | Canada, Mexico, USA | 12/11/2026 |
| **[Senior QA Engineer](https://jobicy.com/jobs/161629-senior-qa-engineer-4)** | Caylent | `General` | - | Mexico | 12/11/2026 |
| **[Senior Platform Engineer](https://jobicy.com/jobs/161624-senior-platform-engineer-8)** | Caylent | `DevOps / Cloud` | - | Mexico | 12/11/2026 |
| **[Senior Network Engineer](https://himalayas.app/companies/mag-aerospace/jobs/senior-network-engineer?utm_source=api)** | MAG Aerospace | `DevOps / Cloud` | - | United States | 12/11/2026 |
| **[Senior Integration Engineer](https://jobicy.com/jobs/155132-senior-integration-engineer-2)** | Legion | `General` | - | Mexico | 12/11/2026 |
| **[Senior IT Engineer](https://jobicy.com/jobs/161619-senior-it-engineer)** | Caylent | `General` | - | Mexico | 12/11/2026 |
| **[Senior Engineering Manager, Consumer / New Verticals](https://jobicy.com/jobs/161687-senior-engineering-manager-consumer-new-verticals)** | Flex | `General` | - | Anywhere | 12/11/2026 |
| **[Senior DevOps Engineer](https://himalayas.app/companies/codilime/jobs/senior-devops-engineer?utm_source=api)** | CodiLime | `DevOps / Cloud` | `DevOps` | Brazil | 12/11/2026 |
| **[Senior Data engineer](https://himalayas.app/companies/tecdata-engineering/jobs/senior-data-engineer?utm_source=api)** | TECDATA ENGINEERING | `AI / Data` | - | Spain | 12/11/2026 |
| **[Senior Automation QA Engineer](https://himalayas.app/companies/description-ciklum/jobs/senior-automation-qa-engineer-5927650515?utm_source=api)** | Description Ciklum | `General` | - | India | 12/11/2026 |
| **[Senior AI Security Engineer - Pharma](https://himalayas.app/companies/ambit-iberia/jobs/senior-ai-security-engineer-pharma?utm_source=api)** | Ambit Iberia | `AI / Data` | `AI` `Security` | Spain | 12/11/2026 |
| **[Senior AI & Full-Stack Engineer - DevOps & Technical Leadership](https://himalayas.app/companies/m365consult/jobs/senior-ai-full-stack-engineer-devops-technical-leadership-226048140?utm_source=api)** | M365Consult | `Fullstack` | `AI` `DevOps` | Nigeria | 12/11/2026 |
| **[Salesforce Senior Developer](https://www.getonbrd.com/jobs/desarrollador-senior-de-salesforce-datoxmx-yucatan)** | DatoxMX | `General` | `Salesforce` | Mexico · Hybrid | 12/11/2026 |
| **[QA de Automação - Sênior](https://himalayas.app/companies/fcamara/jobs/qa-de-automacao-senior?utm_source=api)** | FCamara | `General` | - | Brazil | 12/11/2026 |

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

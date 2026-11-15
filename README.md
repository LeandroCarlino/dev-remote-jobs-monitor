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

![React](https://img.shields.io/badge/React-38%20vacantes-indigo) ![Python](https://img.shields.io/badge/Python-33%20vacantes-indigo) ![AI](https://img.shields.io/badge/AI-28%20vacantes-indigo) ![Node](https://img.shields.io/badge/Node-25%20vacantes-indigo) ![Go](https://img.shields.io/badge/Go-24%20vacantes-indigo) ![TypeScript](https://img.shields.io/badge/TypeScript-22%20vacantes-indigo) ![JavaScript](https://img.shields.io/badge/JavaScript-21%20vacantes-indigo) ![Java](https://img.shields.io/badge/Java-21%20vacantes-indigo)

<sub>374 ofertas activas · 7 fuentes · 31% con salario publicado · actualizado cada 6 h</sub>
<!-- STATS_END -->

## Últimas vacantes

<!-- JOBS_START -->
*Última actualización automática: **2026-11-15 13:49 UTC** · Ofertas activas: **374***

| Puesto | Empresa | Categoría | Tags | Ubicación | Fecha |
|:-------|:--------|:----------|:-----|:----------|:------|
| **[Technical Architect](https://himalayas.app/companies/talan/jobs/technical-architect?utm_source=api)** | Talan | `Backend` | - | Chile | 15/11/2026 |
| **[Staff SW Engineer, Ground & Control Services](https://himalayas.app/companies/blacksky/jobs/staff-sw-engineer-ground-control-services?utm_source=api)** | BlackSky | `General` | - | United States | 15/11/2026 |
| **[Software Engineer, Backend focus](https://himalayas.app/companies/virtuozzo/jobs/software-engineer-backend-focus?utm_source=api)** | Virtuozzo | `Backend` | - | Albania, Andorra, Austria, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria… | 15/11/2026 |
| **[Site Reliability Engineer](https://jobicy.com/jobs/155391-site-reliability-engineer-4)** | Supabase | `DevOps / Cloud` | - | Anywhere | 15/11/2026 |
| **[ServiceNow System Administrator](https://himalayas.app/companies/general-dynamics-information-technology/jobs/servicenow-system-administrator?utm_source=api)** | General Dynamics Information Technology | `DevOps / Cloud` | - | United States | 15/11/2026 |
| **[Senior Transmission Line Project Engineer- Remote](https://himalayas.app/companies/wsp-africa/jobs/senior-transmission-line-project-engineer-remote?utm_source=api)** | WSP Africa | `General` | - | United States | 15/11/2026 |
| **[Senior Technical Support Engineer - Focused Services](https://himalayas.app/companies/palo-alto-networks/jobs/senior-technical-support-engineer-focused-services-3328005615?utm_source=api)** | Palo Alto Networks | `General` | - | Poland | 15/11/2026 |
| **[Senior Solution Architect](https://himalayas.app/companies/salesforce/jobs/senior-solution-architect?utm_source=api)** | Salesforce | `Backend` | - | Brazil | 15/11/2026 |
| **[Senior Service Desk Engineer](https://himalayas.app/companies/richard-fleischman-associates-inc/jobs/senior-service-desk-engineer?utm_source=api)** | Richard Fleischman & Associates, Inc. | `General` | - | Philippines | 15/11/2026 |
| **[Senior Full Stack Engineer - Experimentation - Product Analytics - NASA - Remote](https://himalayas.app/companies/grafana-labs/jobs/senior-full-stack-engineer-experimentation-product-analytics-nasa-remote?utm_source=api)** | Grafana Labs | `Fullstack` | - | Canada, United States | 15/11/2026 |
| **[Senior Forward Deployed Engineer](https://jobicy.com/jobs/155357-senior-forward-deployed-engineer-2)** | Fleetio | `General` | - | Canada, Mexico, USA | 15/11/2026 |
| **[Senior Enterprise Application Developer (Full Stack)](https://himalayas.app/companies/exponent/jobs/senior-enterprise-application-developer-full-stack?utm_source=api)** | Exponent | `Fullstack` | - | United States | 15/11/2026 |
| **[Senior Databricks Platform Engineer](https://himalayas.app/companies/general-dynamics-information-technology/jobs/senior-databricks-platform-engineer?utm_source=api)** | General Dynamics Information Technology | `DevOps / Cloud` | - | United States | 15/11/2026 |
| **[Senior Data Analyst](https://himalayas.app/companies/hubspot/jobs/senior-data-analyst?utm_source=api)** | HubSpot | `AI / Data` | - | Australia | 15/11/2026 |
| **[Senior Backend Engineer (Go), Tenant Scales: Gitaly](https://himalayas.app/companies/gitlab-com/jobs/senior-backend-engineer-go-tenant-scales-gitaly?utm_source=api)** | GitLab | `Backend` | `Go` | Canada | 15/11/2026 |
| **[Senior Backend Engineer (Go / AWS Streaming)](https://himalayas.app/companies/csquareonline/jobs/senior-backend-engineer-go-aws-streaming?utm_source=api)** | Creative Chaos | `DevOps / Cloud` | `Go` `AWS` | Pakistan | 15/11/2026 |
| **[Senior AI Product Engineer](https://himalayas.app/companies/payfit/jobs/senior-ai-product-engineer?utm_source=api)** | PayFit | `AI / Data` | `AI` | France, Spain | 15/11/2026 |
| **[Senior AI Engineer](https://himalayas.app/companies/osano/jobs/senior-ai-engineer?utm_source=api)** | Osano | `AI / Data` | `AI` | United States | 15/11/2026 |
| **[QA Engineer (Mobile Games)](https://himalayas.app/companies/commit/jobs/qa-engineer-mobile-games?utm_source=api)** | CommIT | `Mobile` | - | Armenia | 15/11/2026 |
| **[QA Engineer](https://himalayas.app/companies/trilogy-federal/jobs/qa-engineer?utm_source=api)** | Trilogy Federal | `General` | - | United States | 15/11/2026 |
| **[Principal Architect](https://himalayas.app/companies/ensemble-health-partners/jobs/principal-architect?utm_source=api)** | Ensemble Health Partners | `Backend` | - | United States | 15/11/2026 |
| **[Presales System Engineer - Network Security (Switzerland)](https://himalayas.app/companies/palo-alto-networks/jobs/presales-system-engineer-network-security-switzerland?utm_source=api)** | Palo Alto Networks | `DevOps / Cloud` | `Security` | Switzerland | 15/11/2026 |
| **[Platform Engineer, Managed Postgres](https://jobicy.com/jobs/155389-platform-engineer-managed-postgres)** | Supabase | `DevOps / Cloud` | `PostgreSQL` | Anywhere | 15/11/2026 |
| **[Mechanical Engineer, Data Centers - Remote (U.S.)](https://himalayas.app/companies/aecom/jobs/mechanical-engineer-data-centers-remote-u-s?utm_source=api)** | AECOM | `General` | - | United States | 15/11/2026 |
| **[ML Engineer (MSc. or PhD)](https://himalayas.app/companies/micro1/jobs/ml-engineer-msc-or-phd?utm_source=api)** | micro1 | `AI / Data` | `ML` | Worldwide | 15/11/2026 |

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

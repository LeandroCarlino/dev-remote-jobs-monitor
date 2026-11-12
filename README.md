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

Las búsquedas remotas globales están llenas de ofertas que no son de desarrollo y de puestos que no admiten Latam. Los tableros locales, en cambio, casi nunca tienen API. Este repo junta **cinco fuentes abiertas**, filtra lo que no es un rol técnico, deduce la región y publica todo como **JSON y RSS** que cualquiera puede consumir sin registrarse.

## Qué incluye

| Producto | Datos | Ingeniería |
|:--|:--|:--|
| Dashboard con búsqueda, filtros combinables, orden, favoritos y carga por demanda | 5 fuentes abiertas, deduplicadas y normalizadas | 67 tests offline, cero dependencias |
| Fechas en formato argentino y badge `Nuevo` | API JSON + feed RSS públicos | CI en Python 3.12 y 3.13 |
| Filtro **Latam/AR** y badges de región | Vocabulario controlado de ~75 tecnologías | Guard que impide publicar datos rotos |

## Fuentes

| Fuente | Cobertura | Acceso | Qué aporta |
|:--|:--|:--|:--|
| [RemoteOK](https://remoteok.com) | Global | API JSON | Volumen y salarios en USD |
| [WeWorkRemotely](https://weworkremotely.com) | Global | RSS (Programming / DevOps) | Ofertas de empresas grandes |
| [Remotive](https://remotive.com) | Global | API JSON | Categoría software-dev |
| [Get on Board](https://www.getonbrd.com) | **Latam** | API v0 pública | Chile, Argentina, Colombia, Perú, México y remoto regional |
| [Jobicy](https://jobicy.com) | Global con `geo=latam` | API JSON | Empresas que contratan en Argentina y Latam |

> [!NOTE]
> Todas las vacantes enlazan a la publicación original. Jobicy y Get on Board se acreditan acá y en el sitio, como piden sus términos de API. No se scrapea ningún portal que bloquee el acceso automatizado.

<!-- STATS_START -->
### Tecnologías con más demanda hoy

![React](https://img.shields.io/badge/React-32%20vacantes-indigo) ![Python](https://img.shields.io/badge/Python-29%20vacantes-indigo) ![Go](https://img.shields.io/badge/Go-25%20vacantes-indigo) ![AI](https://img.shields.io/badge/AI-25%20vacantes-indigo) ![Node](https://img.shields.io/badge/Node-22%20vacantes-indigo) ![Java](https://img.shields.io/badge/Java-19%20vacantes-indigo) ![AWS](https://img.shields.io/badge/AWS-18%20vacantes-indigo) ![TypeScript](https://img.shields.io/badge/TypeScript-16%20vacantes-indigo)

<sub>308 ofertas activas · 33% con salario publicado · actualizado cada 6 h</sub>
<!-- STATS_END -->

## Últimas vacantes

<!-- JOBS_START -->
*Última actualización automática: **2026-11-12 07:31 UTC** · Ofertas activas: **308***

| Puesto | Empresa | Categoría | Tags | Ubicación | Fecha |
|:-------|:--------|:----------|:-----|:----------|:------|
| **[Software Engineer - Python - Container Images](https://jobicy.com/jobs/150364-software-engineer-python-container-images)** | Canonical | `General` | `Python` | APAC, EMEA, LATAM, Canada, USA | 12/11/2026 |
| **[Senior Integration Engineer](https://jobicy.com/jobs/155132-senior-integration-engineer-2)** | Legion | `General` | - | Mexico | 12/11/2026 |
| **[Open Source Networking Software Engineer - ToR Switch / SmartNIC / DPU](https://jobicy.com/jobs/150360-open-source-networking-software-engineer-tor-switch-smartnic-dpu)** | Canonical | `General` | - | APAC, LATAM, Canada, China, USA | 12/11/2026 |
| **[Software Engineer(python)](https://www.getonbrd.com/jobs/software-engineer-python-softtechassociate-remote)** | Softtechassociate | `General` | `Python` | Remote · Fully remote | 11/11/2026 |
| **[Senior Software Engineer, Observability (Go)](https://www.getonbrd.com/jobs/senior-software-engineer-observability-go-fastcto-remote)** | FastCTO | `Backend` | `Go` | Remote · Remote (local) | 11/11/2026 |
| **[Senior Software Engineer, Data Product](https://jobicy.com/jobs/155044-senior-software-engineer-data-product)** | TRM Labs | `General` | - | LATAM | 11/11/2026 |
| **[Senior Fullstack Engineer](https://jobicy.com/jobs/161444-senior-fullstack-engineer-4)** | Toptal | `Fullstack` | - | LATAM, Europe | 11/11/2026 |
| **[Senior Data Analyst](https://jobicy.com/jobs/152859-senior-data-analyst)** | Tremendous | `AI / Data` | - | LATAM, Canada, USA | 11/11/2026 |
| **[Semi Senior Full-Stack Java Developer (QA & AI) Bilingüe](https://www.getonbrd.com/jobs/semi-senior-full-stack-java-developer-qa-ai-bilingue-23people-santiago)** | 23people | `Fullstack` | `AI` `Java` | Chile · Hybrid | 11/11/2026 |
| **[Full-Stack Engineer (TypeScript, Next.JS, Postgres)](https://www.getonbrd.com/jobs/full-stack-engineer-typescript-next-js-postgres-opsbox-ai-remote)** | OpsBox AI | `Fullstack` | `TypeScript` `Next.js` `PostgreSQL` | Remote · Remote (local) | 11/11/2026 |
| **[Full Stack Engineer](https://jobicy.com/jobs/161435-full-stack-engineer-9)** | 3Y Health | `Fullstack` | - | Argentina | 11/11/2026 |
| **[Full Stack AI Engineer](https://jobicy.com/jobs/161438-full-stack-ai-engineer)** | 3Y Health | `Fullstack` | `AI` | Argentina | 11/11/2026 |
| **[Founding Engineer](https://jobicy.com/jobs/161432-founding-engineer)** | 3Y Health | `General` | - | Argentina | 11/11/2026 |
| **[Devops Engineer (Azure)](https://jobicy.com/jobs/161433-devops-engineer-azure)** | Particle41 | `DevOps / Cloud` | `Azure` `DevOps` | Mexico | 11/11/2026 |
| **[Devops Engineer (AWS)](https://jobicy.com/jobs/161429-devops-engineer-aws)** | Particle41 | `DevOps / Cloud` | `AWS` `DevOps` | Argentina | 11/11/2026 |
| **[Developer IA (Go/Node.js/React/GCP)](https://www.getonbrd.com/jobs/developer-ia-go-node-react-gcp-agilistik-santiago)** | Agilistik | `DevOps / Cloud` | `React` `Node` `Go` | Chile · Hybrid | 11/11/2026 |
| **[DevOps Engineer (GCP)](https://jobicy.com/jobs/161436-devops-engineer-gcp)** | Particle41 | `DevOps / Cloud` | `GCP` `DevOps` | Mexico | 11/11/2026 |
| **[DevOps](https://www.getonbrd.com/jobs/dev-ops-cumplo-santiago)** | Cumplo | `DevOps / Cloud` | `DevOps` | Chile · Hybrid | 11/11/2026 |
| **[Dev Full-Stack Integraciones [Contractor]](https://www.getonbrd.com/jobs/dev-fullstack-ror-react-integraciones-rankmi-santiago)** | Rankmi | `Fullstack` | - | Remote · Remote (local) | 11/11/2026 |
| **[Desarrollador/a Front-end React](https://www.getonbrd.com/jobs/desarrollador-a-frontend-react-42labs-santiago)** | 42Labs | `Frontend` | `React` | Chile · Hybrid | 11/11/2026 |
| **[Desarrollador/a Back-end Python (AWS)](https://www.getonbrd.com/jobs/desarrollador-a-backend-python-aws-42labs-santiago)** | 42Labs | `DevOps / Cloud` | `Python` `AWS` | Chile · Hybrid | 11/11/2026 |
| **[Data Engineer (Tableau)](https://jobicy.com/jobs/161424-data-engineer-tableau)** | Particle41 | `AI / Data` | - | Argentina | 11/11/2026 |
| **[AI Product Engineer](https://jobicy.com/jobs/161428-ai-product-engineer)** | 3Y Health | `AI / Data` | `AI` | Argentina | 11/11/2026 |
| **[Support Engineer (AMER - Weekends)](https://jobicy.com/jobs/152807-support-engineer-amer-weekends)** | Supabase | `General` | - | LATAM, Canada, USA | 10/11/2026 |
| **[Staff Corporate IT Engineer](https://jobicy.com/jobs/161109-staff-corporate-it-engineer)** | Wellhub | `General` | - | Brazil | 10/11/2026 |

<!-- JOBS_END -->

---

## Cómo funciona

```
cron cada 6 h ──► update-jobs.yml
                    ├─ unittest (67 tests, sin red)
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

## Región y fechas

La región se deduce de la ubicación, ignorando acentos:

1. **`argentina`** — Argentina, Buenos Aires, CABA, Córdoba, Rosario, Mendoza…
2. **`latam`** — LATAM, Latin America o cualquiera de los países de la región.
3. **`worldwide`** — remoto global, "anywhere"…
4. El resto se reparte entre `usa`, `canada`, `europe`, `spain`, `apac`, `africa` u `other`.

Get on Board es un tablero regional: cuando dice "Remote", se marca `latam` (remoto dentro de Latam), no `worldwide`.

La API mantiene `date` en ISO 8601 para que sea fácil de ordenar; el dashboard lo muestra como **dd/mm/yyyy**, con la fecha relativa en el tooltip y un badge **Nuevo** para lo publicado en los últimos 2 días.

## El dashboard

- Búsqueda instantánea (con debounce) por puesto, empresa, tecnología o ubicación.
- Filtros combinables de categoría, región (Latam/AR) y fuente.
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
| Sin tests | 67 tests con `unittest` y fixtures congeladas |

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
  fetcher.py    HTTP + parsers de las 5 fuentes + dedupe
  main.py       orquestación, guard, stats, README y feed RSS
tests/
  test_classify.py     reglas de clasificación y regiones
  test_fetcher.py      parsers con fixtures, dedupe, guard, README y RSS
  test_dependencies.py verifica que no haya imports de terceros
  fixtures/            payloads congelados de las 5 fuentes
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

- [ ] Campo `seniority` (junior / semi / senior) parseado del título.
- [ ] Alertas por Telegram o Discord leyendo el JSON.
- [ ] Más fuentes abiertas: Himalayas, Working Nomads.
- [ ] Filtros compartibles por URL (`?region=latam&cat=backend`).
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

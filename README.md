# 💼 DevRemoteJobs Monitor & Public API

> **Monitor automatizado de ofertas de trabajo remoto para desarrolladores.**
> Rastreo cada 6 horas vía GitHub Actions. Cero servidores, 100% gratuito.

[![Update Remote Jobs](https://github.com/LeandroCarlino/dev-remote-jobs-monitor/actions/workflows/update-jobs.yml/badge.svg)](https://github.com/LeandroCarlino/dev-remote-jobs-monitor/actions/workflows/update-jobs.yml)
[![CI](https://github.com/LeandroCarlino/dev-remote-jobs-monitor/actions/workflows/ci.yml/badge.svg)](https://github.com/LeandroCarlino/dev-remote-jobs-monitor/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![API Status](https://img.shields.io/badge/API-Active%20%26%20Free-emerald.svg)](https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/jobs.json)

**Dashboard:** <https://leandrocarlino.github.io/dev-remote-jobs-monitor/>

---

## ¿Qué es esto?

Un repositorio que es a la vez **un dashboard web** y **una API JSON pública y gratuita** con vacantes remotas de desarrollo, consolidadas desde:

- **RemoteOK** — global
- **WeWorkRemotely** — global (Programming & DevOps)
- **Remotive** — global (Software Dev)
- **Get on Board** — LATAM (Chile, Argentina, Colombia, Perú, México y remoto regional)
- **Jobicy** — global filtrado a `geo=latam`

Todo el pipeline (fetch → normalización → deduplicación → publicación) corre en la nube, gratis, dentro de **GitHub Actions**. No hay backend, ni base de datos, ni cuota de API.

### Diferencias con un scraper ingenuo
| Problema típico | Qué hace este repo |
|:--|:--|
| Se cuelan ofertas que no son de desarrollo | Filtro `is_dev_job`: solo roles de software/IT (nunca "Registered Nurse" ni "Accountant") |
| Categorías erróneas por `if "ai" in titulo` | Reglas con límites de palabra: "p**ai**d" ya no cuenta como IA |
| Categoría "Fullstack" como cajón de sastre | Fallback explícito `General`, así los filtros del dashboard sirven |
| Etiquetas basura (`Medical`, `Travel`) | Vocabulario cerrado de ~75 tecnologías |
| Todo parece "remoto global" | Campo `region` (`argentina`, `latam`, `worldwide`, ...) y filtro Latam/AR en el dashboard |
| Un feed roto vacía la API pública | Guard: aborta sin escribir si hay <20 ofertas o una caída >50% |
| Sin tests | 61 tests con `unittest` y fixtures congeladas (cero dependencias) |

### El dashboard

- **Búsqueda instantánea** con debounce por puesto, empresa, tecnología o ubicación.
- **Filtros**: categoría, región (Latam/AR) y fuente, combinables.
- **Orden**: más recientes, más antiguas, mejor salario o empresa A-Z.
- **Paginación** de 40 en 40 (no se renderizan 300 tarjetas de golpe).
- **Favoritos** guardados en `localStorage`: marcás ofertas con la estrella y volvés cuando quieras.
- **Fechas en formato argentino** (`dd/mm/yyyy`) + "hace N días" + badge `Nuevo`.
- **Enlaces directos** a la postulación y a la fuente original.

---

<!-- STATS_START -->
### Tecnologías con más demanda hoy

![React](https://img.shields.io/badge/React-32%20vacantes-indigo) ![Python](https://img.shields.io/badge/Python-29%20vacantes-indigo) ![Go](https://img.shields.io/badge/Go-25%20vacantes-indigo) ![AI](https://img.shields.io/badge/AI-25%20vacantes-indigo) ![Node](https://img.shields.io/badge/Node-22%20vacantes-indigo) ![Java](https://img.shields.io/badge/Java-19%20vacantes-indigo) ![AWS](https://img.shields.io/badge/AWS-18%20vacantes-indigo) ![TypeScript](https://img.shields.io/badge/TypeScript-16%20vacantes-indigo)

<sub>308 ofertas activas · 33% con salario publicado · actualizado cada 6 h</sub>
<!-- STATS_END -->

## Últimas vacantes

<!-- JOBS_START -->
*Última actualización automática: **2026-11-12 07:23 UTC** · Ofertas activas: **308***

| Puesto | Empresa | Categoría | Tags | Ubicación | Fecha |
|:-------|:--------|:----------|:-----|:----------|:------|
| **[Software Engineer - Python - Container Images](https://jobicy.com/jobs/150364-software-engineer-python-container-images)** | Canonical | `General` | `Python` | APAC, EMEA, LATAM, Canada, USA | 2026-11-12 |
| **[Senior Integration Engineer](https://jobicy.com/jobs/155132-senior-integration-engineer-2)** | Legion | `General` | - | Mexico | 2026-11-12 |
| **[Open Source Networking Software Engineer - ToR Switch / SmartNIC / DPU](https://jobicy.com/jobs/150360-open-source-networking-software-engineer-tor-switch-smartnic-dpu)** | Canonical | `General` | - | APAC, LATAM, Canada, China, USA | 2026-11-12 |
| **[Software Engineer(python)](https://www.getonbrd.com/jobs/software-engineer-python-softtechassociate-remote)** | Softtechassociate | `General` | `Python` | Remote · Fully remote | 2026-11-11 |
| **[Senior Software Engineer, Observability (Go)](https://www.getonbrd.com/jobs/senior-software-engineer-observability-go-fastcto-remote)** | FastCTO | `Backend` | `Go` | Remote · Remote (local) | 2026-11-11 |
| **[Senior Software Engineer, Data Product](https://jobicy.com/jobs/155044-senior-software-engineer-data-product)** | TRM Labs | `General` | - | LATAM | 2026-11-11 |
| **[Senior Fullstack Engineer](https://jobicy.com/jobs/161444-senior-fullstack-engineer-4)** | Toptal | `Fullstack` | - | LATAM, Europe | 2026-11-11 |
| **[Senior Data Analyst](https://jobicy.com/jobs/152859-senior-data-analyst)** | Tremendous | `AI / Data` | - | LATAM, Canada, USA | 2026-11-11 |
| **[Semi Senior Full-Stack Java Developer (QA & AI) Bilingüe](https://www.getonbrd.com/jobs/semi-senior-full-stack-java-developer-qa-ai-bilingue-23people-santiago)** | 23people | `Fullstack` | `AI` `Java` | Chile · Hybrid | 2026-11-11 |
| **[Full-Stack Engineer (TypeScript, Next.JS, Postgres)](https://www.getonbrd.com/jobs/full-stack-engineer-typescript-next-js-postgres-opsbox-ai-remote)** | OpsBox AI | `Fullstack` | `TypeScript` `Next.js` `PostgreSQL` | Remote · Remote (local) | 2026-11-11 |
| **[Full Stack Engineer](https://jobicy.com/jobs/161435-full-stack-engineer-9)** | 3Y Health | `Fullstack` | - | Argentina | 2026-11-11 |
| **[Full Stack AI Engineer](https://jobicy.com/jobs/161438-full-stack-ai-engineer)** | 3Y Health | `Fullstack` | `AI` | Argentina | 2026-11-11 |
| **[Founding Engineer](https://jobicy.com/jobs/161432-founding-engineer)** | 3Y Health | `General` | - | Argentina | 2026-11-11 |
| **[Devops Engineer (Azure)](https://jobicy.com/jobs/161433-devops-engineer-azure)** | Particle41 | `DevOps / Cloud` | `Azure` `DevOps` | Mexico | 2026-11-11 |
| **[Devops Engineer (AWS)](https://jobicy.com/jobs/161429-devops-engineer-aws)** | Particle41 | `DevOps / Cloud` | `AWS` `DevOps` | Argentina | 2026-11-11 |
| **[Developer IA (Go/Node.js/React/GCP)](https://www.getonbrd.com/jobs/developer-ia-go-node-react-gcp-agilistik-santiago)** | Agilistik | `DevOps / Cloud` | `React` `Node` `Go` | Chile · Hybrid | 2026-11-11 |
| **[DevOps Engineer (GCP)](https://jobicy.com/jobs/161436-devops-engineer-gcp)** | Particle41 | `DevOps / Cloud` | `GCP` `DevOps` | Mexico | 2026-11-11 |
| **[DevOps](https://www.getonbrd.com/jobs/dev-ops-cumplo-santiago)** | Cumplo | `DevOps / Cloud` | `DevOps` | Chile · Hybrid | 2026-11-11 |
| **[Dev Full-Stack Integraciones [Contractor]](https://www.getonbrd.com/jobs/dev-fullstack-ror-react-integraciones-rankmi-santiago)** | Rankmi | `Fullstack` | - | Remote · Remote (local) | 2026-11-11 |
| **[Desarrollador/a Front-end React](https://www.getonbrd.com/jobs/desarrollador-a-frontend-react-42labs-santiago)** | 42Labs | `Frontend` | `React` | Chile · Hybrid | 2026-11-11 |
| **[Desarrollador/a Back-end Python (AWS)](https://www.getonbrd.com/jobs/desarrollador-a-backend-python-aws-42labs-santiago)** | 42Labs | `DevOps / Cloud` | `Python` `AWS` | Chile · Hybrid | 2026-11-11 |
| **[Data Engineer (Tableau)](https://jobicy.com/jobs/161424-data-engineer-tableau)** | Particle41 | `AI / Data` | - | Argentina | 2026-11-11 |
| **[AI Product Engineer](https://jobicy.com/jobs/161428-ai-product-engineer)** | 3Y Health | `AI / Data` | `AI` | Argentina | 2026-11-11 |
| **[Support Engineer (AMER - Weekends)](https://jobicy.com/jobs/152807-support-engineer-amer-weekends)** | Supabase | `General` | - | LATAM, Canada, USA | 2026-11-10 |
| **[Staff Corporate IT Engineer](https://jobicy.com/jobs/161109-staff-corporate-it-engineer)** | Wellhub | `General` | - | Brazil | 2026-11-10 |

<!-- JOBS_END -->

---

## API pública

Tres endpoints estáticos, sin token, sin rate limit y con CORS abierto:

```bash
curl https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/jobs.json
curl https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/stats.json
curl https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/feed.xml
```

```js
const jobs = await (
  await fetch('https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/jobs.json')
).json();
```

### Suscripción RSS

Además del JSON hay un feed **RSS 2.0** con las últimas 100 vacantes:

- Web: <https://leandrocarlino.github.io/dev-remote-jobs-monitor/feed.xml>
- Raw: <https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/feed.xml>

Funciona en cualquier lector (Feedly, NetNewsWire, Thunderbird): agregás la URL y recibís las ofertas nuevas sin escribir una línea de código.

### Fechas

La API mantiene `date` en **ISO 8601** (`YYYY-MM-DD`) para que sea fácil de ordenar y parsear. El dashboard muestra el formato argentino **dd/mm/yyyy**, con la fecha relativa ("hoy", "ayer", "hace 3 días") en el tooltip y un badge **Nuevo** para las publicadas en los últimos 2 días.

### Esquema de `jobs.json`

| Campo | Tipo | Descripción |
|:--|:--|:--|
| `id` | string | Hash estable de 12 chars (URL de la oferta) |
| `title` | string | Puesto |
| `company` | string | Empresa |
| `url` | string | Link directo de postulación |
| `location` | string | Ubicación o restricción geográfica |
| `region` | string | `argentina`, `latam`, `worldwide`, `usa`, `canada`, `europe`, `spain`, `apac`, `africa` u `other` |
| `date` | string | `YYYY-MM-DD` (más reciente primero) |
| `category` | string | `Frontend`, `Backend`, `Fullstack`, `AI / Data`, `DevOps / Cloud`, `Mobile` o `General` |
| `tags` | string[] | Hasta 5 tecnologías del vocabulario controlado |
| `salary` | string \| null | Rango salarial cuando la fuente lo publica |
| `source` | string | `RemoteOK`, `WeWorkRemotely` o `Remotive` |

### Foco Latam y Argentina

El dashboard tiene un filtro **Latam/AR** que muestra las ofertas con `region` = `argentina` o `latam`:

```bash
# Solo vacantes abiertas para Latam/Argentina
curl -s https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/jobs.json \
  | jq '[.[] | select(.region == "argentina" or .region == "latam")] | length'
```

Cómo se decide la región:

1. **Argentina** — la ubicación menciona Argentina, Buenos Aires, CABA, Córdoba, Rosario, Mendoza, etc.
2. **Latam** — LATAM, Latin America, o cualquiera de los países de la región.
3. **Get on Board** siempre cae en `latam` cuando su país es "Remote": es un tablero regional, así que "remoto" ahí significa remoto dentro de Latam.
4. El resto se reparte entre `worldwide`, `usa`, `europe`, `apac`… y `other` si no hay pista.

> **Nota honesta sobre Argentina:** los tableros con más volumen local (Computrabajo, Bumeran, ZonaJobs) no ofrecen feed público y bloquean el acceso automatizado (403), así que no están integrados. La cobertura AR actual viene de Get on Board y Jobicy. Si querés sumar volumen argentino de verdad, la vía limpia es la API de Adzuna (`adzuna.com.ar`, gratis con `app_id`/`app_key`) — se puede cablear con dos secrets de GitHub.

---

```
cron (cada 6 h) ──► update-jobs.yml
                      ├─ unittest (46 tests, sin red)
                      ├─ src/main.py ──► src/fetcher.py ──► src/classify.py
                      │                   (fetch + parse)     (tags/categorías/filtro)
                      ├─ guard anti-vacío
                      └─ commit de data/*.json + README si cambió algo

push a main ──────────► ci.yml (tests en Python 3.12 y 3.13)
                      └─ deploy-pages.yml (web/ + data/ ──► GitHub Pages)
```

- `data/` es la **única fuente de verdad** de los datos. `web/` no guarda copias.
- En cada deploy se copia `data/` junto al `index.html`, así el dashboard consume `data/jobs.json` con la misma ruta en local y en producción.

---

## Ejecutar en local

Sin dependencias: solo Python 3.12+.

```bash
# Regenerar data/jobs.json, data/stats.json y la tabla del README
python src/main.py

# Forzar la escritura aunque el guard se dispare (primera ejecución vacía)
python src/main.py --force

# Preview del dashboard: sirve la raíz del repo
python -m http.server 8000
# → http://localhost:8000/web/

# Tests
python -m unittest discover -s tests -v
```

## Estructura

```
src/
  classify.py   reglas puras: tags, categorías, región, filtro dev (testeable)
  fetcher.py    HTTP + parsers de las 5 fuentes + dedupe
  main.py       orquestación, guard anti-vacío, stats y README
tests/
  test_classify.py     reglas de clasificación y regiones
  test_fetcher.py      parsers con fixtures, dedupe, guard, README
  test_dependencies.py verifica que no haya imports de terceros
  fixtures/            payloads congelados de las 5 fuentes
web/
  index.html    dashboard estático (Tailwind CDN + Lucide)
data/
  jobs.json     API pública
  stats.json    agregados para el dashboard y los badges
  feed.xml      feed RSS con las últimas 100 ofertas
```

## Limitaciones conocidas

- Solo el ~33% de las ofertas trae salario: depende de cada fuente.
- La cobertura argentina es baja (Get on Board publica pocas vacantes AR; el resto de los portales locales bloquea scraping). Ver la nota sobre Adzuna arriba.
- 4 commits automáticos al día: el histórico del repo crece. Si molesta, se puede mover la escritura a una rama `data` o squash periódico.
- Las fuentes cambian de formato sin avisar; los parsers fallan suave y el guard evita publicar datos rotos.

## Licencia

MIT — ver [LICENSE](LICENSE).

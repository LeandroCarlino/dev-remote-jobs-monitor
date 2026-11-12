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

- **RemoteOK**
- **WeWorkRemotely** (Programming & DevOps)
- **Remotive** (Software Dev)

Todo el pipeline (fetch → normalización → deduplicación → publicación) corre en la nube, gratis, dentro de **GitHub Actions**. No hay backend, ni base de datos, ni cuota de API.

### Diferencias con un scraper ingenuo

| Problema típico | Qué hace este repo |
|:--|:--|
| Se cuelan ofertas que no son de desarrollo | Filtro `is_dev_job`: solo roles de software/IT (nunca "Registered Nurse" ni "Accountant") |
| Categorías erróneas por `if "ai" in titulo` | Reglas con límites de palabra: "p**ai**d" ya no cuenta como IA |
| Categoría "Fullstack" como cajón de sastre | Fallback explícito `General`, así los filtros del dashboard sirven |
| Etiquetas basura (`Medical`, `Travel`) | Vocabulario cerrado de ~70 tecnologías |
| Un feed roto vacía la API pública | Guard: aborta sin escribir si hay <20 ofertas o una caída >50% |
| Sin tests | 46 tests con `unittest` y fixtures congeladas (cero dependencias) |

---

<!-- STATS_START -->
### Tecnologías con más demanda hoy

![Python](https://img.shields.io/badge/Python-18%20vacantes-indigo) ![Go](https://img.shields.io/badge/Go-18%20vacantes-indigo) ![AI](https://img.shields.io/badge/AI-13%20vacantes-indigo) ![JavaScript](https://img.shields.io/badge/JavaScript-12%20vacantes-indigo) ![TypeScript](https://img.shields.io/badge/TypeScript-10%20vacantes-indigo) ![React](https://img.shields.io/badge/React-10%20vacantes-indigo) ![DevOps](https://img.shields.io/badge/DevOps-7%20vacantes-indigo) ![Docker](https://img.shields.io/badge/Docker-6%20vacantes-indigo)

<sub>82 ofertas activas · 21% con salario publicado · actualizado cada 6 h</sub>
<!-- STATS_END -->

## Últimas vacantes

<!-- JOBS_START -->
*Última actualización automática: **2026-11-12 07:03 UTC** · Ofertas activas: **82***

| Puesto | Empresa | Categoría | Tags | Ubicación | Fecha |
|:-------|:--------|:----------|:-----|:----------|:------|
| **[Senior React Full-stack Developer](https://remotive.com/remote-jobs/software-development/senior-react-full-stack-developer-2091136)** | Lemon.io | `Fullstack` | `Python` `JavaScript` `TypeScript` | LATAM, Europe, USA, Canada, APAC | 2026-11-10 |
| **[Data Engineer](https://remoteOK.com/remote-jobs/remote-data-engineer-addepto-1137714)** | Addepto | `AI / Data` | `Python` `Salesforce` | Worldwide Remote | 2026-11-10 |
| **[Cloud Engineer](https://weworkremotely.com/remote-jobs/knack-cloud-engineer-1)** | Knack | `DevOps / Cloud` | - | Worldwide / Remote | 2026-11-10 |
| **[Senior Software Engineer — Kubernetes Control Plane](https://remoteOK.com/remote-jobs/remote-senior-software-engineer-kubernetes-control-plane-buoyant-1137713)** | Buoyant | `DevOps / Cloud` | `Go` `Kubernetes` | Worldwide Remote | 2026-11-09 |
| **[Senior Backend Cloud Engineer](https://weworkremotely.com/remote-jobs/halcyon-senior-backend-cloud-engineer)** | Halcyon | `DevOps / Cloud` | - | Worldwide / Remote | 2026-11-09 |
| **[Senior Agentic AI Engineer NDA](https://remoteOK.com/remote-jobs/remote-senior-agentic-ai-engineer-nda-gt-1137710)** | GT | `AI / Data` | `AI` `Python` `React` | Warsaw | 2026-11-09 |
| **[Full-Stack Platform Engineer](https://weworkremotely.com/remote-jobs/edgewater-federal-solutions-inc-full-stack-platform-engineer)** | Edgewater Federal Solutions, Inc. | `Fullstack` | - | Worldwide / Remote | 2026-11-09 |
| **[UI Developer](https://remoteOK.com/remote-jobs/remote-ui-developer-rainfocus-1137704)** | RainFocus | `Frontend` | `JavaScript` `React` `Java` | Any State | 2026-11-08 |
| **[Tier III Service Desk Engineer](https://remotive.com/remote-jobs/information-technology/tier-iii-service-desk-engineer-2091045)** | Unio Digital | `DevOps / Cloud` | `Azure` `Security` | Worldwide | 2026-11-07 |
| **[AI Developer](https://remoteOK.com/remote-jobs/remote-ai-developer-salvo-software-1137701)** | Salvo Software | `AI / Data` | `AI` `Python` `Go` | Worldwide Remote | 2026-11-07 |
| **[Senior Vue Developer](https://remoteOK.com/remote-jobs/remote-senior-vue-developer-lemon-io-1137688)** | Lemon.io | `Frontend` | `Python` `JavaScript` `TypeScript` | Worldwide Remote | 2026-11-05 |
| **[Senior Staff Infrastructure & Security Engineer](https://remoteOK.com/remote-jobs/remote-senior-staff-infrastructure-security-engineer-civilgrid-1137687)** | CivilGrid | `DevOps / Cloud` | `DevOps` `Security` | Boston | 2026-11-05 |
| **[ML Inference Engineer – Terminal-Bench Task Designer (vLLM / SGLang / TensorRT-LLM)](https://remoteOK.com/remote-jobs/remote-ml-inference-engineer-terminal-bench-task-designer-vllm-sglang-tensorrt-llm-toptal-1137689)** | Toptal | `AI / Data` | `ML` `LLM` `Docker` | Anywhere in the World | 2026-11-05 |
| **[Feltsense AI Engineer](https://remoteOK.com/remote-jobs/remote-feltsense-ai-engineer-silver-dev-1137691)** | Silver.dev | `AI / Data` | `AI` `JavaScript` `TypeScript` | Worldwide Remote | 2026-11-05 |
| **[Software Engineer](https://remoteOK.com/remote-jobs/remote-software-engineer-claims-1137685)** | Claims | `AI / Data` | `AI` `Blockchain` | Worldwide Remote | 2026-11-04 |
| **[Tech lead](https://remoteOK.com/remote-jobs/remote-tech-lead-ringbook-limited-1137673)** | Ringbook Limited | `General` | - | Worldwide Remote | 2026-11-03 |
| **[Software Engineer Infrastructure](https://remoteOK.com/remote-jobs/remote-software-engineer-infrastructure-sodalis-inc-1137614)** | Sodalis, Inc. | `DevOps / Cloud` | `Go` `Ruby` | Palo Alto | 2026-11-02 |
| **[Salesforce Business Systems Administrator](https://weworkremotely.com/remote-jobs/salesloft-salesforce-business-systems-administrator)** | Salesloft | `DevOps / Cloud` | `Salesforce` | Worldwide / Remote | 2026-11-02 |
| **[AI ML Engineer](https://remoteOK.com/remote-jobs/remote-ai-ml-engineer-docusketch-1137619)** | Docusketch | `AI / Data` | `AI` `ML` `Machine Learning` | Worldwide Remote | 2026-11-02 |
| **[Sr. IT Systems Engineer](https://weworkremotely.com/remote-jobs/carrot-sr-it-systems-engineer)** | Carrot | `DevOps / Cloud` | - | Worldwide / Remote | 2026-10-30 |
| **[DevOps Engineer, Edge and Developer Experience (Remote Eligible in Bulgaria)](https://weworkremotely.com/remote-jobs/smartsheet-devops-engineer-edge-and-developer-experience-remote-eligible-in-bulgaria)** | Smartsheet | `DevOps / Cloud` | `DevOps` | Worldwide / Remote | 2026-10-30 |
| **[CloudOps Engineer (Network Engineer)](https://weworkremotely.com/remote-jobs/wrike-cloudops-engineer-network-engineer)** | Wrike | `DevOps / Cloud` | - | Worldwide / Remote | 2026-10-30 |
| **[Autonomous Systems Security Engineer](https://weworkremotely.com/remote-jobs/anthropic-autonomous-systems-security-engineer)** | Anthropic | `DevOps / Cloud` | `Security` | Worldwide / Remote | 2026-10-30 |
| **[AWS Cloud Solutions Architect](https://remoteOK.com/remote-jobs/remote-aws-cloud-solutions-architect-cloudary-sas-1137606)** | Cloudary SAS | `DevOps / Cloud` | `Go` `SQL` `PostgreSQL` | Worldwide Remote | 2026-10-30 |
| **[Principal Data Engineer](https://weworkremotely.com/remote-jobs/zoominfo-technologies-llc-principal-data-engineer)** | ZoomInfo Technologies LLC | `AI / Data` | - | Worldwide / Remote | 2026-10-29 |

<!-- JOBS_END -->

---

## API pública

Dos endpoints estáticos, sin token, sin rate limit y con CORS abierto:

```bash
curl https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/jobs.json
curl https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/stats.json
```

```js
const jobs = await (
  await fetch('https://raw.githubusercontent.com/LeandroCarlino/dev-remote-jobs-monitor/main/data/jobs.json')
).json();
```

### Esquema de `jobs.json`

| Campo | Tipo | Descripción |
|:--|:--|:--|
| `id` | string | Hash estable de 12 chars (URL de la oferta) |
| `title` | string | Puesto |
| `company` | string | Empresa |
| `url` | string | Link directo de postulación |
| `location` | string | Ubicación o restricción geográfica |
| `date` | string | `YYYY-MM-DD` (más reciente primero) |
| `category` | string | `Frontend`, `Backend`, `Fullstack`, `AI / Data`, `DevOps / Cloud`, `Mobile` o `General` |
| `tags` | string[] | Hasta 5 tecnologías del vocabulario controlado |
| `salary` | string \| null | Rango salarial cuando la fuente lo publica |
| `source` | string | `RemoteOK`, `WeWorkRemotely` o `Remotive` |

---

## Cómo funciona

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
  classify.py   reglas puras: tags, categorías, filtro dev (testeable)
  fetcher.py    HTTP + parsers de las 3 fuentes + dedupe
  main.py       orquestación, guard anti-vacío, stats y README
tests/
  test_classify.py     reglas de clasificación
  test_fetcher.py      parsers con fixtures, dedupe, guard, README
  test_dependencies.py verifica que no haya imports de terceros
  fixtures/            payloads congelados de las 3 fuentes
web/
  index.html    dashboard estático (Tailwind CDN + Lucide)
data/
  jobs.json     API pública
  stats.json    agregados para el dashboard y los badges
```

## Limitaciones conocidas

- Solo el ~25% de las ofertas trae salario: depende de cada fuente.
- 4 commits automáticos al día: el histórico del repo crece. Si molesta, se puede mover la escritura a una rama `data` o squash periódico.
- Las fuentes cambian de formato sin avisar; los parsers fallan suave y el guard evita publicar datos rotos.

## Licencia

MIT — ver [LICENSE](LICENSE).

# Runbook — local development and deployment

Step-by-step commands to run the 3PL Supply Chain Visibility Platform locally and in Docker. Run from the repository root unless noted.

**Related docs:** [README](../README.md)

---

## Repository layout

| Path | Purpose |
|------|---------|
| `frontend/` | Vite React TypeScript SPA |
| `backend/app/` | FastAPI application factory, config, and domain packages (`models`, `schemas`, `routers`, `services`, `workers`) |
| `backend/requirements.txt` | Python dependencies for the API |
| `infra/migrations/` | Database migration helpers (Alembic in a later phase) |
| `infra/seed/` | Seed data scripts for local demos |
| `docker-compose.yml` | Root Compose file for API, frontend, database, and workers |
| `.env.example` | Template for root-level environment variables |

---

## Prerequisites

```bash
node -v           # v20.x or v22.x
python3 --version # 3.11+
docker --version
docker compose version
```

---

## Environment variables

Copy `.env.example` to `.env` at the repository root and adjust values for your environment.

| Variable | Purpose |
|----------|---------|
| `DATABASE_URL` | PostgreSQL connection string for the FastAPI backend |
| `POSTGRES_USER` | Database user when running PostgreSQL via Compose |
| `POSTGRES_PASSWORD` | Database password when running PostgreSQL via Compose |
| `POSTGRES_DB` | Database name when running PostgreSQL via Compose |
| `API_HOST` | Host the API binds to (`uvicorn`) |
| `API_PORT` | Port the API listens on (default `8000`) |
| `CORS_ORIGINS` | Comma-separated browser origins allowed by the API |
| `VITE_API_BASE_URL` | Base URL the frontend uses for API requests |

The backend reads `api_host`, `api_port`, and `database_url` from `.env` via `backend/app/config.py`. Additional variables are documented inline in `.env.example`.

---

## Backend (FastAPI)

From the repository root:

```bash
python3 -m venv backend/.venv
source backend/.venv/bin/activate
pip install -r backend/requirements.txt
uvicorn app.main:app --app-dir backend --reload --host "${API_HOST:-0.0.0.0}" --port "${API_PORT:-8000}"
```

- OpenAPI docs: `http://localhost:8000/api/docs`
- Health-style root: `GET http://localhost:8000/`

Versioned shipment and warehouse routes under `/api/v1/` are added in a later phase.

---

## Frontend (Vite)

In a second terminal, from `frontend/`:

```bash
cd frontend
npm install
npm run dev
```

The dev server defaults to `http://localhost:5173`. Set `VITE_API_BASE_URL` in `.env` so the SPA can reach the API once client modules are wired.

---

## Docker Compose

`docker-compose.yml` at the repository root defines the project name and an empty `services` map. PostgreSQL, backend, frontend, and worker services are added when the full stack phase lands.

Before using Compose in that phase:

```bash
cp .env.example .env
# docker compose up
```

Startup and health-check details will be documented here when those services are defined.

---

## Seed data

Seed scripts under `infra/seed/` will populate sample tenants, warehouses, shipments, and carrier events for local demos. Invocation steps will be documented here once the seed phase is complete.

---

## Portfolio demo

This project is featured in the [portfolio case study](https://github.com/qgjones9/portfolio). Demo recordings and GIFs will be linked from the portfolio project card when available.

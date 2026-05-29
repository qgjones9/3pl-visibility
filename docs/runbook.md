# Runbook — local development and deployment

Step-by-step commands to run the 3PL Supply Chain Visibility Platform locally and in Docker. Run from the repository root unless noted.

**Related docs:** [README](../README.md) · [architecture](architecture/)

---

## Prerequisites

Target versions once the application scaffold is in place:

```bash
node -v    # v20.x or v22.x
python3 --version   # 3.11+
docker --version
docker compose version
```

---

## Local development (planned)

Detailed setup steps will be added as each phase lands:

1. **Backend** — FastAPI with PostgreSQL via Docker or local install
2. **Frontend** — Vite dev server with API proxy to the backend
3. **Full stack** — `docker compose up` for API, frontend, database, and workers

---

## Environment variables

Copy `.env.example` to `.env` and fill in values when available:

| Variable | Purpose |
|----------|---------|
| `DATABASE_URL` | PostgreSQL connection string |
| `API_HOST` / `API_PORT` | FastAPI bind address |
| `VITE_API_BASE_URL` | Frontend API base URL |

---

## Seed data

Seed scripts under `backend/seed/` will populate sample tenants, warehouses, shipments, and carrier events for local demos. Invocation steps will be documented here once the seed phase is complete.

---

## Portfolio demo

This project is featured in the [portfolio case study](https://github.com/qgjones9/portfolio). Demo recordings and GIFs will be linked from the portfolio project card when available.

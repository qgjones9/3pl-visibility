# 3PL Supply Chain Visibility Platform

Real-time shipment and inventory visibility for third-party logistics operators. A B2B dashboard and API layer that unifies warehouse, transportation, and carrier data into a single timeline per shipment.

## Problem

3PL operators manage orders across warehouse management systems, transportation platforms, and carrier portals. Exception handling slows down when teams must reconcile three separate event streams for one shipment. This platform consolidates those sources into one operational view.

## Stack

| Layer | Technology |
|-------|------------|
| Frontend | React 19, TypeScript, Vite |
| Backend | FastAPI, Pydantic, SQLAlchemy (planned) |
| Database | PostgreSQL |
| Infrastructure | Docker Compose |

## Architecture

```
React SPA  →  FastAPI services  →  PostgreSQL (system of record)
                    ↓
            Async workers (carrier ingestion)
```

The frontend provides shipment dashboards, inventory panels, and unified event timelines. FastAPI services expose versioned REST endpoints. PostgreSQL stores tenants, shipments, warehouses, and carrier events. Background workers ingest webhook and batch carrier data.

## Repository layout

| Path | Purpose |
|------|---------|
| `frontend/` | React + Vite SPA (`src/components`, `src/views`, `src/api`, `src/types`) |
| `backend/` | FastAPI package with app factory, config, and domain package stubs |
| `infra/` | Migration and seed placeholders for database and demo data |
| `docker-compose.yml` | Root Compose file for the local stack (service definitions in a later phase) |
| `.env.example` | Documented variables for the API, database, and frontend |
| `docs/` | Runbook and architecture documentation |

## Getting started

```bash
git clone https://github.com/qgjones9/3pl-visibility.git
cd 3pl-visibility
cp .env.example .env
```

Run the API and SPA from the repository root using the commands in the [runbook](docs/runbook.md). Copy `.env.example` to `.env` and adjust values for your environment before starting services.

## Documentation

- [Runbook](docs/runbook.md) — prerequisites, local development, environment variables, and Docker Compose

## License

Private repository. All rights reserved.

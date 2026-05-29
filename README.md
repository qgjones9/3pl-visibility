# 3PL Supply Chain Visibility Platform

Real-time shipment and inventory visibility for third-party logistics operators. A B2B dashboard and API layer that unifies warehouse, transportation, and carrier data into a single timeline per shipment.

## Problem

3PL operators manage orders across warehouse management systems, transportation platforms, and carrier portals. Exception handling slows down when teams must reconcile three separate event streams for one shipment. This platform consolidates those sources into one operational view.

## Stack

| Layer | Technology |
|-------|------------|
| Frontend | React, TypeScript, Tailwind CSS |
| Backend | FastAPI, Pydantic, SQLAlchemy |
| Database | PostgreSQL |
| Infrastructure | Docker Compose |

## Architecture

```
React SPA  →  FastAPI services  →  PostgreSQL (system of record)
                    ↓
            Async workers (carrier ingestion)
```

The frontend provides shipment dashboards, inventory panels, and unified event timelines. FastAPI services expose versioned REST endpoints. PostgreSQL stores tenants, shipments, warehouses, and carrier events. Background workers ingest webhook and batch carrier data.

## Documentation

- [Runbook](docs/runbook.md) — prerequisites, local development, and deployment
- [Architecture](docs/architecture/) — system design and component overview

## Clone

```bash
git clone https://github.com/qgjones9/3pl-visibility.git
cd 3pl-visibility
```

See the [runbook](docs/runbook.md) for setup instructions once the application scaffold is in place.

## License

Private repository. All rights reserved.

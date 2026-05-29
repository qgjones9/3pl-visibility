"""Carrier event ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy import DateTime, Enum, ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin
from app.models.enums import EventSource

if TYPE_CHECKING:
    from app.models.shipment import Shipment
    from app.models.tenant import Tenant


class CarrierEvent(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Timeline entry from WMS, TMS, or carrier webhook ingestion."""

    __tablename__ = "carrier_events"
    __table_args__ = (
        Index(
            "ix_carrier_events_shipment_occurred",
            "shipment_id",
            "occurred_at",
        ),
    )

    tenant_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tenants.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    shipment_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("shipments.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    source: Mapped[EventSource] = mapped_column(
        Enum(
            EventSource,
            name="event_source",
            native_enum=False,
            length=16,
        ),
        nullable=False,
    )
    event_type: Mapped[str] = mapped_column(String(64), nullable=False)
    occurred_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    description: Mapped[str | None] = mapped_column(Text)
    location: Mapped[str | None] = mapped_column(String(255))
    raw_payload: Mapped[dict[str, Any] | None] = mapped_column(JSONB)

    tenant: Mapped[Tenant] = relationship()
    shipment: Mapped[Shipment] = relationship(
        back_populates="carrier_events",
    )

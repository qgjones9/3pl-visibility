"""Shipment ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, Index, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin
from app.models.enums import ShipmentStatus

if TYPE_CHECKING:
    from app.models.carrier_event import CarrierEvent
    from app.models.tenant import Tenant
    from app.models.warehouse import Warehouse


class Shipment(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Order or load tracked across WMS, TMS, and carrier systems."""

    __tablename__ = "shipments"
    __table_args__ = (
        UniqueConstraint(
            "tenant_id",
            "reference_number",
            name="uq_shipments_tenant_reference",
        ),
        Index("ix_shipments_tenant_status", "tenant_id", "status"),
    )

    tenant_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tenants.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    warehouse_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("warehouses.id", ondelete="RESTRICT"),
        index=True,
        nullable=False,
    )
    reference_number: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    tracking_number: Mapped[str | None] = mapped_column(
        String(128),
        index=True,
    )
    carrier_name: Mapped[str | None] = mapped_column(String(128))
    status: Mapped[ShipmentStatus] = mapped_column(
        Enum(
            ShipmentStatus,
            name="shipment_status",
            native_enum=False,
            length=32,
        ),
        default=ShipmentStatus.PENDING,
        nullable=False,
    )
    destination_city: Mapped[str | None] = mapped_column(String(128))
    destination_region: Mapped[str | None] = mapped_column(String(64))
    destination_country_code: Mapped[str | None] = mapped_column(
        String(2),
    )
    shipped_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )
    delivered_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    tenant: Mapped[Tenant] = relationship(back_populates="shipments")
    warehouse: Mapped[Warehouse] = relationship(back_populates="shipments")
    carrier_events: Mapped[list[CarrierEvent]] = relationship(
        back_populates="shipment",
        cascade="all, delete-orphan",
        order_by="CarrierEvent.occurred_at",
    )

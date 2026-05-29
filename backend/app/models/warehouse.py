"""Warehouse ORM model."""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.shipment import Shipment
    from app.models.tenant import Tenant


class Warehouse(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Fulfillment or storage site owned by a tenant."""

    __tablename__ = "warehouses"
    __table_args__ = (
        UniqueConstraint(
            "tenant_id",
            "code",
            name="uq_warehouses_tenant_code",
        ),
    )

    tenant_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tenants.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    code: Mapped[str] = mapped_column(String(32), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str | None] = mapped_column(String(128))
    region: Mapped[str | None] = mapped_column(String(64))
    country_code: Mapped[str | None] = mapped_column(String(2))
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    tenant: Mapped[Tenant] = relationship(back_populates="warehouses")
    shipments: Mapped[list[Shipment]] = relationship(
        back_populates="warehouse",
    )

"""Tenant ORM model."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.shipment import Shipment
    from app.models.warehouse import Warehouse


class Tenant(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """3PL operator or customer org for multi-tenant isolation."""

    __tablename__ = "tenants"

    slug: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        index=True,
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    warehouses: Mapped[list[Warehouse]] = relationship(
        back_populates="tenant",
        cascade="all, delete-orphan",
    )
    shipments: Mapped[list[Shipment]] = relationship(
        back_populates="tenant",
        cascade="all, delete-orphan",
    )

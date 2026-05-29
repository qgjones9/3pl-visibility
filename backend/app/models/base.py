"""Declarative base and shared model mixins."""

from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """ORM declarative base for Alembic metadata."""


class UUIDPrimaryKeyMixin:
    """UUID primary key defaulting to uuid4."""

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )


class TimestampMixin:
    """Created/updated timestamps with timezone-aware columns."""

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

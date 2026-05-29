"""Domain enumerations for ORM columns."""

import enum


class ShipmentStatus(str, enum.Enum):
    """Lifecycle status for a shipment."""

    PENDING = "pending"
    PROCESSING = "processing"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    EXCEPTION = "exception"
    CANCELLED = "cancelled"


class EventSource(str, enum.Enum):
    """System that produced a timeline event."""

    WMS = "wms"
    TMS = "tms"
    CARRIER = "carrier"

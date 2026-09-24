from datetime import datetime

from pydantic import BaseModel, ConfigDict


class IncidentCreate(BaseModel):
    title: str
    description: str
    category: str = "OTHER"
    priority: str = "MEDIUM"


class IncidentUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    category: str | None = None
    priority: str | None = None
    status: str | None = None
    assigned_to: int | None = None


class IncidentResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    priority: str
    status: str
    created_by: int
    assigned_to: int | None
    created_at: datetime
    updated_at: datetime
    resolved_at: datetime | None

    model_config = ConfigDict(from_attributes=True)  
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.incident import Incident
from app.schemas.incident import (
    IncidentCreate,
    IncidentResponse,
    IncidentUpdate,
)


router = APIRouter(
    prefix="/api/incidents",
    tags=["Incidents"]
)

@router.post(
    "/",
    response_model=IncidentResponse
)
def create_incident(
    incident: IncidentCreate,
    db: Session = Depends(get_db)
):
    new_incident = Incident(
        title=incident.title,
        description=incident.description,
        category=incident.category,
        priority=incident.priority,
        created_by=1
    )

    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)

    return new_incident

@router.get(
    "/",
    response_model=list[IncidentResponse]
)
def get_incidents(
    db: Session = Depends(get_db)
):
    return db.query(Incident).all()

@router.get(
    "/{incident_id}",
    response_model=IncidentResponse
)
def get_incident(
    incident_id: int,
    db: Session = Depends(get_db)
):
    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return incident



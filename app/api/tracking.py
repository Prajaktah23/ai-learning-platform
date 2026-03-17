from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.foundation.tracking_service import get_dashboard_data
from app.db.session import get_db
from app.services.foundation.tracking_service import complete_subtopic

router = APIRouter()

@router.get("/dashboard/{email}")
def get_dashboard(email: str, db: Session = Depends(get_db)):
    return get_dashboard_data(db, email)

@router.put("/subtopic/{subtopic_id}/complete")
def mark_subtopic_complete(subtopic_id: int, db: Session = Depends(get_db)):

    subtopic = complete_subtopic(db, subtopic_id)

    if not subtopic:
        raise HTTPException(status_code=404, detail="Subtopic not found")

    return {
        "message": "Subtopic completed",
        "subtopic_id": subtopic.id,
        "status": subtopic.status
    }
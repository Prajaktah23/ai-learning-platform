from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
import json
from app.db.session import get_db
from app.llm.learning_path_prompt import LEARNING_PATH_PROMPT
from app.llm.llm_provider import generate_text
from app.services.foundation.tracking_service import create_learning_path
from datetime import date


router = APIRouter()

@router.post("/generate-learning-path")
def generate_learning_path(
    # user_id: int = Query(..., description="User ID"),
    email: str = Query(..., description="User Email"),
    goal: str = Query(..., description="Skill to learn e.g. Python"),
    level: str = Query(..., description="Beginner | Intermediate | Advanced"),
    duration_weeks: int = Query(..., description="Number of weeks"),
    start_date: date = Query(..., description="Start date e.g. 2026-03-11"),
    db: Session = Depends(get_db)
):
    prompt = LEARNING_PATH_PROMPT.format(
        goal=goal,
        level=level,
        duration_weeks=duration_weeks
    )

    raw = generate_text(prompt)        # ← this is a string

    import re

    match = re.search(r"\{.*\}", raw, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in LLM response")

    json_str = match.group(0)

    data = json.loads(json_str)

    learning_path = create_learning_path(
        db=db,
        email=email,
        start_date=start_date,
        llm_data=data
    )

    return {
        "message": "Learning path generated successfully",
    }

from pydantic import BaseModel
from typing import List
from .topic_schema import TopicResponse
from datetime import date

class LearningPathGenerateRequest(BaseModel):
    email: str
    goal: str
    level: str
    duration_weeks: int
    start_date: date


class LearningPathResponse(BaseModel):
    id: int
    title: str
    topics: List[TopicResponse]
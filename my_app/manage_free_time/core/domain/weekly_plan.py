from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class WeeklyPlan(BaseModel):
    user_id: int
    week_start_date: str
    week_end_date: str
    ideas_ids: List[int]  # Lista ID pomysłów wybranych na ten tydzień

class WeeklyPlanIn(BaseModel):
    week_start_date: str
    week_end_date: str
    ideas_ids: List[int]
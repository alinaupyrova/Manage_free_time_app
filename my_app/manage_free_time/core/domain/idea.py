from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class IdeaIn(BaseModel):

    title: str
    category: str
    tags: List[str]


class Idea(IdeaIn):

    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True, extra="ignore")



from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class UserProfileIn(BaseModel):

    username: str
    bio: Optional[str]


class UserProfile(UserProfileIn):
    id: int
    idea_ids: List[int]

    model_config = ConfigDict(from_attributes=True, extra="ignore")



from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class InvitationIn(BaseModel):
    inviter_id: int
    invitee_email: str
    message: Optional[str] = None


class Invitation(InvitationIn):
    id: int
    model_config = ConfigDict(from_attributes=True, extra="ignore")

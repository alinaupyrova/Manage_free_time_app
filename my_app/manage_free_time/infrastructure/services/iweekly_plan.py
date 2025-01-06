from abc import ABC, abstractmethod
from typing import Iterable

from manage_free_time.core.domain.weekly_plan import WeeklyPlan, WeeklyPlanIn


class IWeeklyPlanService(ABC):
    """A class representing weekly plan-related operations."""

    @abstractmethod
    async def get_by_user(self, user_id: int) -> Iterable[WeeklyPlan]:
        """Fetch all weekly plans for a user."""

    @abstractmethod
    async def create_weekly_plan(self, user_id: int, idea_ids: list) -> WeeklyPlan:
        """Create a new weekly plan for the user."""

    @abstractmethod
    async def update_weekly_plan(self, plan_id: int, data: WeeklyPlanIn) -> WeeklyPlan | None:
        """Update the details of a weekly plan."""

    @abstractmethod
    async def delete_weekly_plan(self, plan_id: int) -> bool:
        """Delete a specific weekly plan."""

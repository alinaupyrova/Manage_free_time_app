from typing import Iterable, Optional
from manage_free_time.core.domain.weekly_plan import WeeklyPlan, WeeklyPlanIn
from manage_free_time.core.repositories.iweekly_plan import IWeeklyPlanRepository
from manage_free_time.infrastructure.services.iweekly_plan import IWeeklyPlanService


class WeeklyPlanService(IWeeklyPlanService):
    """A class implementing the weekly plan service."""

    _repository: IWeeklyPlanRepository

    def __init__(self, repository: IWeeklyPlanRepository) -> None:
        """The initializer of the `WeeklyPlanService`.

        Args:
            repository (IWeeklyPlanRepository): The reference to the repository.
        """
        self._repository = repository

    async def create_plan(self, data: WeeklyPlanIn) -> WeeklyPlan:
        """The method creating a weekly plan.

        Args:
            data (WeeklyPlanIn): Details of the new weekly plan.

        Returns:
            WeeklyPlan: The created weekly plan.
        """
        return await self._repository.create_plan(data)

    async def get_plan_by_user(self, user_id: int) -> Optional[WeeklyPlan]:
        """The method getting a weekly plan for a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Optional[WeeklyPlan]: The user's weekly plan.
        """
        return await self._repository.get_plan_by_user(user_id)

    async def update_plan(self, plan_id: int, data: WeeklyPlanIn) -> Optional[WeeklyPlan]:
        """The method updating a weekly plan.

        Args:
            plan_id (int): The ID of the weekly plan to update.
            data (WeeklyPlanIn): The updated plan data.

        Returns:
            Optional[WeeklyPlan]: The updated plan or None if not found.
        """
        return await self._repository.update_plan(plan_id=plan_id, data=data)

    async def delete_plan(self, plan_id: int) -> bool:
        """The method deleting a weekly plan.

        Args:
            plan_id (int): The ID of the weekly plan to delete.

        Returns:
            bool: Success of the operation.
        """
        return await self._repository.delete_plan(plan_id)

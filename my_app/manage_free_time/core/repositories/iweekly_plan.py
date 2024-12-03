from abc import ABC, abstractmethod
from typing import Optional, Iterable
from manage_free_time.core.domain.weekly_plan import WeeklyPlan, WeeklyPlanIn

class IWeeklyPlanRepository(ABC):
    """Abstrakcyjna klasa reprezentująca repozytorium planów na tydzień."""

    @abstractmethod
    async def get_plan_by_user(self, user_id: int) -> Optional[WeeklyPlan]:
        """Pobiera plan na tydzień dla danego użytkownika."""
        pass

    @abstractmethod
    async def create_weekly_plan(self, user_id: int, data: WeeklyPlanIn) -> WeeklyPlan:
        """Tworzy nowy plan rozrywki na tydzień dla użytkownika."""
        pass

    @abstractmethod
    async def update_weekly_plan(
        self, user_id: int, data: WeeklyPlanIn
    ) -> Optional[WeeklyPlan]:
        """Aktualizuje plan rozrywki na tydzień dla użytkownika."""
        pass

    @abstractmethod
    async def delete_weekly_plan(self, user_id: int) -> bool:
        """Usuwa plan rozrywki na tydzień dla użytkownika."""
        pass

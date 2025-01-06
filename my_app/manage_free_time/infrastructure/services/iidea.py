from abc import ABC, abstractmethod
from typing import Iterable

from manage_free_time.core.domain.idea import Idea, IdeaIn


class IIdeaService(ABC):
    """A class representing idea-related operations."""

    @abstractmethod
    async def get_all(self) -> Iterable[Idea]:
        """Fetch all ideas."""

    @abstractmethod
    async def get_random(self, category: str = None, tags: list = None) -> Idea:
        """Get a random idea, optionally filtered by category and tags."""

    @abstractmethod
    async def get_by_id(self, idea_id: int) -> Idea | None:
        """Fetch an idea by its ID."""

    @abstractmethod
    async def get_by_user(self, user_id: int) -> Iterable[Idea]:
        """Fetch all ideas created by a specific user."""

    async def add_idea(self, data: IdeaIn) -> Idea:
        """Add a new idea to the system."""

    @abstractmethod
    async def update_idea(self, idea_id: int, data: IdeaIn) -> Idea | None:
        """Update the details of an existing idea."""

    @abstractmethod
    async def delete_idea(self, idea_id: int) -> bool:
        """Remove an idea from the system."""

from typing import Iterable, Optional
from manage_free_time.core.domain.idea import Idea, IdeaIn
from manage_free_time.core.repositories.iidea import IIdeaRepository
from manage_free_time.infrastructure.services.idea import IIdeaService


class IdeaService(IIdeaService):
    """A class implementing the idea service."""

    _repository: IIdeaRepository

    def __init__(self, repository: IIdeaRepository) -> None:
        """The initializer of the `IdeaService`.

        Args:
            repository (IIdeaRepository): The reference to the repository.
        """
        self._repository = repository

    async def get_random_idea(self, category: Optional[str] = None) -> Optional[Idea]:
        """The method getting a random idea.

        Args:
            category (Optional[str]): The category of the idea (optional).

        Returns:
            Optional[Idea]: A random idea or None if no idea found.
        """
        return await self._repository.get_random_idea(category=category)

    async def get_all_ideas(self) -> Iterable[Idea]:
        """The method getting all ideas.

        Returns:
            Iterable[Idea]: Collection of all ideas.
        """
        return await self._repository.get_all_ideas()

    async def get_ideas_by_category(self, category: str) -> Iterable[Idea]:
        """The method getting ideas filtered by category.

        Args:
            category (str): The category name.

        Returns:
            Iterable[Idea]: Collection of ideas for the category.
        """
        return await self._repository.get_ideas_by_category(category)

    async def add_idea(self, data: IdeaIn) -> Idea:
        """The method adding a new idea.

        Args:
            data (IdeaIn): Details of the new idea.

        Returns:
            Idea: The newly added idea.
        """
        return await self._repository.add_idea(data)

    async def update_idea(self, idea_id: int, data: IdeaIn) -> Optional[Idea]:
        """The method updating an existing idea.

        Args:
            idea_id (int): The ID of the idea to update.
            data (IdeaIn): The updated idea data.

        Returns:
            Optional[Idea]: The updated idea or None if not found.
        """
        return await self._repository.update_idea(idea_id=idea_id, data=data)

    async def delete_idea(self, idea_id: int) -> bool:
        """The method deleting an idea.

        Args:
            idea_id (int): The ID of the idea to delete.

        Returns:
            bool: Success of the operation.
        """
        return await self._repository.delete_idea(idea_id)

    async def get_ideas_by_user(self, user_id: int) -> Iterable[Idea]:
        """The method fetching ideas created by a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Iterable[Idea]: Collection of ideas created by the user.
        """
        return await self._repository.get_ideas_by_user(user_id)

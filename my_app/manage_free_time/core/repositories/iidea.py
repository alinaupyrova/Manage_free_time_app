from abc import ABC, abstractmethod
from typing import Iterable
from manage_free_time.core.domain.idea import Idea, IdeaIn
from manage_free_time.core.domain.user_profile import UserProfile, UserProfileIn


class IIdeaRepository(ABC):
    """An abstract class representing protocol of idea repository."""

    @abstractmethod
    async def get_all_ideas(self) -> Iterable[Idea]:
        """Retrieve all ideas from the data storage.

        Returns:
            Iterable[Idea]: Collection of ideas in the data storage.
        """

    @abstractmethod
    async def get_by_category(self, category: str) -> Iterable[Idea]:
        """Retrieve ideas filtered by category.

        Args:
            category (str): The category to filter by.

        Returns:
            Iterable[Idea]: Collection of ideas in the given category.
        """

    @abstractmethod
    async def get_by_tags(self, tags: list[str]) -> Iterable[Idea]:
        """Retrieve ideas filtered by tags.

        Args:
            tags (list[str]): List of tags to filter by.

        Returns:
            Iterable[Idea]: Collection of ideas matching the given tags.
        """

    @abstractmethod
    async def get_by_user(self, user_id: int) -> Iterable[Idea]:
        """Retrieve ideas created by a specific user.

        Args:
            user_id (int): The id of the user.

        Returns:
            Iterable[Idea]: Collection of user's ideas.
        """

    @abstractmethod
    async def get_by_id(self, idea_id: int) -> Idea | None:
        """Retrieve an idea by its id.

        Args:
            idea_id (int): The id of the idea.

        Returns:
            Idea | None: The details of the idea, or None if not found.
        """

    @abstractmethod
    async def add_idea(self, data: IdeaIn, user_id: int) -> None:
        """Add a new idea to the data storage.

        Args:
            data (IdeaIn): The details of the new idea.
            user_id (int): The id of the user adding the idea.
        """

    @abstractmethod
    async def update_idea(self, idea_id: int, data: IdeaIn) -> Idea | None:
        """Update an existing idea in the data storage.

        Args:
            idea_id (int): The id of the idea.
            data (IdeaIn): The updated details of the idea.

        Returns:
            Idea | None: The updated idea details, or None if not found.
        """

    @abstractmethod
    async def delete_idea(self, idea_id: int) -> bool:
        """Remove an idea from the data storage.

        Args:
            idea_id (int): The id of the idea.

        Returns:
            bool: Success of the operation.
        """


class IUserRepository(ABC):
    """An abstract class representing protocol of user repository."""

    @abstractmethod
    async def get_all_users(self) -> Iterable[UserProfile]:
        """Retrieve all user profiles from the data storage.

        Returns:
            Iterable[UserProfile]: Collection of user profiles.
        """

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> UserProfile | None:
        """Retrieve a user profile by id.

        Args:
            user_id (int): The id of the user.

        Returns:
            UserProfile | None: The user profile details, or None if not found.
        """

    @abstractmethod
    async def add_user(self, data: UserProfileIn) -> None:
        """Add a new user profile to the data storage.

        Args:
            data (UserProfileIn): The details of the new user profile.
        """

    @abstractmethod
    async def update_user(
        self, user_id: int, data: UserProfileIn
    ) -> UserProfile | None:
        """Update an existing user profile in the data storage.

        Args:
            user_id (int): The id of the user.
            data (UserProfileIn): The updated user profile details.

        Returns:
            UserProfile | None: The updated profile, or None if not found.
        """

    @abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        """Remove a user profile from the data storage.

        Args:
            user_id (int): The id of the user.

        Returns:
        bool: Success of the operation.
                """
from abc import ABC, abstractmethod
from typing import Iterable

from manage_free_time.core.domain.user_profile import UserProfile, UserProfileIn


class IUserProfileService(ABC):
    """A class representing user profile-related operations."""

    @abstractmethod
    async def get_by_id(self, user_id: int) -> UserProfile | None:
        """Fetch user profile by ID."""

    @abstractmethod
    async def get_by_username(self, username: str) -> UserProfile | None:
        """Fetch user profile by username."""

    @abstractmethod
    async def get_all(self) -> Iterable[UserProfile]:
        """Fetch all user profiles."""

    async def create_profile(self, data: UserProfileIn) -> UserProfile:
        """Create a new user profile."""

    @abstractmethod
    async def update_profile(self, user_id: int, data: UserProfileIn) -> UserProfile | None:
        """Update a user profile."""

    @abstractmethod
    async def delete_profile(self, user_id: int) -> bool:
        """Delete a user profile."""

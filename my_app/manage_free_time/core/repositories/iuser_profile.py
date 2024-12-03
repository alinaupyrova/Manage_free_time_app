"""Module containing user profile repository abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable, Optional
from manage_free_time.core.domain.user_profile import UserProfile, UserProfileIn


class IUserProfileRepository(ABC):
    """An abstract class representing protocol of user profile repository."""

    @abstractmethod
    async def get_all_profiles(self) -> Iterable[UserProfile]:
        """The abstract getting all user profiles from the data storage.

        Returns:
            Iterable[UserProfile]: User profiles in the data storage.
        """

    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[UserProfile]:
        """The abstract getting user profile by provided id.

        Args:
            user_id (int): The id of the user.

        Returns:
            Optional[UserProfile]: The user profile details or None if not found.
        """

    @abstractmethod
    async def get_by_username(self, username: str) -> Optional[UserProfile]:
        """The abstract getting user profile by provided username.

        Args:
            username (str): The username of the user.

        Returns:
            Optional[UserProfile]: The user profile details or None if not found.
        """

    @abstractmethod
    async def get_user_ideas(self, user_id: int) -> Iterable[int]:
        """The abstract getting ideas associated with a particular user.

        Args:
            user_id (int): The id of the user.

        Returns:
            Iterable[int]: List of idea IDs associated with the user.
        """

    @abstractmethod
    async def add_user_profile(self, data: UserProfileIn) -> UserProfile:
        """The abstract adding a new user profile to the data storage.

        Args:
            data (UserProfileIn): The details of the new user profile.

        Returns:
            UserProfile: The created user profile.
        """

    @abstractmethod
    async def update_user_profile(
        self, user_id: int, data: UserProfileIn
    ) -> Optional[UserProfile]:
        """The abstract updating user profile in the data storage.

        Args:
            user_id (int): The id of the user.
            data (UserProfileIn): The details of the updated user profile.

        Returns:
            Optional[UserProfile]: The updated user profile or None if not found.
        """

    @abstractmethod
    async def delete_user_profile(self, user_id: int) -> bool:
        """The abstract removing user profile from the data storage.

        Args:
            user_id (int): The id of the user.

        Returns:
            bool: Success of the operation.
        """

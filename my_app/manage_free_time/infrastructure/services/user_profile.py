from typing import Iterable, Optional
from manage_free_time.core.domain.user_profile import UserProfile, UserProfileIn
from manage_free_time.core.repositories.iuser_profile import IUserProfileRepository
from manage_free_time.infrastructure.services.iuser_profile import IUserProfileService


class UserProfileService(IUserProfileService):
    """A class implementing the user profile service."""

    _repository: IUserProfileRepository

    def __init__(self, repository: IUserProfileRepository) -> None:
        """The initializer of the `UserProfileService`.

        Args:
            repository (IUserProfileRepository): The reference to the repository.
        """
        self._repository = repository

    async def create_profile(self, data: UserProfileIn) -> UserProfile:
        """The method creating a user profile.

        Args:
            data (UserProfileIn): The details of the user profile.

        Returns:
            UserProfile: The created user profile.
        """
        return await self._repository.create_profile(data)

    async def get_profile_by_id(self, user_id: int) -> Optional[UserProfile]:
        """The method getting a user profile by ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Optional[UserProfile]: The user profile or None if not found.
        """
        return await self._repository.get_profile_by_id(user_id)

    async def update_profile(self, user_id: int, data: UserProfileIn) -> Optional[UserProfile]:
        """The method updating a user profile.

        Args:
            user_id (int): The ID of the user profile.
            data (UserProfileIn): The updated user profile data.

        Returns:
            Optional[UserProfile]: The updated profile or None if not found.
        """
        return await self._repository.update_profile(user_id=user_id, data=data)

    async def delete_profile(self, user_id: int) -> bool:
        """The method deleting a user profile.

        Args:
            user_id (int): The ID of the user profile.

        Returns:
            bool: Success of the operation.
        """
        return await self._repository.delete_profile(user_id)

    async def get_all_profiles(self) -> Iterable[UserProfile]:
        """The method retrieving all user profiles.

        Returns:
            Iterable[UserProfile]: Collection of all user profiles.
        """
        return await self._repository.get_all_profiles()

    async def follow_user(self, follower_id: int, followee_id: int) -> bool:
        """The method allowing a user to follow another user.

        Args:
            follower_id (int): The ID of the follower.
            followee_id (int): The ID of the user to follow.

        Returns:
            bool: Success of the operation.
        """
        return await self._repository.follow_user(follower_id, followee_id)

    async def unfollow_user(self, follower_id: int, followee_id: int) -> bool:
        """The method allowing a user to unfollow another user.

        Args:
            follower_id (int): The ID of the follower.
            followee_id (int): The ID of the user to unfollow.

        Returns:
            bool: Success of the operation.
        """
        return await self._repository.unfollow_user(follower_id, followee_id)

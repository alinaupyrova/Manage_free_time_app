from abc import ABC, abstractmethod
from typing import Iterable

from manage_free_time.core.domain.invitations import Invitation, InvitationIn


class IInvitationRepository(ABC):
    """An abstract class representing the protocol for an invitation repository."""

    @abstractmethod
    async def get_all_invitations(self) -> Iterable[Invitation]:
        """Get all invitations from the data storage.

        Returns:
            Iterable[Invitation]: A collection of all invitations.
        """

    @abstractmethod
    async def get_by_user(self, user_id: int) -> Iterable[Invitation]:
        """Get all invitations sent by a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Iterable[Invitation]: A collection of invitations sent by the given user.
        """

    @abstractmethod
    async def get_by_event(self, event_id: int) -> Iterable[Invitation]:
        """Get all invitations for a specific event.

        Args:
            event_id (int): The ID of the event.

        Returns:
            Iterable[Invitation]: A collection of invitations for the specified event.
        """

    @abstractmethod
    async def get_by_status(self, status: str) -> Iterable[Invitation]:
        """Get all invitations by status.

        Args:
            status (str): The status of the invitation (e.g., 'pending', 'accepted', 'declined').

        Returns:
            Iterable[Invitation]: A collection of invitations with the given status.
        """

    @abstractmethod
    async def get_by_id(self, invitation_id: int) -> Invitation | None:
        """Get the details of an invitation by its ID.

        Args:
            invitation_id (int): The ID of the invitation.

        Returns:
            Invitation | None: The invitation details or None if not found.
        """

    @abstractmethod
    async def send_invitation(self, data: InvitationIn) -> None:
        """Send a new invitation.

        Args:
            data (InvitationIn): The details of the new invitation.
        """

    @abstractmethod
    async def update_invitation_status(
        self, invitation_id: int, status: str
    ) -> Invitation | None:
        """Update the status of an invitation.

        Args:
            invitation_id (int): The ID of the invitation.
            status (str): The new status of the invitation.

        Returns:
            Invitation | None: The updated invitation details.
        """

    @abstractmethod
    async def delete_invitation(self, invitation_id: int) -> bool:
        """Delete an invitation.

        Args:
            invitation_id (int): The ID of the invitation.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """

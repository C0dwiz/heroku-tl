from enum import Enum
from typing import Optional


class MessageServiceType(Enum):
    """
    Enumeration for different types of service messages.
    """
    # Existing types (these should match the ones already in Telethon)
    CONTACT_REGISTERED = "contact_registered"
    PHONE_CALL_REQUESTED = "phone_call_requested"
    PHONE_CALL_ACCEPTED = "phone_call_accepted"
    PHONE_CALL_DISCARDED = "phone_call_discarded"
    PHONE_CALL_MISSED = "phone_call_missed"
    CONTACT_JOINED = "contact_joined"
    HISTORY_CLEARED = "history_cleared"
    GAME_SCORE = "game_score"
    PAYMENT_SENT = "payment_sent"
    PAYMENT_RECEIVED = "payment_received"
    PINNED_MESSAGE = "pinned_message"
    GAME_SCORE_IN_CHAT = "game_score_in_chat"
    ScreenshotTaken = "screenshot_taken"
    CHANNEL_CREATED = "channel_created"
    CHANNEL_MIGRATED_FROM = "channel_migrated_from"
    CHANNEL_MIGRATED_TO = "channel_migrated_to"
    MESSAGE_EDITED = "message_edited"
    MESSAGE_DELETED = "message_deleted"
    GROUP_CALL_STARTED = "group_call_started"
    GROUP_call_ended = "group_call_ended"
    INVITE_TO_GROUP_CALL = "invite_to_group_call"
    SET_CHAT_TTL = "set_chat_ttl"
    GROUP_CALL_SETTINGS_CHANGED = "group_call_settings_changed"
    GROUP_CALL_JUST_STARTED = "group_call_just_started"
    WEB_APP_DATA = "web_app_data"
    
    # New Layer 224 types
    STAR_GIFT = "star_gift"
    STAR_GIFT_UNIQUE = "star_gift_unique"
    NEW_CREATOR_PENDING = "new_creator_pending"
    CHANGE_CREATOR = "change_creator"

    @classmethod
    def from_action(cls, action) -> Optional['MessageServiceType']:
        """
        Convert a MessageAction to MessageServiceType.
        
        Args:
            action: The MessageAction object to convert
            
        Returns:
            MessageServiceType or None if not a service action
        """
        from .. import types
        
        if isinstance(action, types.MessageActionStarGift):
            return cls.STAR_GIFT
        elif isinstance(action, types.MessageActionStarGiftUnique):
            return cls.STAR_GIFT_UNIQUE
        elif isinstance(action, types.MessageActionNewCreatorPending):
            return cls.NEW_CREATOR_PENDING
        elif isinstance(action, types.MessageActionChangeCreator):
            return cls.CHANGE_CREATOR
        # Add existing mappings as needed
        # This would need to be expanded with all existing message actions
        
        return None

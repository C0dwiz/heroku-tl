from typing import Optional
from .. import TLObject, types


class KeyboardButtonStyle(TLObject):
    """
    Style configuration for keyboard buttons.

    Parameters:
        bg_primary (bool, optional):
            Use primary background color for the button.

        bg_danger (bool, optional):
            Use danger/red background color for the button.

        bg_success (bool, optional):
            Use success/green background color for the button.

        icon (int, optional):
            Custom emoji ID to use as button icon.
    """

    def __init__(
        self,
        *,
        bg_primary: Optional[bool] = None,
        bg_danger: Optional[bool] = None,
        bg_success: Optional[bool] = None,
        icon: Optional[int] = None
    ):
        super().__init__()
        self.bg_primary = bg_primary
        self.bg_danger = bg_danger
        self.bg_success = bg_success
        self.icon = icon

    @staticmethod
    def _parse(style: 'types.TypeKeyboardButtonStyle') -> 'KeyboardButtonStyle':
        if style is None:
            return None

        return KeyboardButtonStyle(
            bg_primary=getattr(style, 'bg_primary', None),
            bg_danger=getattr(style, 'bg_danger', None),
            bg_success=getattr(style, 'bg_success', None),
            icon=getattr(style, 'icon', None)
        )

    def to_dict(self):
        return {
            '_': 'KeyboardButtonStyle',
            'bg_primary': self.bg_primary,
            'bg_danger': self.bg_danger,
            'bg_success': self.bg_success,
            'icon': self.icon
        }

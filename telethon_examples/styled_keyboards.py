"""
Example demonstrating styled keyboard buttons (Layer 224 feature).

This example shows how to use the new KeyboardButtonStyle to create
buttons with different background colors and icons.
"""
import asyncio
from herokutl import TelegramClient, Button, KeyboardButtonStyle


async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()
    
    # Create styled buttons with different background colors
    primary_style = KeyboardButtonStyle(bg_primary=True)
    danger_style = KeyboardButtonStyle(bg_danger=True)
    success_style = KeyboardButtonStyle(bg_success=True)
    
    # Create styled buttons with custom icons (using emoji IDs)
    icon_style = KeyboardButtonStyle(icon=12345)
    
    # Example 1: Inline keyboard with styled buttons
    inline_buttons = [
        [
            Button.inline("Primary Button", "primary_data", style=primary_style),
            Button.inline("Danger Button", "danger_data", style=danger_style)
        ],
        [
            Button.inline("Success Button", "success_data", style=success_style),
            Button.inline("Icon Button", "icon_data", style=icon_style)
        ]
    ]
    
    await client.send_file(
        'me',
        file='https://example.com/image.jpg',  # Replace with actual image
        caption='Styled inline keyboard example:',
        buttons=inline_buttons
    )
    
    # Example 2: Reply keyboard with styled buttons
    reply_buttons = [
        [
            Button.text("Primary Text", style=primary_style),
            Button.text("Danger Text", style=danger_style)
        ],
        [
            Button.request_location("Send Location", style=success_style),
            Button.request_phone("Send Phone", style=icon_style)
        ]
    ]
    
    await client.send_message(
        'me',
        'Styled reply keyboard example:',
        buttons=reply_buttons
    )
    
    # Example 3: URL and auth buttons with styles
    url_buttons = [
        [
            Button.url("Open Telegram", "https://t.me", style=primary_style),
            Button.url("Danger Link", "https://example.com", style=danger_style)
        ],
        [
            Button.auth("Login with Telegram", "https://example.com/auth", style=success_style)
        ]
    ]
    
    await client.send_message(
        'me',
        'Styled URL and auth buttons:',
        buttons=url_buttons
    )
    
    print("Styled keyboard examples sent! Check your saved messages.")
    
    await client.disconnect()


if __name__ == '__main__':
    api_id = 12345
    api_hash = 'your_api_hash_here'
    
    asyncio.run(main())

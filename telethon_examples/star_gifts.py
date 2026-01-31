"""
Example demonstrating StarGift functionality (Layer 224 feature).

This example shows how to handle star gift service messages and work
with the new MessageServiceType entries.
"""
import asyncio
from herokutl import TelegramClient, events, MessageServiceType


async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()
    
    print("Star Gift Example Started")
    print("This bot will handle star gift service messages.")
    
    @client.on(events.NewMessage)
    async def handler(event):
        message = event.message
        
        # Check if this is a service message and get its type
        if message.service_type:
            service_type = message.service_type
            
            if service_type == MessageServiceType.STAR_GIFT:
                print(f"🌟 Received star gift from {message.sender_id}")
                print(f"Message ID: {message.id}")
                if message.action:
                    print(f"Gift details: {message.action}")
                
                # You can access the gift information through the action
                # For example, to get the gift details:
                if hasattr(message.action, 'gift'):
                    gift = message.action.gift
                    print(f"Gift: {gift}")
                    
            elif service_type == MessageServiceType.STAR_GIFT_UNIQUE:
                print("💎 Received unique/collectible star gift!")
                print(f"Message ID: {message.id}")
                if message.action:
                    print(f"Unique gift details: {message.action}")
                    
            elif service_type == MessageServiceType.NEW_CREATOR_PENDING:
                print("👤 New creator transfer pending")
                print(f"Message ID: {message.id}")
                if message.action:
                    print(f"Transfer details: {message.action}")
                    
            elif service_type == MessageServiceType.CHANGE_CREATOR:
                print("🔄 Creator changed")
                print(f"Message ID: {message.id}")
                if message.action:
                    print(f"Change details: {message.action}")
        
        # Handle regular messages
        elif message.text:
            print(f"Regular message: {message.text}")
    
    # Example: Send a message to test the bot
    await client.send_message(
        'me',
        "Star Gift handler is active! Send me a star gift to test the functionality.\n\n"
        "I can handle these service message types:\n"
        "• STAR_GIFT - Regular star gifts\n"
        "• STAR_GIFT_UNIQUE - Unique/collectible star gifts\n"
        "• NEW_CREATOR_PENDING - Pending creator transfers\n"
        "• CHANGE_CREATOR - Creator changes\n\n"
        "The service_type property makes it easy to identify message types!"
    )
    
    print("Bot is running. Press Ctrl+C to stop.")
    
    # Keep the bot running
    try:
        await client.run_until_disconnected()
    except KeyboardInterrupt:
        print("Stopping bot...")
        await client.disconnect()


if __name__ == '__main__':
    # Replace with your actual API credentials
    api_id = 12345
    api_hash = 'your_api_hash_here'
    
    asyncio.run(main())

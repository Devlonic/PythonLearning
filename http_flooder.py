from telethon.sync import TelegramClient

# Replace these values with your own
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'

# Create a new TelegramClient instance
client = TelegramClient('session_name', api_id, api_hash)


async def send_message():
    # Start the client
    await client.start(phone_number)

    # Replace 'USERNAME' with the username of the recipient (or use a phone number)
    await client.send_message('USERNAME', 'Your message here')

    # Close the client
    await client.disconnect()

# Run the send_message function
with client:
    client.loop.run_until_complete(send_message())

from server_status import status_check
import keep_alive
import discord
import os

TOKEN = os.environ['TOKEN']   # Token is hidden inside replit/secrets

client = discord.Client()


# On ready in console message
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# Bot waiting event for in chat message's
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]  # AFO_BOT#3348 -> AFO_BOT
    user_message = str(message.content)  # Content of message typed by user
    channel = str(message.channel.name)  # Channel where the message appear
    print(f'{username}: {user_message} ({channel})')  # In console log from event

    # Preventing bot from his self answearing
    if message.author == client.user:
        return

    # Testing feature
    if message.channel.name == 'test':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return

    # Checking server status - function status_check is returning dictionary
    if user_message.lower() == '!procyon':
        response = status_check()
        for server, status in response.items():
            if server == 'Procyon':
                if status == 'Good':
                    await message.channel.send(f'{server}  :white_check_mark:')
                else:
                    await message.channel.send(f'Server may be down...')


keep_alive.keep_alive()
client.run(TOKEN)

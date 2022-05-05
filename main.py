from server_status import status_check
import keep_alive
import discord
import os

TOKEN = os.environ['TOKEN']  # Token is hidden inside replit/secrets

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

    # Preventing bot from self answering
    if message.author == client.user:
        return

    # Test feature
    if message.channel.name == 'test':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return

    # In discord chat available command's by simple typing !help
    if user_message.lower() == '!help':
        await message.channel.send(f'Command List: !help, !procyon')

    # Checking server status - function status_check is returning dictionary
    if user_message.lower() == '!procyon':
        response = status_check()
        for server, status in response.items():
            if server == 'Procyon':
                if status == 'Good':
                    await message.channel.send(f'{server}  :green_circle:')
                elif status == 'Full':
                    await message.channel.send(f'{server}  :red_circle:')
                elif status == 'Busy':
                    await message.channel.send(f'{server}  :orange_circle:')
                elif status == 'Maintenance':
                    await message.channel.send(f'{server}  :wrench:')
                else:
                    await message.channel.send(f'Server may be down...')


keep_alive.keep_alive()
client.run(TOKEN)

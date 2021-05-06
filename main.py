from telethon import events, Button, TelegramClient
from config import var

client = TelegramClient('Bot', var.APP_ID, var.API_HASH).start(bot_token=var.BOT_TOKEN) 

@client.on(events.NewMessage)
async def start(event):
    await event.reply("Sample login example./nJoin @j_projects", buttons=[Button.auth("⚡️Login⚡️", url=f'{var.APP_DOMAIN}/')])

if __name__ == "__main__":
    client.run_until_disconnected()

import discord
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID_BOT')


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_member_join(self, member):
        channel = self.get_channel(int(CHANNEL_ID))
        nickname = member.nick if member.nick else member.name
        await channel.send(
            f'환영합니다, {nickname}님! 경소고 마크 서버에 오신 것을 환영합니다 :)'
        )


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = MyClient(intents=intents)
client.run(TOKEN)

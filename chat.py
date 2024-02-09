import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID_CHAT')


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('/채팅 청소-') and message.channel.id == int(CHANNEL_ID):
            try:
                num = message.content.replace('/채팅 청소-', '').strip()
                num = int(num)
                await message.channel.purge(limit=num + 1)
                await message.channel.send(f'{num}개의 메시지를 삭제했습니다.')
            except ValueError:
                await message.channel.send('삭제할 메시지의 개수를 정확히 입력해주세요. 예) /채팅 청소-7')

        if message.content.startswith('/채팅 모두 청소') and message.channel.id == int(CHANNEL_ID):
            deleted = await message.channel.purge(limit=100)
            while len(deleted) == 100:
                deleted = await message.channel.purge(limit=100)
            await message.channel.send('모든 메시지를 삭제했습니다.')


intents = discord.Intents.all()
client = MyClient(intents=intents)
client.run(TOKEN)

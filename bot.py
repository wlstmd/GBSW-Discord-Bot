import discord

TOKEN = 'MTIwMzA0ODg0NTYzOTAyODc1Ng.GzP8H0.CMu55npb1P-bwnA1puC2B5yfTiuqIST5MVuj0o'
CHANNEL_ID = '1202554951771881515'


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_member_join(self, member):
        channel = self.get_channel(int(CHANNEL_ID))
        await channel.send(
            '환영합니다, {}!'.format(member.name) + '님 경소고 마크 서버에 오신 것을 환영합니다 :)'
        )


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = MyClient(intents=intents)
client.run(TOKEN)

import discord

TOKEN = 'MTIwMzA0ODg0NTYzOTAyODc1Ng.GzP8H0.CMu55npb1P-bwnA1puC2B5yfTiuqIST5MVuj0o'
CHANNEL_ID = '1203045377087897702'

server_rules = ['🍀 심한 욕설 금지', '🍀 일베 금지']
mc_rules = ['🍀 심한 욕설 금지', '🍀 일베 금지']


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('/규칙') and message.channel.id == int(CHANNEL_ID):
            rules = '\n'.join(server_rules)
            await message.channel.send(f'**서버 규칙**\n```{rules}```')

        if message.content.startswith('/MC 규칙') and message.channel.id == int(CHANNEL_ID):
            rules = '\n'.join(mc_rules)
            await message.channel.send(f'**경소고 마크 서버 규칙**\n```{rules}```')

        if message.content.startswith('/경소고 마크 서버') and message.channel.id == int(CHANNEL_ID):
            await message.channel.send(f'**경소고 마크 서버**\n```🍀 서버 주소 : mc.dya.codes\n\n🍀 grafana: 3.35.156.173:3000```')

        if message.content.startswith('/서버 멤버') and message.channel.id == int(CHANNEL_ID):
            members = '\n'.join([f'🍀 {member.display_name}' for member in message.guild.members])
            await message.channel.send(f'**디코 서버 멤버**\n```{members}```')

        if message.content.startswith('/온라인 멤버') and message.channel.id == int(CHANNEL_ID):
            online_members = '\n'.join([f'🟢 {member.display_name}' for member in message.guild.members if member.raw_status in ['online', 'idle', 'dnd']])
            await message.channel.send(f'**디코 온라인 멤버**\n```{online_members}```')

        if message.content.startswith('/오프라인 멤버') and message.channel.id == int(CHANNEL_ID):
            offline_members = '\n'.join([f'🔴 {member.display_name}' for member in message.guild.members if member.raw_status in ['offline']])
            await message.channel.send(f'**디코 오프라인 멤버**\n```{offline_members}```')

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


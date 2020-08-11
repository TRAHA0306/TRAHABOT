# -*- coding:utf-8 -*- 
# 가끔가다 애가 인코딩을 잘못 읽어서 오류를 냅니다. 그것을 대비하기 위해 'utf-8'으로 읽으라고 선언함

import discord
import os

 
access_token = os.envirin["BOT_TOKEN"]
token = "access_token"
client = discord.Client()

@client.event
async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.
  # 봇이 "반갑습니다"를 플레이 하게 됩니다.
  # discord.Status.online에서 online을 dnd로 바꾸면 "다른 용무 중", idle로 바꾸면 "자리 비움"으로 바뀝니다.
  await client.change_presence(status=discord.Status.online, activity=discord.Game("벤틀리서버"))
  print("원진#7917") 
  print(client.user.name) 
  print(client.user.id) 

   

badwords = ["시발","닥쳐","섹스","년","새끼","섹","ㅈ같다","ㄴㄱㅁ","느금마","창년","애미","애비","엄마","씨발","병신","장애"]

@client.event 
async def on_message(message):

    for word in badwords:
        if message.content.count(word) > 0:
            print("욕설이 감지되어 삭제처리 되었습니다.")
            print(message.author.id)
            await message.channel.purge(limit=1)
    for word in badwords:
        author = message.guild.get_member(int(message.author.id))
        if message.content.count(word) > 0:
            await message.channel.send(embed=embed)

            

embed=discord.Embed(title="파이브엠 서포터즈", description="욕설이 감지되어 삭제처리 되었습니다 ", color=0xCC0045)



client.run(token)








  
access_token = os.envirin["BOT_TOKEN"]
client.run(access_token)


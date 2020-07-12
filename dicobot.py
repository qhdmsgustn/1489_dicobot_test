import discord

class chatbot(discord.Client):
    # 프로그램 처음 실행될때 구성
    async def on_ready(self):
        # 상태메시지
        # 종류 3가지 : Game, Streaming, CustomAActivity
        game = discord.Game("내용")

        # 계정상태변경
        # 온라인상태,game 중으로 변경
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔창에 "Ready!"라고 표시
        print("Ready")

    async def on_message(self,message):
        #sender가 bot일경우 반응 x
        if message.author.bot:
            return None
        
        #message.content = messasge 내용
        if message.content == "!바보":
            #현재 채널 받아옴
            channel = message.channel
            #답변내용 구성
            msg = "너도 바보"
            #msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

if __name__ == "__main__":
    #객체 생성
    client = chatbot()
    #Token 값을 통해 로그인하고 봇 실행
    client.run("토큰")
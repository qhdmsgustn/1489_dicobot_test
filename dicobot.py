import discord
from googletrans import Translator
from discord.utils import get
from discord.ext import commands

token="NzMxNzk5MDg4MjQ4NTIwNzMy.XwxIYQ.kCEuQgC9gmoGSWC8o9LYa39H4C4"

#명령어
client = commands.Bot(command_prefix = '!') 
client.remove_command('help')

###봇 시작###
@client.event
async def on_ready():
    game = discord.Game('Test bot')
    await client.change_presence(status=discord.Status.online, activity=game)
    print(f'{client.user} 에 로그인하였습니다!')

###번역기###
@client.command(name="!",pass_context=True)
async def change_text(ctx,*,to_language):
#번역과정
    translator = Translator()

    if translator.detect(to_language).lang=="ko":
        temp_language = translator.translate(to_language,dest='en')
        from_language = temp_language.text
    else:
        temp_language = translator.translate(to_language,dest='ko')
        from_language = temp_language.text
#출력  
    await ctx.send(f"{ctx.author.mention}"+from_language)

###명령어(목록)###

@client.command(name="help")
async def helper(ctx):
    embed=discord.Embed(title="설명서(manual)", color=0x009dff)
    embed.set_author(name="통역관")
    embed.add_field(name="!! (text)", value="If you write !!(Space Bar)(content), Korean will be translated into English and other languages ​​will be translated into Korean\n!!(띄어쓰기)(내용)치면 알아서 번역해줌", inline=False)
    embed.add_field(name="!안녕", value="Say hello\n인사해줌", inline=True)
    await ctx.channel.send(embed=embed)

###명령어(대화)###

@client.command(aliases=['안녕','안녕하세요', 'ㅎㅇ','hi', 'HI','Hello','HELLO'])
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention}님 안녕하세요")


client.run(token)


###DM보내기###
#@client.command(name="DM보내기", pass_context=True)
#async def send_dm(ctx,user_name: discord.Member):
#    channel=await user_name.create_dm()
#    await channel.send("Hi~너에게 칭호를 주었어")

###채팅방 지우기###
#@client.command(name="청소",pass_context=True)
#async def clear(ctx,amount:int):
#    await ctx.channel.purge(limit=amount)

#@clear.error
#async def clear_error(ctx,error):
#    if isinstance(error, commands.MissingRequiredArgument):
#       await ctx.send('숫자를 입력해주세요.')
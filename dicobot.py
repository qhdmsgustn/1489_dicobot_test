import discord
from discord.utils import get
from discord.ext import commands

token="토큰을 넣으세요"

client = commands.Bot(command_prefix = '!') 
client.remove_command('help')

###봇 시작###
@client.event
async def on_ready():
    game = discord.Game('Test bot')
    await client.change_presence(status=discord.Status.online, activity=game)
    print(f'{client.user} 에 로그인하였습니다!')

###채팅방 지우기###
@client.command(name="청소",pass_context=True)

async def clear(ctx,amount:int):
    await ctx.channel.purge(limit=amount)
@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
       await ctx.send('숫자를 입력해주세요.')

###명령어(대화)###

@client.command(aliases=['안녕','안녕하세요', 'ㅎㅇ','hi', 'HI','Hello','HELLO'])
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention}님 안녕하세요")

@client.command()
async def 망포(ctx):
    await ctx.send("앞잡이")

@client.command() 
async def 바보(ctx):
    await ctx.send("너도")

###DM보내기###
@client.command(name="DM보내기", pass_context=True)
async def send_dm(ctx,user_name: discord.Member):
    channel=await user_name.create_dm()
    await channel.send("Hi~너에게 칭호를 주었어")

client.run(token)

import discord
from datetime import datetime, timedelta
from googletrans import Translator
from discord.utils import get
from discord.ext import commands

###최강의 지도자 리스트
chlrkd_list=['20200720','20200803','20200817','20200831','20200914','20200928','20201012','20201026','20201109','20201123','20201207','20201221','20210104','20210118','20210201','20210215','20210301','20210315','20210329','20210412','20210426','20210510','20210524','20210607','20210621','20210705','20210719','20210802']
chlrkd_name=['살라딘','콘스탄티누스','토미리스','아틸라','레오니다스','아르테미시아','테오도라']
###돌림판 리스트
ehffla_list=['20200623','20200707','20200721','20200804','20200818','20200901','20200915','20200929','20201013','20201027','20201110','20201124','20201208','20201222','20210105','20210119','20210202','20210216','20210302','20210316','20210330','20210413','20210427','20210511','20210525','20210608','20210622','20210706']
ehffla_name=['칭기즈칸','알렉산더','우드스톡','다케다신겐','관우','람세스','이순신']
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
    await ctx.send(f"{ctx.author.mention} "+from_language)

###명령어(목록)###

@client.command(name="help")
async def helper(ctx):
    embed=discord.Embed(title="설명서(manual)", color=0x009dff)
    embed.add_field(name="!! (text)", value="If you write !!(Space Bar)(content)\ntranslate", inline=False)
    embed.add_field(name="!안녕", value="Say hello\n인사해줌", inline=True)
    embed.add_field(name="!최지", value="최강의지도자 날짜", inline=True)
    embed.add_field(name="!돌림판", value="돌림판 날짜", inline=True)
    await ctx.channel.send(embed=embed)

###명령어(대화)###

@client.command(aliases=['안녕','안녕하세요', 'ㅎㅇ','hi', 'HI','Hello','HELLO'])
async def a1(ctx):
    await ctx.send(f"{ctx.author.mention}님 안녕하세요")

@client.command(name="1689")
async def a2(ctx):
    await ctx.send("화이팅~!")
 
@client.command(name="명령어")
async def a3(ctx):
    await ctx.send("무엇을 넣을까")

@client.command(name="최지")
async def a4(ctx):
    ###시간계산###
    now_time = datetime.utcnow()
    choice_time = datetime.strptime(chlrkd_list[0],'%Y%m%d')

    result_time = choice_time-now_time
    
    embed=discord.Embed(title="최강의지도자", color=0x009dff)
    #for chlrkd_Name in chlrkd_name:
        #for chlrkd_List in chlrkd_list(range(0,2)):
    embed.add_field(name="살라딘", value="카운트다운: "+str(result_time.days)+"일 "+str(timedelta(seconds=result_time.seconds)), inline=True)        
    await ctx.channel.send(embed=embed)

@client.command(name="돌림판")
async def a5(ctx):
    embed=discord.Embed(title="돌려돌려돌림판", color=0x009dff)
    embed.add_field(name="칭기즈칸", value="Say hello\n인사해줌", inline=True)
    await ctx.channel.send(embed=embed)


client.run(token)




###채팅방 지우기###
#@client.command(name="청소",pass_context=True)
#async def clear(ctx,amount:int):
#    await ctx.channel.purge(limit=amount)

###DM보내기###
#@client.command(name="DM", pass_context=True)
#async def send_dm(ctx,user_name: discord.Member,*,dm_message):
#    channel=await user_name.create_dm()
#    await channel.send(dm_message)

#@clear.error
#async def clear_error(ctx,error):
#    if isinstance(error, commands.MissingRequiredArgument):
#       await ctx.send('숫자를 입력해주세요.')
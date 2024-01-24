import discord
from discord.ext import commands
import time



intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.typing = False
intents.message_content = True
intents.reactions = True


bot = commands.Bot(command_prefix='!', intents=intents)


canal = None  # Define 'canal' as a global variable
  # Define 'canal' as a global variable

@bot.event
async def on_ready():
              print(f'{bot.user} has connected to Discord!')
              for guild in bot.guilds:
                  await create_roles(guild)

async def create_roles(guild):
              if not discord.utils.get(guild.roles, name="Verificado"):
               await guild.create_role(name="Verificado")
              if not discord.utils.get(guild.roles, name="Silenciado"):
                  await guild.create_role(name="Silenciado")

@bot.event
async def on_guild_join(guild):
              await create_roles(guild)
@bot.event
async def on_member_join(member):
    guild = bot.get_guild(member.guild.id)
    if guild is not None:
        user = bot.get_user(836958968730353704)
        await user.send(f'{member.mention} Acabou de entrar no servidor !! {guild.name}!')
    else:
        print("Guild is None. Unable to send message.")



@bot.command()
async def criar_cargos(ctx):
    roles = ['sub dono', 'Dono 2', 'Dono'] 

    for role in roles:
        await ctx.guild.create_role(name=role)
        await ctx.send(f'Cargo {role} criado com sucesso!')
print(' funcionou ! ')



@bot.command()
async def RAIVA(ctx):
  membro = ctx.author
  user = ctx.author
  await ctx.send(f'mano que raiva que o {membro.mention} está se ta maluko tome esse gif para você https://tenor.com/view/angry-cat-gif-24799029')
  await user.send(f'Relaxa doido vai passar já já ❤️❤️🏳️‍🌈')
  print('tudo certo !')

@bot.command()
async def emoji(ctx):
      user1 = bot.get_user(836958968730353704)  # Substitua pelo ID do primeiro usuário
      user2 = bot.get_user(1043624582524960852)  # Substitua pelo ID do segundo usuário
      user3 = bot.get_user(953047188294991902)
      emoji = '\U0001F600'  # Este é o código Unicode para o emoji de rosto sorridente
      await user1.send(f'Olá! Aqui está um emoji para você: {emoji}')
      await user2.send(f'Olá! Aqui está um emoji para você: {emoji}')
      await user3.send(f'Olá! Aqui está um emoji para você: {emoji}')



@bot.command()
async def delete(ctx, number: int):
    global canal  # Use the global variable 'canal'
    if isinstance(ctx.channel, discord.TextChannel):
        canal = bot.get_channel(1187738633592131604)  # Set the value of 'canal'
        await ctx.channel.purge(limit=number)
        await ctx.send(f'Deleted {number} messages in {ctx.channel.mention}.')
    else:
        await ctx.send("This command can only be used in text channels.")


@bot.command()
async def say(ctx, *, message):
    global canal  # Use the global variable 'canal'
    if isinstance(ctx.channel, discord.TextChannel):
        if canal is None:
            await ctx.message.delete()
            await canal.send(message)  # Send the 'message' to channel 'canal'
        else:
            await ctx.send("The 'canal' has not been set yet.")  # Handle the case where 'canal' is not set
    else:
        await ctx.send("This command can only be used in text channels.")


@bot.command()
async def castigar(ctx, membro: discord.Member):
    cargo_silenciado = discord.utils.get(ctx.guild.roles, name='Silenciado')  # Substitua 'Silenciado' pelo nome do seu cargo de silenciado
    if cargo_silenciado is not None:
      for cargo in membro.roles:  # Loop through all the member's roles
        try:
            if cargo != ctx.guild.default_role:  # Do not remove the default role (usually @everyone)
                await membro.remove_roles(cargo)  # Remove the role
        except discord.Forbidden:
            print(f"Não foi possível remover o cargo {cargo.name} de {membro.name}")
            await ctx.send(f"O cargo {cargo.name} Não foi removido de {membro.name}.")

        await membro.add_roles(cargo_silenciado)  # Adicione o cargo de silenciado
        await ctx.send(f'{membro.mention} foi castigado.')

    else:
        await ctx.send('Cargo de silenciado não encontrado.')

@bot.command()
async def Deletar_canal(ctx, canal: discord.TextChannel):
    await canal.delete()
    await ctx.send(f'O canal {canal.mention} foi apagado.')

@bot.command()
async def gozar(ctx):
    member = ctx.author  # Get the member who used the command
    await ctx.message.delete()
    await ctx.send(f'{member.mention} DISSE: 💦💦🥛💦💦🥛💦💦💦 AI GOZEI🥛💦💦💦🥛💦 https://tenor.com/view/milk-explde-explode-reddit-furry-gif-21627440')


@bot.command()
async def cmds(ctx):
  member = ctx.author
  await ctx.message.delete()
  await ctx.send(f'{member.mention}  Opa estes são os meus comandos disponiveis: !castigar, !Deletar_canal, !gozar, !say, !delete, !emoji, !cmds e !emoji_art por enquanto...')
  await ctx.send('atenção o commando say está bugado e delete é para apagar mensagens!')
@bot.command()
async def emoji_art(ctx):
    user = ctx.author  # Isso pega o usuário que chamou o comando
    # Esta é uma "arte" de emoji simples. Sinta-se à vontade para criar a sua própria!
    emoji_art = """
------🚗--------------
-----------🚙-----🚕-
--🚌----🚗-----------
------🐸-------🚒----
---🚙-------🚚-------
boa SEMANA!!!
       """
    await user.send(f'Aqui está a sua arte de emoji:\n{emoji_art}')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='verify')
async def verify(ctx):
    member = ctx.author
    message = await ctx.send("Reaja a esta mensagem para ser verificado!")
    await message.add_reaction('👍')  # O bot adiciona a reação '👍' à sua própria mensagem
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == '👍'
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('👎')
    else:
        role = discord.utils.get(user.guild.roles, name="Verificado")
        await user.add_roles(role)
        time.sleep(1)
        await ctx.send(f'o {member.mention}foi verificado! 👍')

@bot.command()
async def dm(ctx):
    member = ctx.author
    user = ctx.author
    await user.send(f'Olá!{member.mention} Tudo bom? bom este é meu link para você poder me usar em algum lugar ! https://discord.com/api/oauth2/authorize?client_id=1173622537024966719&permissions=40671259392832&scope=bot')


@bot.command(name ='sad', help ='esse commando manda uma mensagem em seu privado !')
async def sad(ctx):
  member = ctx.author
  await member.send("""Você está triste mano? tenho uma ideia para você de musica escute essa musica e ve se você gosta: https://www.youtube.com/watch?v=DZFDbIy3XS4&list=RDDZFDbIy3XS4&start_radio=1""")

  time.sleep(5)

  await member.send(" Relaxa doido vai passar eu já passei por isso eu não o devcpx meu criador")

  if False:
    print('Erro desconhecido...')
  else:
    print('Tudo certo no commando sad ! ...')

@bot.command()
async def resetar_chat(ctx):
    while True:
        deleted = await ctx.channel.purge(bulk=True)
        if len(deleted) < 100:
            break

bot.run('')

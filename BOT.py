import discord
import os
from discord.ext import commands


intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.guild_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    guild = ctx.guild

    categorias_e_canais = {
        "APOSTAS MOBILE": [
            "📱・1v1-mobile",
            "📱・2v2-mobile",
            "📱・3v3-mobile",
            "📱・4v4-mobile",
            "📱・adm-on",
        ],
        "APOSTAS TÁTICO": [
            "📚・regras-tatico",
            "🚩・1v1-tático",
            "🚩・2v2-tático",
            "🚩・3v3-tático",
            "🚩・4v4-tático",
        ],
        "APOSTA MISTO": [
            "🖥️・1v1-mis",
            "🖥️・2v2-mis",
            "🖥️・3v3-mis",
            "🖥️・4v4-mis",
        ],
        "POSTADOS EMU": [
            "🖥️・1v1-emu",
            "🖥️・2v2-emu",
            "🖥️・3v3-emu",
            "🖥️・4v4-emu",
        ],
    }

    for categoria_nome, canais in categorias_e_canais.items():
        categoria = await guild.create_category(categoria_nome)
        for canal_nome in canais:
            await guild.create_text_channel(canal_nome, category=categoria)

    await ctx.send("✅ Estrutura de canais criada com sucesso!")

import os

bot.run(os.getenv("TOKEN"))


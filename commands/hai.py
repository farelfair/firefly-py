from discord.ext import commands
import discord
from datetime import datetime

class Hai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hai(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(
            title="Halo!",
            description="Hai saya firefly senang bisa melihatmu di sini, Semoga harimu menyenangkan! kalau kamu butuh bantuan tinggal ketik `!help` ya 😊",
            color=3158325,
            timestamp=datetime.utcnow()
            )
        embed.set_footer(
                text=guild.name,
                icon_url=guild.icon.url if guild.icon else None
            )

        await ctx.reply(embed=embed, mention_author=True)

# Required setup function for extension loading
async def setup(bot):
    await bot.add_cog(Hai(bot))

from discord.ext import commands
import discord

class Hai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hai(self, ctx):
        embed = discord.Embed(
            title="Halo!",
            description="Hai saya Firefly, pembantu Anda. Apa yang harus saya lakukan?",
            color=3158325,
        )
        await ctx.reply(embed=embed, mention_author=True)

# Required setup function for extension loading
async def setup(bot):
    await bot.add_cog(Hai(bot))
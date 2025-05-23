from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help!",
            description="**!hai** - say hi for firefly",
            color=3158325,
        )
        await ctx.reply(embed=embed, mention_author=True)

# Required setup function for extension loading
async def setup(bot):
    await bot.add_cog(Help(bot))
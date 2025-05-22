from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help!",
            description="**!help** - show all list command\n**!hai** - say hi for firefly",
            color=int("303135", 16)
        )
        await ctx.reply(embed=embed, mention_author=True)

# Required setup function for extension loading
async def setup(bot):
    await bot.add_cog(Help(bot))
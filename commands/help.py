from discord.ext import commands
import discord
from datetime import datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(
            title="List Commands",
            color=3158325,
            timestamp=datetime.utcnow()
        )
        # field
        embed.add_field(
            name="General",
            value="**!hai** - say hi for firefly\n**!help** - show list cmd (test)",
            inline=False
        )
        # footer
        embed.set_footer(
                text=guild.name,
                icon_url=guild.icon.url if guild.icon else None
            )

        await ctx.reply(embed=embed, mention_author=True)

# Required setup function for extension loading
async def setup(bot):
    await bot.add_cog(Help(bot))
from discord.ext import commands
import discord

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="no reason given"):
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="Banned Member",
                description=f"{member.mention}",
                color=3158325,
            )
            embed.add_field(name="Alasan", value=reason, inline=False)
            embed.set_footer(text=f"Diban oleh: {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(
                title="Permission not allowed",
                description="firefly does not have permission",
                color=3158325,
            )
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="Error Detected",
                description=f"an error occurred: {e}",
                color=3158325,
            )
            await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="You don't have permission",
                description="Member jgn sok gaya",
                color=3158325,
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="⚠️ Wrong format",
                description="Format salah gunakan `!ban @user alasan`",
                color=3158325,
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            await ctx.send("⚠️ User tidak valid. Mention user seperti ini: `@username`")
        else:
            await ctx.send(f"⚠️ Terjadi error: {error}")

async def setup(bot):
    await bot.add_cog(Ban(bot))
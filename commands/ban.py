from discord.ext import commands
import discord

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="Tidak ada alasan diberikan"):
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="<a:banned:755637224854388809> Member Hitam out aja",
                description=f"{member.mention} sok asik jawa out aja sana",
                color=int("303135", 16)
            )
            embed.add_field(name="Alasan", value=reason, inline=False)
            embed.set_footer(text=f"Diban oleh: {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("❌ Saya tidak punya izin untuk memban member ini.")
        except Exception as e:
            await ctx.send(f"⚠️ Terjadi error: {e}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("⛔ Kamu tidak punya izin untuk menggunakan command ini.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("⚠️ Format salah. Contoh: `?ban @user alasan`")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("⚠️ User tidak valid. Mention user seperti ini: `@username`")
        else:
            await ctx.send(f"⚠️ Terjadi error: {error}")

async def setup(bot):
    await bot.add_cog(Ban(bot))
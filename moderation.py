import discord
from discord.ext import commands
from datetime import timedelta


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="clear", description="Delete messages")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):

        await ctx.channel.purge(limit=amount + 1)

        embed = discord.Embed(
            title="🧹 Messages Cleared",
            description=f"Deleted **{amount}** messages.",
            color=discord.Color.orange()
        )

        msg = await ctx.send(embed=embed)
        await msg.delete(delay=3)

    @commands.hybrid_command(name="kick", description="Kick a member")
    @commands.has_permissions(kick_members=True)
    async def kick(
        self,
        ctx,
        member: discord.Member,
        *,
        reason="No reason provided"
    ):

        await member.kick(reason=reason)

        embed = discord.Embed(
            title="👢 Member Kicked",
            color=discord.Color.orange()
        )

        embed.add_field(
            name="Member",
            value=member.mention,
            inline=False
        )

        embed.add_field(
            name="Reason",
            value=reason,
            inline=False
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(name="ban", description="Ban a member")
    @commands.has_permissions(ban_members=True)
    async def ban(
        self,
        ctx,
        member: discord.Member,
        *,
        reason="No reason provided"
    ):

        await member.ban(reason=reason)

        embed = discord.Embed(
            title="🔨 Member Banned",
            color=discord.Color.red()
        )

        embed.add_field(
            name="Member",
            value=member.mention,
            inline=False
        )

        embed.add_field(
            name="Reason",
            value=reason,
            inline=False
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(name="unban", description="Unban user")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: str):

        user = await self.bot.fetch_user(int(user_id))
        await ctx.guild.unban(user)

        embed = discord.Embed(
            title="✅ User Unbanned",
            description=f"{user}",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(name="timeout", description="Timeout a member")
    @commands.has_permissions(moderate_members=True)
    async def timeout(
        self,
        ctx,
        member: discord.Member,
        minutes: int,
        *,
        reason="No reason provided"
    ):

        await member.timeout(
            timedelta(minutes=minutes),
            reason=reason
        )

        embed = discord.Embed(
            title="⏳ Member Timed Out",
            color=discord.Color.yellow()
        )

        embed.add_field(
            name="Member",
            value=member.mention,
            inline=False
        )

        embed.add_field(
            name="Duration",
            value=f"{minutes} minutes",
            inline=False
        )

        embed.add_field(
            name="Reason",
            value=reason,
            inline=False
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(name="untimeout", description="Remove timeout")
    @commands.has_permissions(moderate_members=True)
    async def untimeout(
        self,
        ctx,
        member: discord.Member
    ):

        await member.timeout(None)

        embed = discord.Embed(
            title="✅ Timeout Removed",
            description=f"{member.mention}",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(name="lock", description="Lock channel")
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):

        await ctx.channel.set_permissions(
            ctx.guild.default_role,
            send_messages=False
        )

        embed = discord.Embed(
            title="🔒 Channel Locked",
            description=f"{ctx.channel.mention}",
            color=discord.Color.red()
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(name="unlock", description="Unlock channel")
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):

        await ctx.channel.set_permissions(
            ctx.guild.default_role,
            send_messages=True
        )

        embed = discord.Embed(
            title="🔓 Channel Unlocked",
            description=f"{ctx.channel.mention}",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="slowmode",
        description="Set channel slowmode"
    )
    @commands.has_permissions(manage_channels=True)
    async def slowmode(
        self,
        ctx,
        seconds: int
    ):

        await ctx.channel.edit(
            slowmode_delay=seconds
        )

        embed = discord.Embed(
            title="🐢 Slowmode Updated",
            description=f"Slowmode set to **{seconds} seconds**",
            color=discord.Color.orange()
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="rolegive",
        description="Give role to member"
    )
    @commands.has_permissions(manage_roles=True)
    async def rolegive(
        self,
        ctx,
        member: discord.Member,
        role: discord.Role
    ):

        await member.add_roles(role)

        embed = discord.Embed(
            title="✅ Role Added",
            color=discord.Color.green()
        )

        embed.add_field(
            name="Member",
            value=member.mention,
            inline=False
        )

        embed.add_field(
            name="Role",
            value=role.mention,
            inline=False
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="roleremove",
        description="Remove role from member"
    )
    @commands.has_permissions(manage_roles=True)
    async def roleremove(
        self,
        ctx,
        member: discord.Member,
        role: discord.Role
    ):

        await member.remove_roles(role)

        embed = discord.Embed(
            title="❌ Role Removed",
            color=discord.Color.red()
        )

        embed.add_field(
            name="Member",
            value=member.mention,
            inline=False
        )

        embed.add_field(
            name="Role",
            value=role.mention,
            inline=False
        )

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Moderation(bot))

import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="ping",
        description="Check bot latency"
    )
    async def ping(self, ctx):
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Latency: **{round(self.bot.latency * 1000)}ms**",
            color=discord.Color.blurple()
        )
        await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="av",
        description="Show a user's avatar"
    )
    async def av(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        embed = discord.Embed(
            title=f"{member.display_name}'s Avatar",
            color=discord.Color.blurple()
        )

        embed.set_image(url=member.display_avatar.url)

        await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="userinfo",
        description="Show user information"
    )
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        embed = discord.Embed(
            title="👤 User Information",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(url=member.display_avatar.url)

        embed.add_field(name="Username", value=str(member), inline=False)
        embed.add_field(name="User ID", value=member.id, inline=False)
        embed.add_field(name="Top Role", value=member.top_role.mention, inline=False)
        embed.add_field(name="Bot", value="Yes" if member.bot else "No", inline=False)
        embed.add_field(
            name="Joined Server",
            value=member.joined_at.strftime("%Y-%m-%d"),
            inline=False
        )
        embed.add_field(
            name="Account Created",
            value=member.created_at.strftime("%Y-%m-%d"),
            inline=False
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="u",
        description="Short userinfo command"
    )
    async def u(self, ctx, member: discord.Member = None):
        await self.userinfo(ctx, member)

    @commands.hybrid_command(
        name="nick",
        description="Change or remove a member nickname"
    )
    @commands.has_permissions(manage_nicknames=True)
    async def nick(
        self,
        ctx,
        member: discord.Member,
        *,
        nickname: str = None
    ):

        await member.edit(nick=nickname)

        if nickname is None:
            embed = discord.Embed(
                title="🗑️ Nickname Removed",
                description=f"Removed nickname from {member.mention}",
                color=discord.Color.orange()
            )
        else:
            embed = discord.Embed(
                title="✏️ Nickname Changed",
                color=discord.Color.green()
            )

            embed.add_field(
                name="Member",
                value=member.mention,
                inline=False
            )

            embed.add_field(
                name="New Nickname",
                value=nickname,
                inline=False
            )

        await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="roles",
        description="Show all server roles"
    )
    async def roles(self, ctx):

        roles = [role.mention for role in reversed(ctx.guild.roles[1:])]

        embed = discord.Embed(
            title="🎭 Server Roles",
            description="\n".join(roles[:50]),
            color=discord.Color.purple()
        )

        embed.set_footer(
            text=f"Total Roles: {len(ctx.guild.roles)-1}"
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="serverinfo",
        description="Show server information"
    )
    async def serverinfo(self, ctx):

        guild = ctx.guild

        embed = discord.Embed(
            title=f"🌐 {guild.name}",
            color=discord.Color.green()
        )

        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        embed.add_field(name="Owner", value=str(guild.owner), inline=False)
        embed.add_field(name="Server ID", value=guild.id, inline=False)
        embed.add_field(
            name="Created",
            value=guild.created_at.strftime("%Y-%m-%d"),
            inline=False
        )
        embed.add_field(
            name="Members",
            value=guild.member_count,
            inline=True
        )
        embed.add_field(
            name="Channels",
            value=len(guild.channels),
            inline=True
        )
        embed.add_field(
            name="Roles",
            value=len(guild.roles),
            inline=True
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="help",
        description="Show all commands"
    )
    async def help(self, ctx):

        embed = discord.Embed(
            title="📖 Gotham Bot Commands",
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="🛠 Moderation",
            value="""
.clear
.kick
.ban
.unban
.timeout
.untimeout
.lock
.unlock
.slowmode
""",
            inline=False
        )

        embed.add_field(
            name="🎭 Roles",
            value="""
.rolegive
.roleremove
.roles
""",
            inline=False
        )

        embed.add_field(
            name="👤 User",
            value="""
.av
.userinfo
.u
.nick
""",
            inline=False
        )

        embed.add_field(
            name="🌐 Server",
            value=".serverinfo",
            inline=False
        )

        embed.add_field(
            name="🏓 Utility",
            value="""
.ping
.help
""",
            inline=False
        )

        embed.set_footer(
            text="Programmed by d4sw."
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))

import aiohttp
import discord
from redbot.core import commands


class Insult(commands.Cog):
    """Polite user messaging."""

    def __init__(self, bot):
        self.bot = bot
        self.headers = {
            'X-Mashape-Key': 'kPgrTWlClqmshjyMDorgCZ0TcS6kp1ePfLUjsnCYR170S2VdWj',
            'Accept': 'text/plain',
        }

        self.params = {
            'mode': 'random',
        }

    def getActors(self, offender, target):
        bot = self.bot.user
        return bot, offender, target

    @commands.command()
    async def insult(self, ctx, user: discord.Member):
        """Tell user what you think of them!"""
        if not user:
            await ctx.send_help()
            return

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get('https://evilinsult.com/generate_insult.php?lang=en&type=text', params=self.params) as resp:

                if resp.status == 200:
                    bot, offender, target = self.getActors(ctx.message.author, user)
                    text = await resp.text()

                    if target == bot:
                        insult = f"{offender.mention}, {text.lower()}"
                    else:
                        insult = f"{target.mention}, {text.lower()}"

                    await ctx.send(insult)

                else:
                    await ctx.send(f"I've got nothing to say to the likes of you (Code {resp.status})")

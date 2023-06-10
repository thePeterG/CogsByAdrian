import discord
import random
import time
from redbot.core import commands


class Killer(commands.Cog):
    """Do unto others as you would have them do unto you"""

    def __init__(self, bot):
        self.bot = bot

    def getActors(self, killer, target):
        return {'id': self.bot.user.id, 'nick': self.bot.user.display_name, 'formatted': self.bot.user.mention}, {'id': killer.id, 'nick': killer.display_name, 'formatted': "<@{}>".format(killer.id)}, {'id': target.id, 'nick': target.display_name, 'formatted': target.mention}

    # SLAP
    @commands.command()
    async def slap(self, ctx, *, user: discord.Member):
        """Open hand, not a closed fist!"""

        killer = ctx.author

        bot, killer, target = self.getActors(killer, user)

        diceroll = random.randint(0, 100)

        if target['id'] == bot['id']:  # trying to slap the bot, eh?

            message1 = "{} looks at {}... ✋😏 🤖".format(
                killer['nick'], bot['nick'])
            message2 = "but {} suddenly slaps {} with his silver sword! 😵💫 🍆🤖".format(
                bot['nick'], killer['nick'])

        elif killer['id'] == target['id']:  # wants to slap themselves

            message1 = "{} looks themselves in the mirror... 🖼😐".format(
                killer['nick'])

            if diceroll > 89:
                message2 = "and smashes their head against it! ✨🖼💥😫"

            elif diceroll > 10:
                message2 = "and gently pats their cheeks to wake up! 🖼😊"

            else:
                message2 = "and trips on the wet floor! Ouch! 🤕"

        else:  # wants to slap another user

            message1 = "{} raises their hand... ✋😏".format(killer['nick'])

            if diceroll > 89:
                message2 = "and mutilates {}! Oh my god, there's blood everywhere! 😵💥🤛😡".format(
                    target['formatted'])

            elif diceroll > 50 and diceroll < 55:
                message2 = "and gives {} a romantic spanking 😊🍑 👋😍".format(
                    target['formatted'])

            elif diceroll > 10:
                message2 = "and slaps {} senseless! 😫💫👋😠".format(
                    target['formatted'])

            else:
                message2 = "and misses! So stupid! 👋😟💨 😛"

        await ctx.send(message1)
        time.sleep(1)
        await ctx.send(message2)

    # PUNCH
    @commands.command()
    async def punch(self, ctx, *, user: discord.Member):
        """Open up a can of whoop-ass on a user!"""

        killer = ctx.author

        bot, killer, target = self.getActors(killer, user)

        diceroll = random.randint(0, 100)

        if target['id'] == bot['id']:  # trying to punch the bot, eh?

            message1 = "{} waves their fists at {}... 🤖 ✊"

from .penis import Insult

async def setup(bot):
    await bot.add_cog(Insult(bot))

import discord
from discord.ext import commands

from googletrans import Translator


class Translate(commands.Cog):
    """Class to translate user provided strings."""
    
    def __init__(self, bot):
        self.bot = bot
        self.tr = Translator()
        
    @commands.command()
    async def translate(self, ctx, *to_translate: str, ):
        to_translate = ' '.join(to_translate[:])
        translated_text = self.tr.translate(to_translate).text
        await ctx.send(translated_text)
        

def setup(bot):
    bot.add_cog(Translate(bot))
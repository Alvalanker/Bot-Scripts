import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
async def music(ctx):
    response = "All info about Alvalanker: LINKS: https://linktr.ee/alvalanker"
    await ctx.send(response)


@bot.command()
async def spotify(ctx):
    response = "Spotify https://open.spotify.com/artist/12O6L9BEaefqiZ5eQ2XD9R"
    await ctx.send(response)


@bot.command()
async def itunes(ctx):
    response = "Apple Music https://music.apple.com/us/artist/alvalanker/1403509237"
    await ctx.send(response)


@bot.command()
async def soundcloud(ctx):
    response = "SoundCloud https://soundcloud.com/alvalanker/radiation"
    await ctx.send(response)


@bot.command()
async def discord(ctx):
    response = "Discord https://discord.gg/tzycU3vf6r"
    await ctx.send(response)


@bot.command()
async def instagram(ctx):
    response = "Instagram https://www.instagram.com/alvalanker1"
    await ctx.send(response)


@bot.command()
async def facebook(ctx):
    response = "Facebook http://http://www.facebook.com/relicradiationmusic"
    await ctx.send(response)


@bot.command()
async def youtube(ctx):
    response = "YouTube https://www.youtube.com/@alvalankerofficial"
    await ctx.send(response)


@bot.command()
async def hello(ctx):
    response = f"Hello {ctx.author.mention}! I am just here to provide an information database for Alvalanker. I can't really help you with anything else at this time, but I hope to be upgraded in the near future. Until then, feel free to ask Rommel to tell you a joke!"
    await ctx.send(response)


@bot.command()
async def joke(ctx):
    response = "Why don't scientists trust atoms? Because they make up everything!"
    await ctx.send(response)


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        author = message.author
        content = message.content.lower()

        if any(keyword in content for keyword in ["music", "new", "links", "link", "discog", "disc", "songs", "discography", "website", "info", "information"]):
            response = f"{author.mention}, All info about Alvalanker: LINKS: https://linktr.ee/alvalanker"
            await message.channel.send(response)
        elif "spotify" in content:
            response = f"Spotify https://open.spotify.com/artist/12O6L9BEaefqiZ5eQ2XD9R"
            await message.channel.send(response)
        elif "itunes apple" in content:
            response = f"Apple Music https://music.apple.com/us/artist/alvalanker/1403509237"
            await message.channel.send(response)
        elif "soundcloud" in content:
            response = f"SoundCloud https://soundcloud.com/alvalanker/radiation"
            await message.channel.send(response)
        elif "discord" in content:
            response = f"Discord https://discord.gg/tzycU3vf6r"
            await message.channel.send(response)
        elif "instagram" in content:
            response = f"Instagram https://www.instagram.com/alvalanker1"
            await message.channel.send(response)
        elif "facebook" in content:
            response = f"Facebook http://http://www.facebook.com/relicradiationmusic"
            await message.channel.send(response)
        elif "youtube" in content:
            response = f"YouTube https://www.youtube.com/@alvalankerofficial"
            await message.channel.send(response)
        elif any(keyword in content for keyword in ["hello", "sup", "hey", "whats up"]):
            response = f"Hello {author.mention}! I am just here to provide an information database for Alvalanker. I can't really help you with anything else at this time, but I hope to be upgraded in the near future. Until then, feel free to ask Rommel to tell you a joke!"
            await message.channel.send(response)
        elif "fuck" in content:
            response = f"Haha {author.mention}! Go fuck yourself!"
            await message.channel.send(response)
        else:
            response = f"I'm sorry, {author.mention}, I didn't understand your question. I am only here to provide information about Alvalanker, so ask me something like 'music', 'links', 'songs', 'discography', 'website', or 'info'."
            await message.channel.send(response)

    await bot.process_commands(message)


# Run the bot with your bot token
bot.run("TOKEN")

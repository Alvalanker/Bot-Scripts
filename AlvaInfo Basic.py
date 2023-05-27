import discord
from discord.ext import commands
import gspread
from google.oauth2.service_account import Credentials

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Load the credentials using the OAuth client ID credentials
credentials = Credentials.from_service_account_file('eminent-subject-387503-38373d56ce0e.json')
credentials = credentials.with_scopes(['https://www.googleapis.com/auth/spreadsheets'])
# Authorize the credentials and create a client to access the Google Sheets API
client = gspread.authorize(credentials)

@bot.command(name='reload')
async def reload_module(ctx, module):
    bot.reload_extension(module)
    await ctx.send(f"Reloaded module: {module}")

@bot.command(name='disc')
async def discography(ctx):
    spreadsheet_id = "18_crzaHZ00xbr9OdjmetRTKVJV1OvVMQeCDUgWvnHCU"
    try:
        spreadsheet = client.open_by_key(spreadsheet_id)
        worksheet = spreadsheet.get_worksheet(0)  # Replace 0 with the index of the desired worksheet
        # Fetch data from the worksheet
        data = worksheet.get_all_values()
        # Create the discography message
        discography_message = 'Discography:\n'
        for row in data:
            album = row[0]
            songs = row[1:]
            discography_message += f'Album: {album}\n'
            for song in songs:
                discography_message += f'- {song}\n'
            discography_message += '\n'
        # Send the discography message
        await ctx.send(discography_message)
    except gspread.exceptions.APIError as e:
        print(f"Error accessing Spreadsheet {spreadsheet_id}: {str(e)}")

@bot.command(name='sheets')
async def quarterly_earnings(ctx):
    spreadsheet_ids = [
        "1fZdlxKl-M4iyPmBa243pivpQ14CGdiY9Rpn1OmgyjNI",
        "15AnwgH1CdUneQpKDlcHT1UKghEb7K9SStzpclk_WA30",
        "1lvUTXUcPtV9njNBRrp5mWGS2zmmWeSjJmX4PVXqUweM",
        # Add the remaining spreadsheet IDs here
    ]
    earnings_message = 'Quarterly Earnings:\n'
    for i, spreadsheet_id in enumerate(spreadsheet_ids, start=1):
        try:
            spreadsheet = client.open_by_key(spreadsheet_id)
            # You can modify the code here to fetch the desired data from each spreadsheet
            earnings_message += f'Spreadsheet {i}: {spreadsheet.title}\n'
        except gspread.exceptions.APIError as e:
            print(f"Error accessing Spreadsheet {spreadsheet_id}: {str(e)}")
    # Send the earnings message
    await ctx.send(earnings_message)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if bot.user.mentioned_in(message):
        author = message.author
        content = message.content.lower()

        if any(keyword in content for keyword in ["music", "new", "links", "discog", "disc", "songs", "discography", "website", "info", "information"]):
            response = f"{author.mention}, All info about Alvalanker: LINKS: https://linktr.ee/alvalanker\n"
            # Send the response
            await message.channel.send(response)
        elif "spotify" in content:
            response = f"Spotify https://open.spotify.com/artist/12O6L9BEaefqiZ5eQ2XD9R\n"
            await message.channel.send(response)
        elif "itunes apple" in content:
            response = f"Apple Music https://music.apple.com/us/artist/alvalanker/1403509237\n"
            await message.channel.send(response)
        elif "soundcloud" in content:
            response = f"SoundCloud https://soundcloud.com/alvalanker/radiation\n"
            await message.channel.send(response)
        elif "discord" in content:
            response = f"Discord https://discord.gg/tzycU3vf6r\n"
            await message.channel.send(response)
        elif "instagram" in content:
            response = f"Instagram https://www.instagram.com/alvalanker1\n"
            await message.channel.send(response)
        elif "facebook" in content:
            response = f"Facebook http://http://www.facebook.com/relicradiationmusic\n"
            await message.channel.send(response)
        elif "youtube" in content:
            response = f"YouTube https://www.youtube.com/@alvalankerofficial\n"
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

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Run the bot with your bot token
bot.run("TOKEN")

import discord
import yaml
import re
import asyncio
from pathlib import Path

# ---------------- CONFIG ----------------
TOKEN = "YOUR_BOT_TOKEN"  # <-- Replace with your bot token
CASES_FOLDER = "../_cases/"
DATA_FOLDER = "../_data/court_proceedings"

# Set up intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Required to read message content

client = discord.Client(intents=intents)


def message_to_dict(msg: discord.Message):
    """Convert a Discord message to dictionary for YAML export."""
    simple_embeds = []
    for e in msg.embeds:
        data = e.to_dict()
        simple_embeds.append({
            "title": data.get("title"),
            "url": data.get("url")
        })

    # Get the raw content
    content = msg.content or None
    
    # Resolve pinged users
    pinged_users = []
    if content:
        matches = re.findall(r'<@(\d+)>', content)
        for user_id in matches:
            member = msg.guild.get_member(int(user_id))
            if member:
                pinged_users.append({"id": user_id, "name": member.display_name})
            else:
                pinged_users.append({"id": user_id, "name": "Unknown User"})

    return {
        "username": msg.author.name,
        "avatar_url": str(msg.author.display_avatar.url),
        "content": content,
        "timestamp": msg.created_at.isoformat(),
        "attachments": [att.url for att in msg.attachments],
        "stickers": [sticker.name for sticker in msg.stickers],
        "embeds": [e for e in simple_embeds if e["title"] or e["url"]],
        "pinged_users": pinged_users,
    }


# Main function to run the bot and its logic
async def main():
    try:
        # 1️⃣ Ask for case slug
        slug = input("Enter case slug (e.g., spion-v-huckle): ").strip()
        case_file_path = Path(CASES_FOLDER) / f"{slug}.md"

        if not case_file_path.exists():
            print(f"Case file {CASES_FOLDER}/{slug}.md not found!")
            return

        # 2️⃣ Ask for Discord message link
        link = input("Enter a Discord message link: ").strip()
        match = re.match(r"https://discord.com/channels/(\d+)/(\d+)/(\d+)", link)
        if not match:
            print("Invalid link format!")
            return

        guild_id, channel_id, message_id = map(int, match.groups())
        
        # 3️⃣ Wait for bot to be ready before proceeding
        await client.wait_until_ready()

        # 4️⃣ Get guild and channel
        guild = client.get_guild(guild_id)
        if not guild:
            print("Guild not found or bot not in this server!")
            return

        channel = guild.get_channel(channel_id)
        if not channel:
            print("Channel not found or bot has no access!")
            return

        print(f"Fetching messages from channel {channel.name}...")

        messages = []

        # 5️⃣ Fetch original message
        try:
            original = await channel.fetch_message(message_id)
            messages.append(message_to_dict(original))
        except Exception as e:
            print(f"Could not fetch original message: {e}")
        
        # 6️⃣ Fetch all messages after original
        try:
            async for msg in channel.history(after=discord.Object(id=message_id), limit=None):
                messages.append(message_to_dict(msg))
        except Exception as e:
            print(f"Error fetching channel history: {e}")

        if not messages:
            print("No messages fetched.")
        else:
            # 7️⃣ Save messages to _data
            data_folder = Path(DATA_FOLDER)
            data_folder.mkdir(parents=True, exist_ok=True)
            output_file = data_folder / f"{slug}.yaml"

            with open(output_file, "w", encoding="utf-8") as f:
                yaml.dump(messages, f, allow_unicode=True)

            print(f"Messages saved to {output_file}")
            
    finally:
        # 8️⃣ This ensures the client closes gracefully
        print("Closing client...")
        await client.close()


# This creates a task for the main logic and runs the bot client
async def run_bot():
    try:
        await asyncio.gather(
            client.start(TOKEN),
            main()
        )
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the entire application
if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        print("Exiting...")
from pyrogram import Client, filters

# Replace 'my_bot' with a unique name for your bot session and provide your bot token, api_id, and api_hash.
app = Client(
    "my_bot",

)

# Handler for start command
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello {message.from_user.first_name}! How can I help you today?")

# Handler for echoing messages
@app.on_message(filters.text & ~filters.command(["start"]))
def echo(client, message):
    message.reply_text(message.text)

# Run the bot
app.run()

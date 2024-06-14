from pyrogram import Client, filters

# Replace 'my_bot' with a unique name for your bot session and provide your bot token, api_id, and api_hash.
app = Client(
    "my_bot",
    api_id=27376757,
    api_hash="27d4e363b3524401b62e86f1cc16c096",
    bot_token="7413073877:AAFIMuTZM0IQjANvmakArpS0sfUuOU7ohj4"
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
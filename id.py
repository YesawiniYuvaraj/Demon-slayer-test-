import pyrogram
from pyrogram import Filters, Client

@app.on_message(Filters.command("id"))
def get_reply_info(client, message):
    user_id = message.from_user.id
    group_id = message.chat.id
    
    message.reply_text(f"User ID: {user_id}\nGroup/Chat ID: {group_id}")

app.run()

from pyrogram import Client, filters


@app.on_message(filters.private("start"))
async def start(client, message):
    await message.reply("Hello Guys you need to start your journey")
Button = InlineKeyboardMarkup
(
    [
        [
  InlineKeyboardButton("Yes", callback_data="yes"),
InlineKeyboardButton("No", callback_data="no")
]
    ]
)

if yes= Button = InlineKeyboardMarkup
(
    [
        [
          InlineKeyboardButton("Zenitsu Agatsuma", callback_data="zen"),
          InlineKeyboardButton("Nezuko Kamado", callback_data="nez"),
          InlineKeyboardButton("Hashira Inosuke", callback_data="has"),
]
    ]
)

if no = await message.reply_text("OK HAVE I GOOD DAY") 

if zen = await message.reply_text ("pic=https://telegra.ph/file/81ae53d2e76474ecdb0b0.jpg has been added to your /myslayer list")

if nez = await message.reply_text("pic=https://telegra.ph/file/4c8d263a06f836a988f81.jpg has been added to your /myslayer list")

if has
= await message.reply_text("pic=https://telegra.ph/file/2fdc05423bcf6c570ae7a.jpg has been added to you /myslayer list")

app.run()

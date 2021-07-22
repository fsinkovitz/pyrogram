from pyrogram import Client

api_id = 
api_hash = ""

with Client("minha_conta", api_id,"api_hash") as app:
    chat = app.get_chat("Supergroup Title")
print(chat)
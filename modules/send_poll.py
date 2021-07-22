from pyrogram import Client

api_id = 
api_hash = ""

with Client("minha_conta", api_id,"api_hash") as app:
    app.send_poll(chat_id, "Prefere o Sim, o Não ou o Talvez?", ["Sim", "Não", "Talvez"])
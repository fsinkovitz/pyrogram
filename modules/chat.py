from pyrogram import Client

api_id = 
api_hash = ""

with Client("minha_conta", api_id,"api_hash") as app:
    app.send_message(
    chat_id, "Bom dia rapaziada")
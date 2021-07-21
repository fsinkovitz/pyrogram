from pyrogram import Client

app = Client("minha_conta")

with app:
    app.send_message("De boas manok")
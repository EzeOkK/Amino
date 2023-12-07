email = " " # Coloque seu email
password= " " # Coloque sua senha

try:
  import BotAmino
  from BotAmino import BotAmino, Parameters
except:
  import os
  os.system("pip install aminofix BotAmino")

client = BotAmino(email=email, password=password)

@client.on_member_join():
def welcome(data):
  data.send_message(data.chatId, f"Olá {data.author}n")


client.launch()

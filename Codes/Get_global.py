email = " " # Coloque seu email
password = " " #Coloque sua senha
link = " " # Link do perfil


try:
  import aminofix
except:
  import os
  os.system("pip install amino.fix")
  import aminofix as amino

client = amino.Clieny()
client.login(email=email, password=password)

uid = client.get_from_code(link). objectId

print(f"ndc//:user-profile/{uid}")

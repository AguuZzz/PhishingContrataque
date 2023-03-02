import requests
import random
import time
import os 
import string
from fake_useragent import UserAgent

ua = UserAgent()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

#Inicio
cls()
print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⠦⡄⠀⠀⠀⠀⠀⠀⡴⠀⠀⠀
⠀⢀⣀⠀⠀⠀⣀⠤⠖⠒⠋⡉⠙⢲⣺⢅⡀⠀⠹⡀⠀⠀⠀⢀⡜⠁⠀⠀⠀
⣼⠉⠀⠉⠓⠏⠁⠀⠀⠀⠀⢯⣧⠈⢿⡆⠈⠓⢴⠇⠀⠀⣠⠊⠀⠀⠀⡀⠀
⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⡀⠄⠠⢀⠈⢣⡀⠀⠁⠀⢀⡤⠊⠀⠀
⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⠎⠀⠀⠀⠘⡇⠀⢧⠀⠐⠊⠁⠀⠀⠀        AntiPhishing
⠀⢸⠳⣄⠀⠀⠀⠀⠀⠀⠀⠈⢺⠀⠀⠀⠀⠀⡇⠀⢸⠀⠀⠀⠀⢀⣀⣀⡀       By: AguuZzz
⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠠⠄⢀⡀⢇⠀⢸⡀⠀⡀⠀⠀⠀⠀⠀       Presione enter para continuar
⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⠀⠀⠀⠈⠙⠆⡼⠛⢦⡀⠑⠢⣄⠀⠀
⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⠢⣀⠀⢀⡴⡰⠁⠀⢀⡇⠀⠀⠈⠑⠀
⠀⠀⠀⢸⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠗⠒⠚⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡜⠀⠉⠢⢄⣀⠀⠀⠀⠀⠀⣀⡤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡇⠀⠀⠀⠀⣨⠟⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠂⠴⠒⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
input("")
cls()


#Link
link = input("Inserte el link aqui: ")
cls()

#Se inserta el "name=" del input
print('El campo es el valor de "name=": <input type="text" name="NAME">')  
campo = input("Inserte el nombre del campo usuario aqui: ")
cls()

campo2 = input("Inserte el nombre del campo contraseña aqui: ")
cls()


#Selecciona la cantidad de paquetes a enviar
cantidad = input("Cuantos paquetes desearia enviar?: ")
try: # Intenta transformrar la cantidad en un entero
    cantidad = int(cantidad)
    cls()
except ValueError:
    print("Seleccione un numero")
    time.sleep(1)
    exit()



def enviobucle():
    random_useragent = ua.random 
    randomusario = ''.join(random.choice(string.ascii_letters) for i in range(8))
    randomcontra = ''.join(random.choice(string.ascii_letters) for i in range(8))

    data = {
        campo: randomusario,
        campo2: randomcontra,
    }

    headers = {"user-agent": random_useragent}
    envio = requests.post(link, headers=headers, data=data)

    if envio.status_code == 200:
        print("Formulario enviado")
        print(f"Usuario: {randomusario}")
        print(f"Contraseña: {randomcontra}")
        print(f"Header (User-Agent: {random_useragent}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("Hubo un error al enviar el paquete")
    

i = 1
while i <= cantidad: 
    enviobucle()
    time.sleep(1)
    i += 1 

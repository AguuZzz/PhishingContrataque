import requests
import random
import time
import os 
import string

#Inicio
os.system('cls' if os.name == 'nt' else 'clear')
print("Contraataque phishing")
time.sleep(1)
print("by AguuZzz ")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')


#Link
link = input("Inserte el link aqui: ")
os.system('cls' if os.name == 'nt' else 'clear')


#Se inserta el "name=" del input
print('El campo es el valor de "name=": <input type="text" name="NAME">')  
campo = input("Inserte el nombre del campo usuario aqui: ")
os.system('cls' if os.name == 'nt' else 'clear')

campo2 = input("Inserte el nombre del campo contraseña aqui: ")
os.system('cls' if os.name == 'nt' else 'clear')


#Selecciona la cantidad de paquetes a enviar
cantidad = int(input("Cuantos paquetes desearia enviar?: "))
os.system('cls' if os.name == 'nt' else 'clear')



def enviobucle():
    randomusario = ''.join(random.choice(string.ascii_letters) for i in range(8))
    randomcontra = ''.join(random.choice(string.ascii_letters) for i in range(8))

    data = {
        campo: randomusario,
        campo2: randomcontra,
    }


    envio = requests.post(link, data=data)

    if envio.status_code == 200:
        print("Formulario enviado")
        print(f"Usuario: {randomusario}")
        print(f"Contraseña: {randomcontra}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("Hubo un error al enviar el paquete")
    

i = 1
while i <= cantidad: 
    enviobucle()
    time.sleep(1)
    i += 1 
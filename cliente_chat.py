#Ejercicio realizado por Laura Díaz, Carla de León y Carolina Bertoncini
#CLIENTE

import socket

IP = "10.0.2.15"
PORT = 8094

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((IP, PORT))
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Ha entrado usted en el chat")
    conversacion = True
    while conversacion:
        mensaje = input(">>")
        mensaje = str.encode(mensaje)
        cliente.send(mensaje)
        print(cliente.recv(1000).decode("utf-8"))
        if mensaje.lower() == "salir":
            print("El chat se ha cerrado")
            cliente.close()
            servidor.close()


except KeyboardInterrupt:
    cliente.close()
    print("Ha surgido un problema, cierre del programa")

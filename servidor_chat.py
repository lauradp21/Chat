#Ejercicio realizado por Laura Díaz, Carla de León y Carolina Bertoncini
#SERVIDOR

import socket

PORT = 8094
IP = "10.0.2.15"
MAX_OPEN_REQUESTS = 5

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    servidor.bind((IP, PORT))
    servidor.listen(MAX_OPEN_REQUESTS)
    print("Esperando conexion en {IP},{PORT}".format(IP = IP, PORT = PORT))
    (cliente, direccion) = servidor.accept()
    print("Alguien se ha conectado al chat")
    conversacion = True
    while conversacion:
        print(cliente.recv(1000).decode("utf-8"))
        mensaje = input(">>")
        mensaje = str.encode(mensaje)
        cliente.send(mensaje)
        if mensaje == "salir":
            print("El chat se ha cerrado")
            servidor.close()
            cliente.close()
            


except KeyboardInterrupt:
    cliente.close()
    servidor.close()
    print("Ha surgido un problema, cierre del programa")

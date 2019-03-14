#Hecho por Carolina Bertoncini, Laura Diaz y Carla de Leon
import socket
IP = '127.0.0.1'
PUERTO = 8083
num_respuestas = 2

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    servidor.bind((IP, PUERTO))
    servidor.listen(num_respuestas)
    print('Esperando conexion en {ip},{puerto}'.format(ip = IP, puerto = PUERTO))
    (cliente, direccion) = servidor.accept()
    print('Se ha conectado alguien')
    c_abierta = True
    while c_abierta:
        opcion=cliente.recv(1000).decode('utf-8')
        numero=opcion.split(" ")
        if numero[0]== "0":
            msg = ("Cerrando la calculadora...")

            msg = str.encode(msg)
            cliente.send(msg)

        elif numero[0]== "1":
            msg=int(numero[1]) + int(numero[2])
            msg=str(msg)
            msg = str.encode(msg)
            cliente.send(msg)
        elif numero[0]=="2":
            msg= int(numero[1]) * int(numero[2])
            msg=str(msg)
            msg = str.encode(msg)
            cliente.send(msg)
        else:
            print("inserte una opcion válida")

        c_abierta = False

except KeyboardInterrupt:
    cliente.close()
    print('Cerrando la calculadora...')

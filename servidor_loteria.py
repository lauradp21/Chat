import socket
import random

PORT = 8081
IP = "10.108.33.36"
MAX_OPEN_REQUESTS = 5

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((IP, PORT))
servidor.listen(MAX_OPEN_REQUESTS)
(cliente, direccion) = servidor.accept()
try:

    def process_client(cliente):
        numero = random.randint(0, 9)
        print('Esperando conexion en {IP},{PORT}'.format(IP = IP, PORT = PORT))
        #Voy a coger el IP del cliente
        ip = cliente.getpeername()
        ip = ip.split(".")
        suma = 0
        for i in ip:
            i = int(i)
            suma += i
        resto = suma % 10
        if resto == numero:
            print("TE HA TOCADO. EL NUMERO ERA: ", resto)
        else:
            print("NO TE HA TOCADO. TU NUMERO ERA: ", resto)
        cliente.close()

    process_client(cliente)


except socket.error:
    print("Ha habido un problema en el servidor")
    cliente.close()
    servidor.close()

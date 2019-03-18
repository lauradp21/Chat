import socket

IP = "10.108.33.36"
PORT = 8081

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((IP, PORT))
    print("conexión establecida")
    print(cliente.recv(2048).decode("utf-8"))
except KeyboardInterrupt:

    cliente.close()
    print("Usted salio")

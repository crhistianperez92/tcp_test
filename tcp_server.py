import socket
import threading

# Configuración del servidor
HOST = 'localhost'  # Dirección IP local o host
PORT = 5001        # Puerto del servidor


# Función para manejar cada cliente en un hilo separado
def handle_client(client_socket, address):
    print(f"Cliente conectado desde {address}")
    try:
        while True:
            # Recibir datos del cliente
            message = client_socket.recv(1024).decode().upper()
            if not message:
                break

            print(f"Mensaje de {address}: {message}")

            # Desconectar al cliente si envía "desconectar"
            if message == "DESCONEXION":
                print(f"Cliente {address} desconectado.")
                break

            # Responder al cliente (opcional)
            client_socket.send(message.encode('utf-8'))
    except ConnectionResetError:
        print(f"Cliente {address} se ha desconectado abruptamente.")
    finally:
        client_socket.close()
        print(f"Conexión con {address} cerrada.")


# Configuración y ejecución del servidor
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Servidor TCP escuchando en {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        # Crear un hilo para cada cliente conectado
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()


if __name__ == "__main__":
    start_server()
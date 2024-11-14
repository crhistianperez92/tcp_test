import socket


class ClientTCP:
    client = None
    
    def __init__(self, host='localhost', port=8000):
        try:
            # Crear objeto socket
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Conectar al servidor
            self.client.connect((host, port))

        except socket.error as e:
            print(f"No se pudo conectar al servidor: {e}")

    def sent_message(self, message):
        # Enviar datos al servidor
        self.client.send(message.encode())
        
        try:
            # Recibir respuesta del servidor
            respuesta = self.client.recv(1024)
            print(f"Respuesta del servidor: {respuesta.decode()}")
            return True
        except socket.error as e:
            return False

    def close_client(self):
        # Cerrar conexión
        self.client.close()

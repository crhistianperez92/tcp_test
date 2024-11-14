# Proyecto TCP Server y Cliente

Este proyecto incluye dos scripts de Python:
- `tcp_server.py`: Actúa como el servidor TCP, escuchando conexiones y manejando la comunicación con los clientes.
- `tcp_client.py`: Es la clase de para el Cliente de TCP, enviando mensajes al server.
- `main.py`: Actúa como el cliente TCP, conectándose al servidor y enviando mensajes.

## Prerrequisitos

Asegúrate de tener instalado:
- **Python 3.10** o superior.

## Instrucciones para Ejecutar

1. **Clonar el repositorio o descargar los archivos**:

   ```bash
   git https://github.com/crhistianperez92/tcp_test.git
   cd tcp_test

2. **Ejecutar el Server**
    
    Abre una terminal y corre el archivo tcp_server.py para iniciar el servidor:

    ```bash
    python tcp_server.py


3. **Ejecutar el Server**

    Abre otra terminal (mientras el servidor está en ejecución) y corre el archivo main.py para iniciar el cliente:

    ```bash
    python main.py


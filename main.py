from tcp_client import ClientTCP

client = ClientTCP(host='127.0.0.1', port=5001)

flag_close = True


while flag_close:
    print("Desea enviar un mensaje al servidor???")
    message = input()

    if message.lower() == 'cerrar':
        flag_close = False

    exito = client.sent_message(message)

    if not exito:
        print("La conexión ha finalizado desea volver a abrir la conexion (Si). o No para cerrar")
        message = input()
        if message.lower() == 'si':
            client = ClientTCP(host='127.0.0.1', port=5001)
        else:
            flag_close = False

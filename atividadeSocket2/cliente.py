import socket

def main():
    server_ip = "127.0.0.1"  # IP do servidor
    server_port = 12345  # Porta do servidor

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        response = client_socket.recv(1024).decode()
        print(response)

        if "Informe sua matrícula" in response:
            matricula = input()
            client_socket.send(matricula.encode())
        elif "Informe sua senha" in response:
            senha = input()
            client_socket.send(senha.encode())
        elif "Sua resposta" in response:
            resposta = input()
            client_socket.send(resposta.encode())
        elif "Total de questões corretas" in response:
            break

    client_socket.close()

if __name__ == "__main__":
    main()

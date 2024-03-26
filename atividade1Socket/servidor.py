import socket
import os

def handle_request(client_socket, client_address, base_path):
    # Recebe a requisição do cliente
    data = client_socket.recv(1024)
    request = data.decode().splitlines()[0].split()[1]
    
    # Monta o caminho completo do arquivo solicitado
    file_path = os.path.join(base_path, request.lstrip('/'))

    # Verifica se o arquivo existe e retorna o conteúdo
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
            response = file.read()
            client_socket.send(b"HTTP/1.1 200 OK\n\n" + response)
    else:
        error_message = b"HTTP/1.1 404 Not Found\n\n<h1>404 Not Found</h1>"
        client_socket.send(error_message)

    client_socket.close()

def start_server(port, base_path):
    # Cria o socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Servidor iniciado na porta {port}")

    while True:
        # Aguarda por conexões de clientes
        client_socket, client_address = server_socket.accept()
        print(f"Conexão recebida de {client_address}")
        
        # Lida com a requisição do cliente em uma thread separada
        handle_request(client_socket, client_address, base_path)

if __name__ == "__main__":
    # Configurações do servidor (porta e diretório base)
    porta = int(input("Digite a porta do servidor: "))
    diretorio_base = input("Digite o caminho do diretório base: ")

    start_server(porta, diretorio_base)

import socket

# Lista de questões e respostas corretas
QUESTIONS = [
    {"question": "Qual é a capital do Brasil?", "options": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], "correct_answer": "Brasília"},
    {"question": "Quem pintou a Mona Lisa?", "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"], "correct_answer": "Leonardo da Vinci"},
    {"question": "Qual é o maior planeta do Sistema Solar?", "options": ["Terra", "Saturno", "Júpiter", "Plutão"], "correct_answer": "Júpiter"},
    {"question": "Quem escreveu Noites Brancas?", "options": ["Machado de Assis", "Fiódor Dostoiévski", "Liev Tolstói", "Virginia Woolf"], "correct_answer": "Fiódor Dostoiévski"},
    {"question": "Qual cidade brasileira é conhecida como a Terra da Garoa?", "options": ["São Paulo", "Videira", "Brasília", "Teresina"], "correct_answer": "São Paulo"}
]

# Lista de alunos e senhas
USERS = {"12345": "senha123", "54321": "123456"}

def handle_client(client_socket):
    # Autenticação do aluno
    client_socket.send("Informe sua matrícula: ".encode())
    matricula = client_socket.recv(1024).decode().strip()
    client_socket.send("Informe sua senha: ".encode())
    senha = client_socket.recv(1024).decode().strip()

    if matricula in USERS and USERS[matricula] == senha:
        client_socket.send("Autenticação bem-sucedida!\n".encode())
        total_questions = len(QUESTIONS)
        questions_answered = 0
        correct_answers = 0

        for question_data in QUESTIONS:
            question = question_data["question"]
            options = "\n".join(f"{i+1}. {option}" for i, option in enumerate(question_data["options"]))
            correct_answer = question_data["correct_answer"]

            client_socket.send(f"\n{question}\n{options}\n".encode())
            client_socket.send("Sua resposta: ".encode())
            answer = client_socket.recv(1024).decode().strip()

            print(f"Resposta do aluno: {answer.lower()} - Resposta correta: {correct_answer.lower()}")  # Debug
            questions_answered += 1
            if answer.lower() == correct_answer.lower():  # Convertendo as respostas para minúsculas para comparação
                correct_answers += 1

        client_socket.send(f"\nTotal de questões respondidas: {questions_answered}\n".encode())
        client_socket.send(f"Total de questões corretas: {correct_answers}\n".encode())
    else:
        client_socket.send("Matrícula ou senha incorretas. Conexão encerrada.\n".encode())

    client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor iniciado em {host}:{port}")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Conexão estabelecida com {client_addr[0]}:{client_addr[1]}")
        handle_client(client_socket)

if __name__ == "__main__":
    HOST = "127.0.0.1"  # IP do servidor
    PORT = 12345  # Porta a ser utilizada
    start_server(HOST, PORT)

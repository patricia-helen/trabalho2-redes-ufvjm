"""
Trabalho 2 de Redes de Computadores 2 - Exercício 1
Integrantes: 
- Patrícia Helen Ribeiro Moreira
"""
import argparse
import socket
import threading
from datetime import datetime

def handle_client(conn, addr):
    """Lida com a comunicação de um cliente específico em uma thread."""
    try:
        while True:
            # Recebe a mensagem do cliente
            data = conn.recv(1024)
            if not data: # Se não receber dados, o cliente desconectou
                break
            
            mensagem = data.decode('utf-8')
            agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Imprime no console (Data/Hora e IP:Porta)
            print(f"[{agora}] {addr[0]}:{addr[1]} enviou: {mensagem}")
            
            # Responde com a confirmação
            resposta = "Mensagem recebida"
            conn.sendall(resposta.encode('utf-8'))
            
    except Exception as e:
        print(f"[ERRO] Erro na conexão com {addr}: {e}")
    finally:
        # Encerramento seguro da conexão
        conn.close()
        print(f"[DESCONECTADO] Cliente {addr} encerrou a conexão.")

def start_server(host, port):
    # Cria o socket IPv4 (AF_INET) TCP (SOCK_STREAM)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Permite o reuso da porta
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((host, port))
        server.listen()
        print(f"[SERVIDOR INICIADO] Escutando em {host}:{port}")
        
        while True:
            # Aceita novas conexões
            conn, addr = server.accept()
            print(f"[NOVA CONEXÃO] Cliente conectado: {addr}")
            
            # Cria e inicia uma nova thread para o cliente conectado
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\n[ENCERRANDO] Servidor finalizado pelo usuário (Ctrl+C).")
    finally:
        # Garante a liberação do recurso do servidor
        server.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor TCP")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="IP do servidor")
    parser.add_argument("--port", type=int, default=5000, help="Porta do servidor")
    args = parser.parse_args()

    start_server(args.host, args.port)
"""
Trabalho 2 de Redes de Computadores 2 - Exercício 3
Integrantes:
- Patrícia Helen Ribeiro Moreira
"""
import argparse
import socket
import threading
from datetime import datetime

# Dicionário global que mapeia {socket_cliente: nickname}
clientes_conectados = {}
# Trava (Mutex) para evitar conflitos quando múltiplas threads acessam o dicionário
clientes_lock = threading.Lock()


def broadcast(mensagem, remetente_conn=None):
    """Envia uma mensagem para todos os clientes conectados, exceto o remetente."""
    dados = mensagem.encode('utf-8')
    with clientes_lock:
        # Iteramos sobre uma cópia das chaves para evitar erro caso alguém saia durante o envio
        for conn in list(clientes_conectados.keys()):
            if conn != remetente_conn:
                try:
                    conn.sendall(dados)
                except Exception:
                    # Se o envio falhar, a desconexão será tratada pela thread daquele cliente
                    pass


def handle_client(conn, addr):
    """Gerencia a entrada, troca de mensagens e saída de um cliente em uma thread."""
    nickname = None
    try:
        # 1. A primeira mensagem enviada pelo cliente deve ser o seu nickname
        dados_nick = conn.recv(1024)
        if not dados_nick:
            return
        nickname = dados_nick.decode('utf-8').strip()

        # Registra o cliente na sala de forma segura
        with clientes_lock:
            clientes_conectados[conn] = nickname

        agora = datetime.now().strftime("%H:%M:%S")
        print(f"[{agora}] {nickname} ({addr[0]}:{addr[1]}) entrou no chat.")
        broadcast(f"[SISTEMA] {nickname} entrou na sala!", remetente_conn=conn)

        # 2. Loop contínuo para receber e retransmitir mensagens
        while True:
            data = conn.recv(1024)
            if not data:
                break

            mensagem = data.decode('utf-8').strip()
            if mensagem.lower() == 'sair':
                break

            agora = datetime.now().strftime("%H:%M:%S")
            print(f"[{agora}] [{nickname}]: {mensagem}")
            broadcast(f"[{nickname}]: {mensagem}", remetente_conn=conn)

    except Exception as e:
        print(f"[ERRO] Falha na comunicação com {addr}: {e}")
    finally:
        # 3. Remove o cliente da sala e avisa os demais sem derrubar o servidor
        with clientes_lock:
            if conn in clientes_conectados:
                del clientes_conectados[conn]

        conn.close()
        if nickname:
            agora = datetime.now().strftime("%H:%M:%S")
            print(f"[{agora}] {nickname} ({addr[0]}:{addr[1]}) saiu do chat.")
            broadcast(f"[SISTEMA] {nickname} saiu da sala.", remetente_conn=conn)


def start_server(host, port):
    """Inicializa o servidor TCP central do chat."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((host, port))
        server.listen()
        print(f"[SERVIDOR DE CHAT INICIADO] Escutando em {host}:{port}")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()

    except KeyboardInterrupt:
        print("\n[ENCERRANDO] Servidor de chat finalizado pelo usuário (Ctrl+C).")
    finally:
        with clientes_lock:
            for conn in list(clientes_conectados.keys()):
                conn.close()
            clientes_conectados.clear()
        server.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor de Chat TCP Multithread")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="IP de escuta do servidor")
    parser.add_argument("--port", type=int, default=7000, help="Porta TCP do servidor")
    args = parser.parse_args()

    start_server(args.host, args.port)
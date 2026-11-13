"""
Trabalho 2 de Redes de Computadores 2 - Exercício 4
Integrantes:
- Patrícia Helen Ribeiro Moreira
"""
import argparse
import socket
import threading
from datetime import datetime

# Variável compartilhada entre todas as threads para contar clientes atendidos
contador_atendimentos = 0
# Trava (Mutex) para garantir acesso thread-safe ao contador
contador_lock = threading.Lock()


def handle_client(conn, addr):
    """Atende a solicitação de hora de um cliente em uma thread dedicada."""
    global contador_atendimentos
    try:
        # Aguarda a solicitação enviada pelo cliente
        data = conn.recv(1024)
        if not data:
            return

        solicitacao = data.decode('utf-8').strip()

        # Região crítica: incrementa e lê o contador de forma atômica
        with contador_lock:
            contador_atendimentos += 1
            atendimento_atual = contador_atendimentos

        agora = datetime.now()
        timestamp_log = agora.strftime("%Y-%m-%d %H:%M:%S")
        hora_resposta = agora.strftime("%H:%M:%S")

        # Registra a solicitação recebida e atendida com data/hora, cliente e contador
        print(
            f"[{timestamp_log}] [Atendimentos: {atendimento_atual}] "
            f"Cliente {addr[0]}:{addr[1]} solicitou '{solicitacao}' -> Hora enviada: {hora_resposta}"
        )

        # Envia a hora atual no formato HH:MM:SS para o cliente
        conn.sendall(hora_resposta.encode('utf-8'))

    except ConnectionResetError:
        print(f"[AVISO] O cliente {addr[0]}:{addr[1]} encerrou a conexão abruptamente.")
    except Exception as e:
        print(f"[ERRO] Falha ao atender cliente {addr[0]}:{addr[1]}: {e}")
    finally:
        # Garante o fechamento seguro do socket deste cliente sem afetar o servidor
        conn.close()


def start_server(host, port):
    """Inicializa o servidor de hora TCP multithread."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((host, port))
        server.listen()
        print(f"[SERVIDOR DE HORA INICIADO] Escutando em {host}:{port}")

        while True:
            conn, addr = server.accept()
            # Dispara uma thread independente para atender cada cliente em paralelo
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()

    except KeyboardInterrupt:
        print("\n[ENCERRANDO] Servidor de hora finalizado pelo usuário (Ctrl+C).")
    finally:
        server.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor de Hora TCP Multithread")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="IP de escuta do servidor")
    parser.add_argument("--port", type=int, default=7000, help="Porta TCP do servidor")
    args = parser.parse_args()

    start_server(args.host, args.port)
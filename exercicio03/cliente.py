"""
Trabalho 2 de Redes de Computadores 2 - Exercício 3
Integrantes:
- Patrícia Helen Ribeiro Moreira
"""
import argparse
import socket
import sys
import threading


def receber_mensagens(client_socket):
    """Thread dedicada a escutar continuamente mensagens enviadas pelo servidor."""
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("\n[SISTEMA] Conexão encerrada pelo servidor.")
                break

            mensagem = data.decode('utf-8')
            # O '\r' limpa a linha atual 'Você: ' para exibir a mensagem recebida sem bagunçar o terminal
            print(f"\r{mensagem}\nVocê: ", end="", flush=True)
        except Exception:
            # Ocorre normalmente quando o cliente fecha o socket ao digitar 'sair'
            break


def start_client(host, port):
    """Conecta ao servidor de chat e gerencia o envio de mensagens."""
    # Solicita um nickname válido antes de abrir a conexão
    nickname = ""
    while not nickname:
        nickname = input("Digite seu nickname para entrar no chat: ").strip()
        if not nickname:
            print("[AVISO] O nickname não pode ser vazio.")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))
        # Envia o nickname como primeira mensagem de identificação
        client.sendall(nickname.encode('utf-8'))

        print(f"\nConectado ao chat em {host}:{port} como '{nickname}'.")
        print("Digite suas mensagens e pressione Enter. Digite 'sair' para encerrar.\n")

        # Inicia a thread de recebimento paralelo (daemon=True encerra junto com o programa principal)
        thread_leitura = threading.Thread(target=receber_mensagens, args=(client,), daemon=True)
        thread_leitura.start()

        # Thread principal fica dedicada apenas à leitura do teclado e envio
        while True:
            mensagem = input("Você: ").strip()

            if not mensagem:
                continue

            if mensagem.lower() == 'sair':
                client.sendall("sair".encode('utf-8'))
                print("Saindo da sala de chat...")
                break

            client.sendall(mensagem.encode('utf-8'))

    except ConnectionRefusedError:
        print(f"[ERRO] Não foi possível conectar. Servidor indisponível em {host}:{port}.")
    except KeyboardInterrupt:
        print("\nSaindo da sala de chat...")
    except Exception as e:
        print(f"[ERRO] Falha na conexão: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente de Chat TCP")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="IP do servidor de chat")
    parser.add_argument("--port", type=int, default=7000, help="Porta TCP do servidor")
    args = parser.parse_args()

    start_client(args.host, args.port)
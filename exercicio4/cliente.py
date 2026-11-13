"""
Trabalho 2 de Redes de Computadores 2 - Exercício 4
Integrantes:
- Patrícia Helen Ribeiro Moreira
"""
import argparse
import socket


def solicitar_hora(host, port):
    """Conecta ao servidor de hora, envia uma requisição e exibe a resposta."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5.0)

    try:
        client.connect((host, port))
        # Envia a solicitação de hora ao servidor
        client.sendall("GET_TIME".encode('utf-8'))

        # Recebe a resposta no formato HH:MM:SS
        data = client.recv(1024)
        if not data:
            print("[AVISO] O servidor encerrou a conexão sem enviar dados.")
            return

        hora_recebida = data.decode('utf-8').strip()
        print(f"Hora atual recebida do servidor ({host}:{port}): {hora_recebida}")

    except ConnectionRefusedError:
        print(f"[ERRO] Conexão recusada. O servidor em {host}:{port} está indisponível.")
    except socket.timeout:
        print("[ERRO] Tempo limite excedido ao aguardar resposta do servidor.")
    except Exception as e:
        print(f"[ERRO] Falha na comunicação com o servidor: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente de Hora TCP")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="IP do servidor de hora")
    parser.add_argument("--port", type=int, default=7000, help="Porta TCP do servidor")
    args = parser.parse_args()

    solicitar_hora(args.host, args.port)
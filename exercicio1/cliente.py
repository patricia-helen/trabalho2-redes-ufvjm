"""
Trabalho 2 de Redes de Computadores 2 - Exercício 1
Integrantes: 
- Patrícia Helen Ribeiro Moreira
"""
import argparse
import socket
import sys

def start_client(host, port):
    # Criação do socket do cliente
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Tenta conectar ao servidor
        client.connect((host, port))
        print(f"Conectado ao servidor {host}:{port}")
        print("Digite suas mensagens. Digite 'sair' para encerrar.")
        
        while True:
            # Entrada do usuário
            mensagem = input("\nVocê: ").strip() # .strip() remove espaços vazios nas pontas
            
            # Validação para mensagens vazias
            if not mensagem:
                print("[AVISO] A mensagem não pode ser vazia. Tente novamente.")
                continue
                
            # Condição de saída
            if mensagem.lower() == 'sair':
                print("Encerrando o cliente...")
                break
                
            # Envia a mensagem convertida em bytes
            client.sendall(mensagem.encode('utf-8'))
            
            # Aguarda e exibe a resposta do servidor
            resposta = client.recv(1024)
            print(f"Servidor: {resposta.decode('utf-8')}")
            
    except ConnectionRefusedError:
        # Tratamento de exceção caso o servidor esteja offline
        print(f"[ERRO] Conexão recusada. O servidor no endereço {host}:{port} está indisponível.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro inesperado: {e}")
    finally:
        # Garante que o socket do cliente sempre será fechado
        client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente TCP")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="IP do servidor")
    parser.add_argument("--port", type=int, default=5000, help="Porta do servidor")
    args = parser.parse_args()

    start_client(args.host, args.port)
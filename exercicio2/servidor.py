"""
Trabalho 2 de Redes de Computadores 2 - Exercício 2
Integrantes: 
- Patrícia Helen Ribeiro Moreira
"""
import argparse
import socket
from datetime import datetime

def start_server(host, port):
    # Cria o socket UDP (SOCK_DGRAM)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    
    print(f"[SERVIDOR UDP INICIADO] Escutando pacotes em {host}:{port}")
    
    try:
        while True:
            # O servidor UDP bloqueia no recvfrom esperando qualquer datagrama.
            # 65507 é o tamanho máximo de payload do UDP sobre IPv4.
            data, addr = server.recvfrom(65507)
            
            mensagem = data.decode('utf-8')
            agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"[{agora}] Recebido de {addr[0]}:{addr[1]} -> {mensagem}")
            
            # Echo: devolve os mesmos dados para o endereço de origem
            server.sendto(data, addr)
            
    except KeyboardInterrupt:
        print("\n[ENCERRANDO] Servidor UDP finalizado (Ctrl+C).")
    finally:
        server.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor UDP Echo")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="IP do servidor")
    parser.add_argument("--port", type=int, default=6000, help="Porta do servidor")
    args = parser.parse_args()

    start_server(args.host, args.port)
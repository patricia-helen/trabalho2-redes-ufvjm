"""
Trabalho 2 de Redes de Computadores 2 - Exercício 2
Integrantes: 
- Patrícia Helen Ribeiro Moreira
"""
import argparse
import socket

# Constante teórica máxima (65535 total - 20 cabeçalho IP - 8 cabeçalho UDP)
MAX_UDP_PAYLOAD = 65507

def start_client(host, port):
    # Cria o socket UDP (SOCK_DGRAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # REQUISITO: Timeout de 3 segundos para evitar bloqueio infinito se o pacote for perdido
    client.settimeout(3.0)
    
    print(f"Cliente UDP iniciado. Servidor alvo: {host}:{port}")
    print("Digite suas mensagens. Digite 'sair' para encerrar.")
    
    try:
        while True:
            mensagem = input("\nVocê: ").strip()
            
            if not mensagem:
                print("[AVISO] A mensagem não pode ser vazia.")
                continue
                
            if mensagem.lower() == 'sair':
                print("Encerrando o cliente...")
                break
                
            # Codifica a mensagem em bytes
            dados = mensagem.encode('utf-8')
            
            # REQUISITO: Validação de tamanho máximo
            tamanho = len(dados)
            if tamanho > MAX_UDP_PAYLOAD:
                print(f"[ERRO] A mensagem excede o limite do UDP ({tamanho} > {MAX_UDP_PAYLOAD} bytes).")
                continue
            
            # Envia o datagrama direto ao destino (sem connect prévio)
            client.sendto(dados, (host, port))
            
            try:
                # Aguarda o eco do servidor
                resposta, addr = client.recvfrom(MAX_UDP_PAYLOAD)
                print(f"Servidor (Echo): {resposta.decode('utf-8')}")
            except socket.timeout:
                # REQUISITO: Tratamento de erro de tempo limite
                print("[ERRO] Tempo limite de resposta atingido. O pacote foi perdido ou o servidor está offline.")
            
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro inesperado: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente UDP Echo")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="IP do servidor alvo")
    parser.add_argument("--port", type=int, default=6000, help="Porta do servidor alvo")
    args = parser.parse_args()

    start_client(args.host, args.port)
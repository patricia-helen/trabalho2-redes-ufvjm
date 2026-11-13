"""
Trabalho 2 de Redes de Computadores 2 - Exercício 10
Integrantes:
- Patrícia Helen Ribeiro Moreira
"""
import asyncio
import websockets
import json

# Conjunto para rastrear todos os clientes conectados simultaneamente
clientes_conectados = set()

async def chat_handler(websocket):
    """Gerencia a conexão de um cliente específico de forma assíncrona."""
    clientes_conectados.add(websocket)
    username = "Desconhecido"
    
    try:
        # Loop assíncrono para escutar mensagens deste cliente
        async for message in websocket:
            dados = json.loads(message)
            
            if dados.get("tipo") == "login":
                username = dados.get("username")
                msg_sistema = json.dumps({"tipo": "sistema", "mensagem": f"{username} entrou na sala."})
                # Retransmite (broadcast) para todos os clientes
                websockets.broadcast(clientes_conectados, msg_sistema)
                print(f"[SISTEMA] {username} conectou.")
                
            elif dados.get("tipo") == "mensagem":
                texto = dados.get("mensagem")
                msg_chat = json.dumps({"tipo": "chat", "username": username, "mensagem": texto})
                websockets.broadcast(clientes_conectados, msg_chat)
                print(f"[{username}]: {texto}")
                
    except websockets.exceptions.ConnectionClosed:
        # Erro esperado quando o navegador fecha abruptamente
        pass
    except Exception as e:
        print(f"[ERRO] Falha com cliente {username}: {e}")
    finally:
        # REQUISITO: Tratar desconexões inesperadas sem derrubar o servidor
        clientes_conectados.remove(websocket)
        msg_sistema = json.dumps({"tipo": "sistema", "mensagem": f"{username} saiu da sala."})
        websockets.broadcast(clientes_conectados, msg_sistema)
        print(f"[SISTEMA] {username} desconectou.")

async def main():
    print("[SERVIDOR WEBSOCKET INICIADO] Escutando em ws://127.0.0.1:8765")
    # Inicia o servidor na porta exigida pelo edital (8765)
    async with websockets.serve(chat_handler, "127.0.0.1", 8765):
        await asyncio.Future()  # Mantém o servidor rodando para sempre

if __name__ == "__main__":
    asyncio.run(main())
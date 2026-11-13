# Exercício 10: Chat em Rede com WebSockets

## Integrantes
- Patrícia Helen Ribeiro Moreira

## Descrição
Sistema de chat em tempo real que demonstra o protocolo WebSockets. O servidor foi implementado em Python utilizando a biblioteca `websockets` sob a arquitetura `asyncio` (assíncrona baseada em eventos), mantendo um conjunto atualizado de conexões. O cliente foi implementado utilizando a WebSocket API nativa do navegador (HTML/JavaScript), com comunicação estruturada via payloads JSON.

## Como executar
1. Abra um terminal dentro da pasta `exercicio10/` e certifique-se de ter instalado a biblioteca (`pip install websockets`).
2. Inicie o servidor:
   ~~~bash
   python3 servidor.py
   ~~~
3. Abra o arquivo `cliente.html` diretamente em **qualquer navegador web** (Chrome, Firefox, Edge).
   - Você pode abrir múltiplas abas do mesmo arquivo `cliente.html` para simular vários usuários (ex: Patricia, João, Maria) conversando entre si em tempo real.
   - Fechar a aba do navegador simula uma desconexão inesperada, que o servidor tratará graciosamente notificando os demais usuários.
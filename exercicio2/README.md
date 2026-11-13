# Exercício 2: Servidor Echo (UDP)

## Integrantes
- Patrícia Helen Ribeiro Moreira

## Descrição
Implementação de arquitetura cliente-servidor utilizando o protocolo UDP (`SOCK_DGRAM`). O servidor funciona como um serviço de eco puro. O cliente implementa restrições matemáticas de limite de pacote (máximo de 65.507 bytes no payload) e detecção de perda de pacotes via controle de `timeout`.

## Como executar
Abra dois terminais distintos dentro do diretório `exercicio2/`:

**1. No primeiro terminal, inicie o servidor:**
~~~bash
python3 servidor.py --host 127.0.0.1 --port 6000
~~~

**2. No segundo terminal, inicie o cliente:**
~~~bash
python3 cliente.py --host 127.0.0.1 --port 6000
~~~
*(Para testar o tratamento de timeout exigido, basta rodar o cliente com o servidor desligado. A mensagem enviada se perderá e o cliente emitirá o erro controlado após 3 segundos).*
# Exercício 4: Servidor de Hora com Threads (TCP)

## Integrantes
- Patrícia Helen Ribeiro Moreira

## Descrição
Servidor TCP multithread capaz de atender múltiplos clientes simultaneamente e retornar a hora atual do sistema no formato `HH:MM:SS`. Utiliza controle explícito de concorrência por meio de `threading.Lock` para manter um contador *thread-safe* do total de atendimentos realizados e registra logs detalhados de cada requisição.

## Dependências
- **Python 3.10 ou superior**
- Utiliza apenas módulos nativos da biblioteca padrão (`socket`, `threading`, `argparse` e `datetime`).

## Parâmetros de Execução
- `--host`: Endereço IPv4 do servidor (padrão: `127.0.0.1`).
- `--port`: Porta TCP de comunicação (padrão: `7000`).

## Como executar
Abra dois terminais distintos dentro do diretório `exercicio4/`:

**1. No primeiro terminal, inicie o servidor:**
~~~bash
python3 servidor.py --host 127.0.0.1 --port 7000
~~~

**2. No segundo terminal, execute o cliente para consultar a hora:**
~~~bash
python3 cliente.py --host 127.0.0.1 --port 7000
~~~

*(Para testar múltiplas requisições concorrentes simultâneas no Linux, execute no segundo terminal: `for i in {1..5}; do python3 cliente.py & done`)*
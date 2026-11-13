# Exercício 1: Cliente-Servidor TCP Multithread

## Integrantes
- Patrícia Helen Ribeiro Moreira

## Descrição
Implementação de uma arquitetura cliente-servidor utilizando o protocolo TCP (`SOCK_STREAM`), capaz de atender múltiplos clientes simultaneamente por meio de *threads* e registrar data, hora, IP e porta de origem de cada mensagem recebida.

## Dependências
- **Python 3.10 ou superior**
- Utiliza apenas bibliotecas nativas da linguagem (`socket`, `threading`, `argparse`, `datetime` e `sys`), não sendo necessária a instalação de pacotes externos via `pip`.

## Parâmetros de Execução
Ambos os scripts aceitam argumentos opcionais via linha de comando:
- `--host`: Endereço IPv4 do servidor (padrão: `127.0.0.1`).
- `--port`: Porta TCP de comunicação (padrão: `5000`).

## Como executar
Abra dois terminais distintos dentro do diretório `exercicio1/`:

**1. No primeiro terminal, inicie o servidor:**
```bash
python3 servidor.py --host 127.0.0.1 --port 5000
```

2. No segundo terminal, inicie o cliente:

```bash
python3 cliente.py --host 127.0.0.1 --port 5000
```

(Para testar múltiplos clientes simultâneos, abra novos terminais e repita o comando do cliente. Digite sair no cliente para encerrar a conexão de forma segura).


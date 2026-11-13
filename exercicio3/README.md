# Exercício 3: Chat em Rede (TCP)

## Integrantes
- Patrícia Helen Ribeiro Moreira

## Descrição
Sistema de chat em tempo real baseado na arquitetura cliente-servidor sobre protocolo TCP (`SOCK_STREAM`). O servidor central utiliza *threads* e travas de sincronização (`threading.Lock`) para gerenciar múltiplos usuários simultâneos e realizar *broadcast* de mensagens e notificações de entrada/saída. O cliente utiliza uma *thread* dedicada para recebimento contínuo em paralelo com a digitação do usuário.

## Dependências
- **Python 3.10 ou superior**
- Utiliza apenas módulos nativos da biblioteca padrão (`socket`, `threading`, `argparse`, `datetime` e `sys`).

## Parâmetros de Execução
- `--host`: Endereço IPv4 do servidor (padrão: `127.0.0.1`).
- `--port`: Porta TCP de comunicação (padrão: `7000`).

## Como executar
Para testar a troca de mensagens entre múltiplos participantes, abra **três terminais distintos** dentro do diretório `exercicio3/`:

**1. No primeiro terminal, inicie o servidor:**
~~~bash
python3 servidor.py --host 127.0.0.1 --port 7000
~~~

**2. No segundo terminal, conecte o primeiro cliente (ex.: Patricia):**
~~~bash
python3 cliente.py --host 127.0.0.1 --port 7000
~~~

**3. No terceiro terminal, conecte o segundo cliente (ex.: Joao):**
~~~bash
python3 cliente.py --host 127.0.0.1 --port 7000
~~~
*(Digite `sair` em qualquer cliente para desconectá-lo sem afetar o servidor ou os demais participantes).*
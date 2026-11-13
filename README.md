# Trabalho 2 de Redes de Computadores 2 - UFVJM

**Estudante:** Patrícia Helen Ribeiro Moreira  
**Instituição:** Universidade Federal dos Vales do Jequitinhonha e Mucuri (UFVJM)  
**Curso:** Sistemas de Informação   

Repositório oficial contendo a implementação prática de redes de computadores, englobando sockets de baixo nível (TCP/UDP), controle de concorrência com threads, análise de tráfego com Wireshark e comunicação em tempo real via WebSockets.

---

## 📋 Sumário dos Exercícios

| Pasta | Tópico Principal | Descrição Resumida |
| :--- | :--- | :--- |
| [`exercicio01/`](./exercicio01/) | **TCP Multithread** | Comunicação cliente-servidor TCP concorrente para múltiplos clientes. |
| [`exercicio02/`](./exercicio02/) | **UDP Echo & Timeout** | Servidor de eco UDP com validação de payload máximo (65.507 bytes) e tratamento de timeout. |
| [`exercicio03/`](./exercicio03/) | **Chat TCP (Broadcast)** | Sala de chat em tempo real com threads, sincronização por Mutex (`Lock`) e repasse de mensagens. |
| [`exercicio04/`](./exercicio04/) | **Servidor de Hora TCP** | Fornecimento concorrente de horário (`HH:MM:SS`) com contador de atendimentos thread-safe. |
| [`exercicio05/`](./exercicio05/) | **Tráfego HTTP** | Captura e análise de requisições/respostas HTTP via Wireshark (`.pcapng`). |
| [`exercicio06/`](./exercicio06/) | **Handshake TCP** | Análise dos pacotes de estabelecimento (*SYN, SYN-ACK, ACK*) e encerramento de sessão. |
| [`exercicio07/`](./exercicio07/) | **Resolução DNS** | Inspeção de consultas e respostas de mapeamento de nomes de domínio. |
| [`exercicio08/`](./exercicio08/) | **Tráfego ICMP (Ping)** | Mensuração de latência e Round Trip Time (RTT) em testes de conectividade. |
| [`exercicio09/`](./exercicio09/) | **Tráfego DHCP** | Captura do processo DORA (*Discover, Offer, Request, Acknowledge*) de alocação de IP. |
| [`exercicio10/`](./exercicio10/) | **WebSockets** | Chat bidirecional assíncrono em tempo real utilizando Python (`websockets` + `asyncio`) e HTML/JS. |

---

## 🛠️ Tecnologias e Ambiente
- **Linguagem:** Python 3.10+
- **Sistema Operacional:** Linux Ubuntu
- **Ferramentas de Rede:** Wireshark, Netcat / Telnet, cURL, Git & GitHub Flow

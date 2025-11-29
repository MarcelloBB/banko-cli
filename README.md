
# Banko — CLI de gerenciamento de fila para bancos

Banko é uma pequena ferramenta de linha de comando para simular e gerenciar filas de atendimento (com suporte a clientes preferenciais). Foi desenvolvida como um utilitário didático ou para uso simples em ambientes locais.

## Funcionalidades

- Adicionar clientes (normais ou preferenciais) com operação desejada.
- Atender o próximo cliente (prioridade para preferenciais).
- Ver o status atual das filas e o log do dia.
- Gerar um relatório simples com métricas (total de atendidos, tempo médio de espera, top operações).
- Resetar os dados (fila, atendidos e logs).

## Requisitos

- Python 3.10+
- Dependências: `click`, `tabulate` (estão listadas em `requirements.txt` e em `pyproject.toml`).

## Instalação

Recomenda-se criar e ativar um ambiente virtual antes de instalar:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale a aplicação em modo editável:

```bash
pip install -e .
```

Isso fornecerá o entry point `banko` (definido em `pyproject.toml`).

## Uso

Com o entry point instalado, use o comando `banko` seguido do subcomando.

Exemplos:

```bash
# Adiciona uma cliente preferencial
banko add "Maria" --preferencial --op "Abertura de conta"

# Atende o próximo cliente
banko next

# Mostra o status das filas e o log
banko status

# Gera um mini-relatório do dia
banko report

# Reseta todos os dados (com confirmação)
banko reset

# Força o reset sem perguntar
banko reset --force
```

Observações:
- O comando `add` aceita a opção `--preferencial` para marcar o cliente como preferencial e `--op` para descrever a operação.
- O comando `next` dá prioridade a clientes preferenciais.

## Persistência de dados

Os dados (filas, atendidos e log de eventos) são armazenados em JSON no arquivo:

```
~/.banko_queue.json
```

Esse arquivo é criado automaticamente pela aplicação e contém os estados serializados.

## Arquitetura (visão rápida)

- `banko/cli.py`: ponto central da CLI (Click) e registro dos subcomandos.
- `banko/commands/`: comandos disponíveis (`add`, `next`, `status`, `report`, `reset`).
- `banko/core/queue_manager.py`: lógica das filas (fila normal e preferencial + persistência).
- `banko/core/storage.py`: serialize/deserialize para `~/.banko_queue.json`.
- `banko/core/logger.py`: registro de eventos do dia.

## Desenvolvimento

Para desenvolver localmente, instale em modo editável conforme mostrado acima. Edite os arquivos em `banko/` e execute o CLI via:

```bash
banko <subcomando>
```

Para executar diretamente (sem instalar), você também pode rodar:

```bash
python -m banko
```

## Contribuições

Pull requests são bem-vindos. Abra uma issue antes de trabalhar em mudanças maiores para alinharmos o escopo.

## Licença

Escolha uma licença apropriada para o seu projeto (por exemplo, MIT). Este repositório não contém um arquivo de licença explícito por padrão.

import click
from datetime import datetime
from ..core.models import Cliente


@click.command(name="add")
@click.argument("nome")
@click.option("--preferencial", is_flag=True, help="Marca o cliente como preferencial")
@click.option("--op", default="Não informado", help="Operação desejada pelo cliente")
@click.pass_context
def cmd(ctx, nome, preferencial, op):
    """Adiciona um cliente na fila.
    Ex: bank add "Maria" --preferencial --op "Abertura de conta"
    """
    manager = ctx.obj["manager"]
    logger = ctx.obj["logger"]

    cliente = Cliente(
        nome=nome, preferencial=preferencial, chegada=datetime.now(), operacao=op
    )
    manager.adicionar_cliente(cliente)

    logger.registrar(
        f"Cliente {cliente.nome} ({'preferencial' if preferencial else 'normal'}) "
        f"entrou na fila - Operação: {op}"
    )

    click.echo(
        f"Cliente '{nome}' adicionado ({'preferencial' if preferencial else 'normal'}) Operação: {op}"
    )

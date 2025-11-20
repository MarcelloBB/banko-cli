import click
from datetime import datetime
from ..core.models import Cliente


@click.command(name="add")
@click.argument("nome")
@click.option("--preferencial", is_flag=True, help="Marca o cliente como preferencial")
@click.pass_context
def cmd(ctx, nome, preferencial):
    """Adiciona um cliente na fila.
    Ex: bank add "Maria" --preferencial
    """
    manager = ctx.obj["manager"]
    logger = ctx.obj["logger"]

    cliente = Cliente(nome=nome, preferencial=preferencial, chegada=datetime.now())
    manager.adicionar_cliente(cliente)
    logger.registrar(
        f"Cliente {cliente.nome} ({'preferencial' if cliente.preferencial else 'normal'}) entrou na fila"
    )
    click.echo(
        f"Cliente '{cliente.nome}' adicionado ({'preferencial' if cliente.preferencial else 'normal'})."
    )

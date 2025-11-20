import click


@click.command(name="next")
@click.pass_context
def cmd(ctx):
    """Atende o próximo cliente (preferencial tem prioridade)."""
    manager = ctx.obj["manager"]
    logger = ctx.obj["logger"]

    cliente = manager.proximo_cliente()
    if cliente is None:
        click.echo("Nenhum cliente na fila.")
        return

    logger.registrar(
        f"Cliente {cliente.nome} atendido ({'preferencial' if cliente.preferencial else 'normal'})"
    )
    click.echo(
        f"Atendendo: {cliente.nome} ({'preferencial' if cliente.preferencial else 'normal'})"
    )

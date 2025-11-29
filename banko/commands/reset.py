import click
from ..core.storage import save_data, _default_data


@click.command(name="reset")
@click.option("--force", is_flag=True, help="Não perguntar confirmação.")
def cmd(force):
    """
    Limpa toda a fila, clientes atendidos e logs.
    """

    if not force:
        confirmar = click.prompt(
            "Tem certeza que deseja limpar TUDO? (y/n)", default="n"
        )
        if confirmar.lower() not in ("y", "yes"):
            click.echo("Operação cancelada.")
            return

    data = _default_data()
    save_data(data)

    click.echo("Dados limpos com sucesso!")

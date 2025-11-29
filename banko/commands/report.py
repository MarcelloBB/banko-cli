import click
from tabulate import tabulate
from collections import Counter


@click.command(name="report")
@click.pass_context
def cmd(ctx):
    """Gera um mini-relatório do dia."""
    manager = ctx.obj["manager"]
    atendidos = manager.listar_atendidos()

    if not atendidos:
        click.echo("Nenhum cliente foi atendido ainda.")
        return

    tempos = [c.tempo_espera for c in atendidos if c.tempo_espera is not None]
    tempo_medio = sum(tempos) / len(tempos) if len(tempos) > 0 else 0

    ops = Counter([c.operacao for c in atendidos]).most_common(3)

    pref = sum(1 for c in atendidos if c.preferencial)
    norm = len(atendidos) - pref

    table = [
        ["Total de atendidos", len(atendidos)],
        ["Tempo médio de espera (s)", round(tempo_medio, 2)],
        ["Atendidos preferenciais", pref],
        ["Atendidos normais", norm],
    ]

    click.echo("\nBANKO - RELATÓRIO DE USO DIÁRIO")
    click.echo(tabulate(table, headers=["Métrica", "Valor"], tablefmt="fancy_grid"))

    click.echo("\nTop 3 operações:")
    for op, count in ops:
        click.echo(f" - {op}: {count} clientes")

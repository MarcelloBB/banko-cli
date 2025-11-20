import click


@click.command(name="status")
@click.pass_context
def cmd(ctx):
    """Mostra o status atual das filas e o log do dia."""
    manager = ctx.obj["manager"]
    logger = ctx.obj["logger"]

    pref = manager.listar_fila_preferencial()
    norm = manager.listar_fila_normal()
    atendidos = manager.listar_atendidos()

    click.echo("\nFila Preferencial:")
    if pref:
        for idx, c in enumerate(pref, 1):
            click.echo(f"  {idx}. {c.nome} (chegada: {c.chegada.strftime('%H:%M:%S')})")
    else:
        click.echo("  (vazia)")

    click.echo("\nFila Normal:")
    if norm:
        for idx, c in enumerate(norm, 1):
            click.echo(f"  {idx}. {c.nome} (chegada: {c.chegada.strftime('%H:%M:%S')})")
    else:
        click.echo("  (vazia)")

    click.echo("\nAtendidos (total: {})".format(len(atendidos)))
    if atendidos:
        for idx, c in enumerate(atendidos[-10:], 1):
            click.echo(f"  {idx}. {c.nome} (chegada: {c.chegada.strftime('%H:%M:%S')})")

    click.echo("\nLog do dia:")
    events = logger.listar()
    if events:
        for e in events[-20:]:
            click.echo(f"  {e}")
    else:
        click.echo("  (sem eventos)")

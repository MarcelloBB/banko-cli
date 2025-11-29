import click
from .commands import add, nxt, status, report, reset
from .core.queue_manager import QueueManager
from .core.logger import Logger

manager = QueueManager()
logger = Logger()


@click.group()
@click.version_option(version="0.1.0")
@click.pass_context
def cli(ctx):
    """Banko é um sistema de gerenciamento de filas para bancos e instituições similares.

    Use commands: add, next, status, report, reset.
    """

    ctx.obj = {
        "manager": manager,
        "logger": logger,
    }


cli.add_command(add.cmd)
cli.add_command(nxt.cmd)
cli.add_command(status.cmd)
cli.add_command(report.cmd)
cli.add_command(reset.cmd)

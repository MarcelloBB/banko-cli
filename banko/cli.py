import click
from .core.queue_manager import QueueManager
from .core.logger import Logger

# Create singletons for the running process
manager = QueueManager()
logger = Logger()


@click.group()
@click.version_option(version="0.1.0")
@click.pass_context
def cli(ctx):
    """Bank Queue Simulator CLI

    Use commands: add, next, status
    """
    # attach shared objects to context so commands can access them
    ctx.obj = {
        "manager": manager,
        "logger": logger,
    }


# Import commands and register them
from .commands import add, nxt, status  # noqa: E402,F401

cli.add_command(add.cmd)
cli.add_command(nxt.cmd)
cli.add_command(status.cmd)

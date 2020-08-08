"""Main app."""

from .routes import setup_routes

from aiohttp import web
from aiojobs.aiohttp import setup

from cleo import Command
from cleo import Application


async def setup_app(app):
    """Setup app async helpers."""
    app['meter_storage'] = []


class NotificationServerCommand(Command):
    """Starts server 

    start_server
        {--host=0.0.0.0 : Host to listen on}
        {--port=8081 : Port to listen on}
        {--config=config.ini : Config file}
        {--debug : Debug and verbose mode}
    """
    def handle(self):
        """Handle command."""
        app = web.Application()
        app.on_startup.append(setup_app)
        setup(app)
        setup_routes(app)
        web.run_app(app,
                    host=self.option('host'),
                    port=int(self.option('port')))


def main():
    """Main."""
    application = Application()
    application.add(NotificationServerCommand())
    application.run()

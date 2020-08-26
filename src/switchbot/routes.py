"""Routes."""
from .handlers import meter


def setup_routes(app):
    """Setup routes."""
    app.router.add_get('/latest', meter.latest)
    app.router.add_get('/all', meter.all)
    app.router.add_get('/start', meter.start)
    app.router.add_get('/', meter.index)

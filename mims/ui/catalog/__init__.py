from pathlib import Path

from flask import Flask

from mims.config import config
from mims.ui.catalog import views
from odp.const import ODPScope
from odp.const.hydra import HydraScope
from odp.ui import base


def create_app():
    """
    Flask application factory.
    """
    app = Flask(__name__)
    app.config.update(
        UI_CLIENT_ID=config.MIMS.CATALOG.UI_CLIENT_ID,
        UI_CLIENT_SECRET=config.MIMS.CATALOG.UI_CLIENT_SECRET,
        UI_CLIENT_SCOPE=[
            HydraScope.OPENID,
            HydraScope.OFFLINE_ACCESS,
            ODPScope.CATALOG_READ,
            ODPScope.TOKEN_READ,
        ],
        SI_CLIENT_ID=config.MIMS.CATALOG.SI_CLIENT_ID,
        SI_CLIENT_SECRET=config.MIMS.CATALOG.SI_CLIENT_SECRET,
        SI_CLIENT_SCOPE=[
            ODPScope.CATALOG_READ,
        ],
        SECRET_KEY=config.MIMS.CATALOG.FLASK_SECRET,
    )

    base.init_app(app, user_api=True, client_api=True, template_dir=Path(__file__).parent / 'templates')
    views.init_app(app)

    return app

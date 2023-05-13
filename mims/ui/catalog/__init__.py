from pathlib import Path

from flask import Flask

from mims.config import config
from mims.ui.catalog import views
from odp.const import ODPCatalog, ODPScope
from odp.const.hydra import HydraScope
from odp.ui import base


def create_app():
    """
    Flask application factory.
    """
    app = Flask(__name__)
    app.config.update(
        CATALOG_ID=ODPCatalog.MIMS,
        CATALOG_FACETS=[
            'Project',
            'Location',
            'Instrument',
            'License',
        ],
        CATALOG_TERMS_OF_USE='''
            These data are made available with the express understanding that any such use
            will properly acknowledge the originator(s) and publisher and cite the accession
            numbers and/or associated Digital Object Identifiers. Anyone wishing to use these
            data should properly cite and attribute the data providers listed as authors in
            the metadata provided with each dataset. It is expected that all the conditions
            of the data license will be strictly honoured. Use of any material herein should
            be properly cited using the dataset’s persistent identifiers such as accession
            numbers and DOIs.
        ''',
        UI_CLIENT_ID=config.MIMS.CATALOG.UI_CLIENT_ID,
        UI_CLIENT_SECRET=config.MIMS.CATALOG.UI_CLIENT_SECRET,
        UI_CLIENT_SCOPE=[
            HydraScope.OPENID,
            HydraScope.OFFLINE_ACCESS,
            ODPScope.RECORD_READ,
            ODPScope.TOKEN_READ,
        ],
        CI_CLIENT_ID=config.MIMS.CATALOG.CI_CLIENT_ID,
        CI_CLIENT_SECRET=config.MIMS.CATALOG.CI_CLIENT_SECRET,
        CI_CLIENT_SCOPE=[
            ODPScope.CATALOG_READ,
            ODPScope.CATALOG_SEARCH,
        ],
        SECRET_KEY=config.MIMS.CATALOG.FLASK_SECRET,
    )

    base.init_app(app, user_api=True, client_api=True, template_dir=Path(__file__).parent / 'templates')
    views.init_app(app)

    return app

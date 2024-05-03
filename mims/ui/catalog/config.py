from odp.config.base import BaseConfig
from odp.config.mixins import AppConfigMixin


class MIMSCatalogConfig(BaseConfig, AppConfigMixin):
    class Config:
        env_prefix = 'MIMS_CATALOG_'


class MIMSConfig(BaseConfig):
    _subconfig = {
        'CATALOG': MIMSCatalogConfig,
    }


class Config(BaseConfig):
    _subconfig = {
        'MIMS': MIMSConfig,
    }


config = Config()

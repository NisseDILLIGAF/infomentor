import configparser
import os

_config = None

_defaults = {
    "general": {
        "baseurl": "",
        "im1url": "https://infomentor.se/swedish/production",
        "mimrul": "https://hub.infomentor.se",
    },
    "user": {"username": "", "password": ""},
}


def _set_defaults(config):
    config = _defaults


def load(cfg_file="infomentor.ini"):
    """Load the config from the file"""
    global _config
    if _config is None:
        _config = configparser.ConfigParser(_defaults)
        if not os.path.isfile(cfg_file):
            _set_defaults(_config)
            save(cfg_file)
        _config.read(cfg_file)
    return _config


def save(cfg_file="infomentor.ini"):
    """Write config to file"""
    global _config
    with open(cfg_file, "w+") as f:
        _config.write(f)

"""Bridge module for plugin entry point resolution.

N.E.K.O host's fallback loader expects __init__.py at the plugin root directory.
This bridge re-exports the entry class from the nested plugins/<id>/ directory.
"""
from .plugins.neko_mail import NekoMailPluginEntry as NekoMailPluginEntry

__all__ = ["NekoMailPluginEntry"]

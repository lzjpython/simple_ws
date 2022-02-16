"""
ASGI config for simple_ws project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from ws.middleware import websockets

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_ws.settings')

application = get_asgi_application()
application = websockets(application)

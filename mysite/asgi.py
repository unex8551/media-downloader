"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from starlette.staticfiles import StaticFiles
from starlette.applications import Starlette
from starlette.routing import Mount

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()

app = Starlette(
    routes=[
        Mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), '..', 'mediaDownloader', 'static')), name="static")
    ]
)

app.mount("/", application)
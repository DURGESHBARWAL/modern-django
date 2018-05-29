from .base import*

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env('DJANGO_SECRET_KEY', default='yq6yl7#7=o7u5-gw&d!0wasc607u)%@z404*c93dq%o79c#g6d')


DEBUG = env.bool('DJANGO_DEBUG', default=True)

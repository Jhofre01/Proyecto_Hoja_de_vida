"""
Django settings for hojadevida project.
"""

import os
from pathlib import Path
import dj_database_url

# ===============================
# BASE
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ===============================
# SECURITY
# ===============================
SECRET_KEY = "django-insecure-hoja-de-vida-2025-jhofre"

DEBUG = True


ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

ALLOWED_HOSTS.append('.onrender.com')

# ===============================
# APPLICATIONS
# ===============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'paginasusuario.apps.PaginasusuarioConfig',
]

# ===============================
# MIDDLEWARE
# ===============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ===============================
# URLS / TEMPLATES
# ===============================
ROOT_URLCONF = 'hojadevida.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hojadevida.wsgi.application'

# ===============================
# DATABASE
# ===============================
DATABASES = {
    'default': dj_database_url.parse(
        "postgresql://basehojadevida_user:LA1Y5mKNYWToIUQz7QNmUlNLlS9E7Ulc@dpg-d5mnh5be5dus73el0ce0-a.virginia-postgres.render.com/basehojadevida",
        conn_max_age=600,
        ssl_require=True
    )
}



# ===============================
# PASSWORD VALIDATION
# ===============================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ===============================
# INTERNATIONALIZATION
# ===============================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ===============================
# STATIC FILES
# ===============================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "paginasusuario" / "static",
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)

# ===============================
# MEDIA FILES
# ===============================
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ===============================
# DEFAULT PK
# ===============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===============================
# CLOUDINARY CONFIG
# ===============================

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dfglycyoq',
    'API_KEY': '225322155144452',
    'API_SECRET': 'mpMFBgO4vroVpERT5CDJdiHCl_M',
}


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'



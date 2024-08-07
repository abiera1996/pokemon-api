"""
Django settings for pokedex project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os, datetime
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(0am)*pr66uqv-p&#31if$dbldw5n&c2yo%7=6=!r3!s%v#$u@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pokedex',
    'app_pokemon',
    'app_web',
    'utils',
    
    'tailwind',
    'tailwind_theme',
    'django_browser_reload',
    'rest_framework', 
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pokedex.middleware.LoggingMiddleware', 
    'pokedex.middleware.ResponseHandler',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

ROOT_URLCONF = 'pokedex.urls'
TAILWIND_APP_NAME = 'tailwind_theme'
INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pokedex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media')
]
 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=3),
    'JWT_ALLOW_REFRESH': True
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ), 
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_PAGINATION_CLASS': 'pokedex.pagination.CustomPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'EXCEPTION_HANDLER': 'pokedex.exception.custom_exception_handler'
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Pokemon API',
    'DESCRIPTION': 'Core API business management and services. ',
    'CONTACT': {},
    'LICENSE': {},
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'EXTERNAL_DOCS': {},
    'EXTENSIONS_INFO': {},
    'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
    'SERVE_AUTHENTICATION': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        "persistAuthorization": True,
        "displayOperationId": True,
    },
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE': True,
    'CAMELIZE_NAMES': False,

    'APPEND_COMPONENTS': {
        'securitySchemes': {
            'bearerAuthTraxion': {
                'type': 'http',
                'scheme': 'bearer',
                'bearerFormat': 'JWT',
                'name': 'Authorization',
                'in': 'header'
            },
        },
    },
    'POSTPROCESSING_HOOKS': [
        'drf_spectacular.hooks.postprocess_schema_enums',
    ],
    'SORT_OPERATIONS': False,
    'SORT_OPERATION_PARAMETERS': False,
    'COMPONENT_SPLIT_REQUEST': True,
    # OTHER SETTINGS
}
APPEND_SLASH = False 

# ----------- Configs ------------------
CORS_ALLOW_ALL_ORIGINS = False 
PROJECT_ENVIRONMENT = 'dev'

try:
    from pokedex.local import *
except:
    pass

# LOGGING SETTINGS
LOGGING = { 
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'custom':{
            'format':"API [%(levelname)s] %(asctime)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
        },
    }, 
    'handlers': {
        'logging_handler':{
            'class':'logging.handlers.RotatingFileHandler',
            'level': 'WARNING' if PROJECT_ENVIRONMENT == 'production' else 'DEBUG',
            'formatter': 'custom',
            'maxBytes': 31457280,  # 1024 * 1024 * 30B = 30MB
            'backupCount': 5,
            'filename':'logs/api.log',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'custom'
        },  
    },
    'loggers': {
        'django': {
            'handlers': ['logging_handler', 'console'],
            'level': 'WARNING' if PROJECT_ENVIRONMENT == 'production' else 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': { 
            'handlers': ['console'],
            'level': 'WARNING',   # DEBUG will log all queries, so change it to WARNING.
            'propagate': False,   # Don't propagate to other handlers
        },
        'django.utils.autoreload': {
            'handlers': ['console'],
            'level': 'WARNING',   # DEBUG will log all queries, so change it to WARNING.
            'propagate': False,   # Don't propagate to other handlers
        },
        'django.template': {
            'handlers': ['console'],
            'level': 'WARNING',   # DEBUG will log all queries, so change it to WARNING.
            'propagate': False,   # Don't propagate to other handlers
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'WARNING',   # DEBUG will log all queries, so change it to WARNING.
            'propagate': False,   # Don't propagate to other handlers
        },
        'django.server': {
            'handlers': ['console'],
            'level': 'INFO',   # DEBUG will log all queries, so change it to WARNING.
            'propagate': False,   # Don't propagate to other handlers
        }, 
    }
}
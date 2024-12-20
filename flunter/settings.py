"""
Django settings for flunter project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from datetime import timedelta
import os
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
env = environ.Env(
    DEBUG=(bool, False),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ["https://maximum-vertically-barnacle.ngrok-free.app"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    "rest_framework",
    "rest_framework_swagger",
    "drf_yasg",
    "rest_framework_simplejwt.token_blacklist",
    "web",
    "users",
    "administration",
    "aisearchbot",
    "django_user_agents",
    "api.jwtauth",
    "api.subscriptions",
    "api.payments",
    "api.auth_users",
    "api.asb",
    "api.actions",
    'api.shared_profiles',
    'api.my_lists',
    'api.saved_searches',
    "api.search_locations",
    "api.needs",
    "api.user_connections",
    "api.asb_admin",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    
    'users.middlewares.SessionUpdateMiddleware',

]

ROOT_URLCONF = 'flunter.urls'

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
                'flunter.context_processors.api_base_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'flunter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': env('FLUNTER_DB_ENGINE'),
        'NAME': env('FLUNTER_DB_NAME'),
        'USER': env('FLUNTER_DB_USER'),
        'PASSWORD': env('FLUNTER_DB_PASSWORD'),
        'HOST': env('FLUNTER_DB_HOST'),
        'PORT': env('FLUNTER_DB_PORT'),
        'CONN_MAX_AGE': None
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    "NON_FIELD_ERRORS_KEY": "Error",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "api.core.pagination.CustomPagination",
    "PAGE_SIZE": 5,
    "DATE_INPUT_FORMATS": ["%d-%m-%Y"],
    "TIME_INPUT_FORMATS": ["%I:%M %p"],
    "DATETIME_INPUT_FORMATS": ["%d-%m-%Y %I:%M %p"]
    
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=int(os.getenv("ACCESS_TOKEN_LIFE_HOURS"))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(os.getenv("REFRESH_TOKEN_LIFE_DAYS"))),
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "users.User"

SESSION_COOKIE_NAME = env.str('SESSION_COOKIE')


EMAIL_USE_TLS = env.bool('FLUNTER_EMAIL_USE_TLS', default=True)
EMAIL_HOST = env.str('FLUNTER_EMAIL_HOST')
EMAIL_PORT = env.int('FLUNTER_EMAIL_PORT')
EMAIL_HOST_USER = env.str('FLUNTER_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('FLUNTER_EMAIL_HOST_PASSWORD')



DEFAULT_PROFILE_IMAGE = "default-profile.png"

from django.contrib.messages import constants as cs
MESSAGE_TAGS = {
    cs.SUCCESS:'alert-success',
    cs.INFO:'alert-info',
    cs.ERROR:'alert-danger',
    cs.WARNING: 'alert-warning'
}
LOGOUT_REDIRECT_URL = "/"
STRIPE_PUBLIC_KEY = env.str('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = env.str('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_KEY = env.str('STRIPE_WEBHOOK_KEY')

GOOGLE_MAPS_API_KEY = env.str('GOOGLE_MAPS_API_KEY')

FRONTEND_URL = env.str('FRONTEND_URL')
AISEARCHBOT_URL = env.str('AISEARCHBOT_URL')
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_TRUSTED_ORIGINS = ["https://flunter.app", "https://www.flunter.app"]

CONTACT_EMAIL_RECEIVER = env.str('CONTACT_EMAIL_RECEIVER')
ENV = env.str('ENV')

SESSION_LIFETIME_HOURS = env.int('SESSION_LIFETIME_HOURS')
SESSION_LIFETIME_MINUTES = env.int('SESSION_LIFETIME_MINUTES')

if SESSION_LIFETIME_HOURS > 0:
    SESSION_LIFETIME = timedelta(hours=SESSION_LIFETIME_HOURS)
elif SESSION_LIFETIME_MINUTES > 0:
    SESSION_LIFETIME = timedelta(minutes=SESSION_LIFETIME_MINUTES)
else:
    SESSION_LIFETIME = timedelta(hours=1)

API_URL = env.str('API_URL')


CORS_ALLOW_ALL_ORIGINS = True
import os
from pathlib import Path
from urllib.parse import urlparse

# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# Security key (don't expose this in production, set via environment variables)
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-@0((ij7wn8e0!m%mv0u(xw++bs8z-k=1#$h4srwmpf@j-$ai^w')

# Debug settings
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# Allowed hosts (add your Vercel domain here)
ALLOWED_HOSTS = [".vercel.app", "127.0.0.1", ".now.sh", "localhost"]

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'ckeditor',
    'corsheaders',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True  # Adjust this for production

# URL configuration
ROOT_URLCONF = 'resume.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'resume.context_processors.project_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'resume.wsgi.application'

# Database configuration (adjust for production use with DATABASE_URL)
DATABASE_URL = os.getenv('postgres://postgres:root@localhost:5432/portfolio')

if DATABASE_URL:
    parsed_db_url = urlparse(DATABASE_URL)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': parsed_db_url.path[1:],  # Removes leading '/'
            'USER': parsed_db_url.username,
            'PASSWORD': parsed_db_url.password,
            'HOST': parsed_db_url.hostname,
            'PORT': parsed_db_url.port,
        }
    }
else:
    # Fallback for local development (make sure PostgreSQL is running locally)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'portfolio',
            'USER': 'postgres',
            'PASSWORD': 'root',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# CKEditor configuration
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


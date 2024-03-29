"""
Django settings for tracker project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from djangae.settings_base import * #Set up some AppEngine specific stuff
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

from .boot import get_app_config
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_app_config().secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

INTERNAL_IPS = (
    '127.0.0.1',
    'localhost',
    '::1'
)

# Application definition

INSTALLED_APPS = (
    'djangae', # Djangae needs to come before django apps in django 1.7 and above
    'djangae.contrib.consistency',
    'django.contrib.admin',
    'django.contrib.auth',
    'djangae.contrib.gauth.datastore',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangosecure',
    'csp',
    'cspreports',
    'djangae.contrib.gauth',
    'djangae.contrib.security',
    'crispy_forms',
    'crispy_forms_foundation',
    'tracker',
    'tracker.site'
)

MIDDLEWARE_CLASSES = (
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'djangae.contrib.gauth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'csp.middleware.CSPMiddleware',
    'session_csrf.CsrfMiddleware',
    'djangosecure.middleware.SecurityMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'djangae.contrib.gauth.datastore.backends.AppEngineUserAPIBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "session_csrf.context_processor",
    "tracker.site.context_processors.general",
)

SECURE_CHECKS = [
    "djangosecure.check.sessions.check_session_cookie_secure",
    "djangosecure.check.sessions.check_session_cookie_httponly",
    "djangosecure.check.djangosecure.check_security_middleware",
    "djangosecure.check.djangosecure.check_sts",
    "djangosecure.check.djangosecure.check_frame_deny",
    "djangosecure.check.djangosecure.check_ssl_redirect",
    "tracker.checks.check_session_csrf_enabled",
    "tracker.checks.check_csp_is_not_report_only"
]

CSP_REPORT_URI = reverse_lazy('report_csp')
CSP_REPORTS_LOG = True
CSP_REPORTS_LOG_LEVEL = 'warning'
CSP_REPORTS_SAVE = True
CSP_REPORTS_EMAIL_ADMINS = False

ROOT_URLCONF = 'tracker.urls'

WSGI_APPLICATION = 'tracker.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static-dev/'

# sensible default CPS settings, feel free to modify them
CSP_DEFAULT_SRC = ("'self'", "*.gstatic.com")
CSP_STYLE_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'", "themes.googleusercontent.com", "*.gstatic.com")
CSP_FRAME_SRC = ("'self'", "www.google.com", "www.youtube.com", "accounts.google.com", "apis.google.com", "plus.google.com")
CSP_SCRIPT_SRC = ("'self'", "*.googleanalytics.com", "*.google-analytics.com", "ajax.googleapis.com")
CSP_IMG_SRC = ("'self'", "data:", "s.ytimg.com", "*.googleusercontent.com", "*.gstatic.com")
CSP_CONNECT_SRC = ("'self'", "plus.google.com", "www.google-analytics.com")

if DEBUG:
    CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
    CSP_IMG_SRC += ("*.placehold.it",)

CRISPY_TEMPLATE_PACK = 'foundation-5'
CRISPY_ALLOWED_TEMPLATE_PACKS = ('foundation-5', )

AUTH_USER_MODEL = 'djangae.GaeUser'

CONSISTENCY_CONFIG = {

    # These defaults apply to every model, unless otherwise overriden.
    # The values shown here are the default defaults (i.e. what you get if
    # you don't set CONSISTENCY_CONFIG at all).
    "defaults": {
        "cache_on_creation": True,
        "cache_on_modification": True,
        "cache_time": 60,  # Seconds
        "caches": ["django"],  # Where to store the cache.
        "only_cache_matching": [],  # Optional filtering (see below)
    },
}

from djangae.contrib.gauth.settings import *

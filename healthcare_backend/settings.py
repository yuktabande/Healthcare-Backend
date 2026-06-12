import tomllib
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

# Load main config
with open(BASE_DIR / "pyproject.toml", "rb") as f:
    _config = tomllib.load(f)

# Load secrets separately
_secrets_path = BASE_DIR / "secrets.toml"
if not _secrets_path.exists():
    raise FileNotFoundError("secrets.toml not found. Copy secrets.toml.example and fill it in.")

with open(_secrets_path, "rb") as f:
    _secrets = tomllib.load(f)

_django_cfg = _config["tool"]["django"]
_db_cfg = _django_cfg["database"]
_jwt_cfg = _django_cfg["jwt"]

SECRET_KEY = _secrets["secret_key"]  # ← from secrets.toml
DEBUG = _django_cfg["debug"]
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "rest_framework",
    "rest_framework_simplejwt",
    # Local apps
    "authentication",
    "patients",
    "doctors",
    "mappings",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "healthcare_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "healthcare_backend.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": _db_cfg["name"],
        "USER": _db_cfg["user"],
        "PASSWORD": _db_cfg["password"],
        "HOST": _db_cfg["host"],
        "PORT": _db_cfg["port"],
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DRF settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
    ),
}

# JWT settings from pyproject.toml
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=_jwt_cfg["access_token_lifetime_minutes"]),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=_jwt_cfg["refresh_token_lifetime_days"]),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": False,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

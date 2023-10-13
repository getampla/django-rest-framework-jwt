import django

if django.VERSION < (3, 2):
  default_app_config = 'rest_framework_jwt.blacklist.apps.BlacklistedTokenConfig'

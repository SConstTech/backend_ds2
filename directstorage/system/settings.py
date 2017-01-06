from copy import deepcopy

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


default_settings = {
    'SEND_ACTIVATION_EMAIL': False,
    'SEND_CONFIRMATION_EMAIL': False,
    'SET_PASSWORD_RETYPE': False,
    'SET_USERNAME_RETYPE': False,
    'PASSWORD_RESET_CONFIRM_RETYPE': False,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': False,
    'ROOT_VIEW_URLS_MAPPING': {},
    'PASSWORD_VALIDATORS': [],
    'SERIALIZERS': {
        'activation': 'system.serializers.ActivationSerializer',
        'login': 'system.serializers.LoginSerializer',
        'password_reset': 'system.serializers.PasswordResetSerializer',
        'password_reset_confirm': 'system.serializers.PasswordResetConfirmSerializer',
        'password_reset_confirm_retype': 'system.serializers.PasswordResetConfirmRetypeSerializer',
        'set_password': 'system.serializers.SetPasswordSerializer',
        'set_password_retype': 'system.serializers.SetPasswordRetypeSerializer',
        'set_username': 'system.serializers.SetUsernameSerializer',
        'set_username_retype': 'system.serializers.SetUsernameRetypeSerializer',
        'user_registration': 'system.serializers.UserRegistrationSerializer',
        'user': 'system.serializers.UserSerializer',
        'token': 'system.serializers.TokenSerializer',
        'token_group': 'system.serializers.TokenGroupSerializer',
    },
    'LOGOUT_ON_PASSWORD_CHANGE': False,
}


def get(key):
    user_settings = merge_settings_dicts(
        deepcopy(default_settings), getattr(settings, 'system', {}))
    try:
        return user_settings[key]
    except KeyError:
        raise ImproperlyConfigured('Missing settings: system[\'{}\']'.format(key))


def merge_settings_dicts(a, b, path=None, overwrite_conflicts=True):
    """merges b into a, modify a in place

    Found at http://stackoverflow.com/a/7205107/1472229
    """
    if path is None:
        path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_settings_dicts(a[key], b[key], path + [str(key)], overwrite_conflicts=overwrite_conflicts)
            elif a[key] == b[key]:
                pass  # same leaf value
            else:
                if overwrite_conflicts:
                    a[key] = b[key]
                else:
                    conflict_path = '.'.join(path + [str(key)])
                    raise Exception('Conflict at %s' % conflict_path)
        else:
            a[key] = b[key]
    # Don't let this fool you that a is not modified in place
    return a

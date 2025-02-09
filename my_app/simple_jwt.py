# my_app/simple_jwt.py

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),  # Access token 7 kun davomida amal qiladi
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  # Refresh token 7 kun davomida amal qiladi
    'ROTATE_REFRESH_TOKENS': True,  # Refresh tokenni har safar yangilash
    'BLACKLIST_AFTER_ROTATION': True,  # Refresh tokenni yangilagandan keyin eski tokenni blacklistga qo'yish
}

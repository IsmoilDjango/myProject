# my_app/scripts/create_admin.py
from django.contrib.auth.models import User

def run():
    try:
        if not User.objects.filter(username="ismoilDjangoAdmin").exists():
            User.objects.create_superuser("ismoilDjangoAdmin", "maxammatovislom222@gmail.com", "parol123!")
            print("Superuser created successfully!")
        else:
            print("Superuser already exists.")
    except Exception as e:
        print(f"Error creating superuser: {e}")

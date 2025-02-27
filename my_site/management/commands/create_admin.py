from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Creates a superuser if none exist"

    def handle(self, *args, **kwargs):
        try:
            if not User.objects.filter(username="ismoiladmin").exists():
                User.objects.create_superuser("ismoiladmin", "maxammatovislom222@gmail.com", "Admin123!")
                self.stdout.write(self.style.SUCCESS("Superuser created successfully!"))
            else:
                self.stdout.write(self.style.WARNING("Superuser already exists."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating superuser: {e}"))

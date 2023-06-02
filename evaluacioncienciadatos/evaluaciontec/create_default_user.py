from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates a default user for the application'

    def handle(self, *args, **options):
        username = 'administrador'  # Replace with desired username
        email = 'areli.pa@cdguzman.tecnm.mx'  # Replace with desired email
        password = 'admin123'  # Replace with desired password

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Default user created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Default user already exists.'))
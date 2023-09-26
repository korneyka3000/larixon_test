from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        username = 'admin'
        password = 'admin'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, password=password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists.'))

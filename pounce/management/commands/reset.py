from django.core.management.base import BaseCommand

from ...models import Course


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Course.objects.all().delete()

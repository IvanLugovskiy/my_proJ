from book.models import Book

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(1_000):
            Book.objects.create(
                author=fake.name(),
                title=fake.word(),
            )

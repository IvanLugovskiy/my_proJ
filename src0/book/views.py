from book.models import Book

from django.http import HttpResponse

from faker import Faker


def book(request):
    books = Book.objects.all()
    results = ''
    for tmp in books:
        results += f'ID: {tmp.id}, title: {tmp.title}, author: {tmp.author}'

    return HttpResponse(results)


def create_book(request):
    fake = Faker()
    tmp = Book.objects.create(
        author=fake.name(),
        title=fake.word(),
    )
    return HttpResponse(f'ID: {tmp.id}, author: {tmp.author}, title: {tmp.title}')

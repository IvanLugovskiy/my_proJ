from book.models import Book
from django.shortcuts import render, get_object_or_404
from book.forms import Book, BookForm

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from faker import Faker


def book(request):
    books = Book.objects.all()
    results = ''
    for tmp in books:
        results += f'ID: {tmp.id}, title: {tmp.title}, author: {tmp.author}'

    return HttpResponse(results)



def create_book(request):
    global form
    if request.method == 'POST':
        form = BookForm(request.POST)
        is_valid = form.is_valid()
        if is_valid:
            form.save()
            return HttpResponseRedirect('/books/list/')
    elif request.method == 'GET':
        form = BookForm()
    context = {'book_form': form}
    return render(request, 'create_book.html', context=context)


def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        is_valid = form.is_valid()
        if is_valid:
            form.save()
            return HttpResponseRedirect('/books/list/')
    elif request.method == 'GET':
        form = BookForm(instance=book)
        context = {'book_form': form}
        return render(request, 'create_book.html', context=context)
    
   

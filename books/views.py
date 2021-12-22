from django.shortcuts import render, HttpResponse
from . models import Author, Book
from django.db.models import Count

def book_view(request):

    # 4.1 solution
    print("-------4.1 solution----------")
    for b in  Book.objects.all()[:5:0]:
        print(b.title + "," + b.author.name)

    # 4.2 solution
    print("-------4.2 solution----------")
    for author in Author.objects.all():
        result = Book.objects.filter(author=author)
        for book in result:
            print(author.name,",", book.title)
    
    # 4.3 solution
    print("-------4.3 solution----------")
    book_count = Author.objects.annotate(total_books=Count('book'))
    for count in book_count:
        print(count.name, count.total_books)

    return HttpResponse('<h2> Django assignment </h2>')
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = [
        "title",
        "author",
        "published_date",
        "isbn",
        "copies_total",
        "copies_available",
    ]
    success_url = reverse_lazy("book_list")


class BookUpdateView(UpdateView):
    model = Book
    fields = [
        "title",
        "author",
        "published_date",
        "isbn",
        "copies_total",
        "copies_available",
    ]
    success_url = reverse_lazy("book_list")


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("book_list")

# Create your views here.

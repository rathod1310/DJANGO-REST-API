from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# BookListCreateView
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# BookRetrieveUpdateDeleteView
class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
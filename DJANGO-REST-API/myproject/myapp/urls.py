from django.urls import path
from . import views
from .views import BookListCreateView, BookRetrieveUpdateDeleteView

urlpatterns = [
	path('',BookListCreateView.as_view(), name='book-list-create'),
    path('<int:pk>/',BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),

]
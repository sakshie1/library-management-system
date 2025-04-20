from django.urls import path
from .views import AdminSignupView, BookListCreateView, BookUpdateDeleteView, StudentBookListView, AdminLoginView

urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view()),
    path('admin/login/', AdminLoginView.as_view()),
    path('books/', BookListCreateView.as_view()),
    path('books/<int:pk>/', BookUpdateDeleteView.as_view()),
    path('student/books/', StudentBookListView.as_view()),
]

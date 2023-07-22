from django.urls import path
from book.views import UserRegistrationView,UserLoginView
urlpatterns =[
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    #path('bkinfo/<int:pk>',BookDetailView.as_view(),name='book_detail'),
    
]
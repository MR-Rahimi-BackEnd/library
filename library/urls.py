from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_book,name='list_book'),
    path('create/',views.form_book,name='create_book'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('create_book',views.create_book,name = 'create'),
    path('book/<int:id>',views.book_details,name='book_details'),
    path('book/update/<int:id>',views.update_book,name='book_update'),
    path('book/delet/<int:id>',views.delet_book,name='book_delet'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('about/',views.about,name='about'),
]
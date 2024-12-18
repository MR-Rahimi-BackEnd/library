from django.contrib import admin
from django.urls import path
from .views import SignupView,ListView,FormBook,UpdateBook,DeletBook,DetailView
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',ListView.as_view(),name='list_book'),
    path('create/',FormBook.as_view(),name='create_book'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('create_book',TemplateView.as_view(template_name = 'library/create_book'),name = 'create'),
    path('book/<int:pk>',DetailView.as_view(),name='book_details'),
    path('book/update/<int:pk>',UpdateBook.as_view(),name='book_update'),
    path('book/delet/<int:pk>',DeletBook.as_view(),name='book_delet'),
    path('contact/',TemplateView.as_view(template_name = 'library/contact.html'),name='contact'),
    path('services/',TemplateView.as_view(template_name = 'library/services.html'),name='services'),
    path('about/',TemplateView.as_view(template_name = 'library/about.html'),name='about'),
    path('home/',TemplateView.as_view(template_name = 'library/home.html'),name='home'),
    path('logout/accounts',TemplateView.as_view(template_name = 'library/logout_accounts.html'),name='logout_accounts'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
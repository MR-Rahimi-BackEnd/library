from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Book
from .forms import NewForm, SingupForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.models import User


class ListView(ListView):
    model = Book
    template_name = 'library/list_book.html'
    context_object_name = 'book'

class FormBook(CreateView):
    model = Book
    form_class = NewForm
    template_name = 'library/create_book.html'
    success_url = reverse_lazy('list_book')
    
class SignupView(CreateView):
    model = User
    form_class = SingupForm
    template_name = 'library/signup.html'
    success_url = reverse_lazy('login')
    
class UpdateBook(UpdateView):
    model = Book
    form_class  = NewForm
    template_name = 'library/update_book.html'
    success_url = reverse_lazy('list_book')
    
class DeletBook(DeleteView):
    model = Book
    template_name = 'library/delet_book.html'
    success_url = reverse_lazy ('list_book')
    
class DetailView(DetailView):
    model = Book
    template_name = 'library/details_book.html'
    context_object_name = 'book'


# def list_book(request):
#     book = Book.objects.all()
#     return render(request,'library/list_book.html',{'book':book})


# def signup_view(request):
#     if request.method == 'POST':
#         form = SingupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = SingupForm()
#     return render(request, 'library/signup.html', {'form': form})

# def book_details(request,id):
#     book = get_object_or_404(Book,id=id)
#     return render(request,'library/details_book.html',{'book':book})





# def update_book(request,id):
#     book = get_object_or_404(Book,id=id)
#     if request.method =='POST':
#         form = NewForm(request.POST , instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('list_book')
#     else:
#         form = NewForm(instance=book)
#     return render(request,'library/update_book.html',{'book':book,'form':form})


# def delet_book(request,id):
#     book = get_object_or_404(Book,id=id)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('list_book')
#     return render(request,'library/delet_book.html',{'book':book})


# def form_book(request):
#     if request.method == 'POST':
#         form = NewForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             return redirect('list_book')
#     else:
#         form = NewForm()
#     return render(request,'library/create_book.html',context={'form':form})





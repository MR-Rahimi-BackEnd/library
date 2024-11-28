from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Book
from .forms import NewForm, SingupForm

def list_book(request):
    book = Book.objects.all()
    return render(request,'list_book.html',{'book':book})

def create_book(request):
    return render(request,'create_book')


def form_book(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('list_book')
    else:
        form = NewForm()
    return render(request,'create_book.html',context={'form':form})


def signup_view(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SingupForm()
    return render(request, 'signup.html', {'form': form})

def book_details(request,id):
    book = get_object_or_404(Book,id=id)
    return render(request,'details_book.html',{'book':book})


def update_book(request,id):
    book = get_object_or_404(Book,id=id)
    if request.method =='POST':
        form = NewForm(request.POST , instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = NewForm(instance=book)
    return render(request,'update_book.html',{'book':book,'form':form})

def delet_book(request,id):
    book = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_book')
    return render(request,'delet_book.html',{'book':book})

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')
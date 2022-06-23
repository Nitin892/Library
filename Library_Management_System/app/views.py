from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import auth
from .models import Book
from django.contrib.auth.hashers import check_password
from .forms import BookForm

def home(request):
    return render(request,'app/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("getbook")
        return render(request, 'app/login.html', {'error': 'invalid credetial'})
    return render(request,'app/login.html')


def signup(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password2==password1:
            if User.objects.filter(username=username).exists():
                return render(request,'app/login.html',{'error':'username already exists'})
            elif User.objects.filter(email=email).exists():
                return render(request,'app/login.html',{'error':'email already exists'})

            else:
                user=User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password1)
                user.save()
                return redirect('login')
    return render(request,'app/signup.html')


from django.contrib.auth.decorators import login_required
@login_required(login_url='loginform')
def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url='login')
def createbook(request):
    if request.method=="POST":
        form=BookForm(request.POST)
        newform=form.save(commit=False)
        newform.user=request.user
        newform.save()
        return redirect('getbook')
    return render(request,'app/createbook.html',{'form':BookForm})





@login_required(login_url='login')
def getBook(request):
    book = Book.objects.filter(user=request.user)
    return render(request, 'app/getbook.html', {'book': book})

@login_required(login_url='login')
def deletebook(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("getbook")


@login_required(login_url='login')
def updatebook(request, id):
    book = Book.objects.get(id=id)
    updatebook = BookForm(request.POST or None, instance=book)
    if request.method == 'POST':
        if updatebook.is_valid():
            newform = updatebook.save(commit=False)
            newform.user = request.user
            newform.save()
            return redirect('getbook')
    return render(request, 'app/update.html', {'updatebook': updatebook})
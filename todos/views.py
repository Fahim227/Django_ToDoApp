from django.contrib import messages
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.http import request
from .models import todo
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import todoSerializer
# Create your views here.
@login_required
def index(request):
    all_todos =  todo.objects.filter(user_id = request.user)
    context = {
        'todo_list' : all_todos
    }
    return render(request, 'todos/list.html',context)
    
def insert(request):
    id = request.user.id
    todo_obj = todo(title = request.POST['title'],content = request.POST['content'],user_id=id)
    todo_obj.save()
    return redirect("/todos/home")

def delete(request,todo_id):
    delete_item= todo.objects.get(id=todo_id)
    delete_item.delete()
    return redirect("/todos/home")

def edit(request,todo_id):
    todos = todo.objects.get(id=todo_id)
    context = {
        "todo_title" : todos.title,
        "todo_content" : todos.content,
        "todo_id" : todos.id
    }
    #print("Hello"+todos)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if len(str(title)) != 0:
            todos.title = title

        if len(str(content)) != 0:
            todos.content = content

        todos.save()
        return redirect('/todos/home')


    else:
        return render(request, 'todos/edit.html', context)
    

def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['conpassword']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect("/todos/register")
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"Email already exists")
                 return redirect("/todos/register")
            else:
                userr = User.objects.create_user(username=username,email=email,password=password1)
                userr.save()
                return redirect('/todos')
                print("Saved")
        else:
            messages.info(request,'password not matching..')    
            return redirect('/todos/register')

    else:
        return render(request,'todos/register.html')
        

def login(request):
    if request.method == 'POST':
        Uname = request.POST['username']
        Upassword = request.POST['password']

        authobj = auth.authenticate(username = Uname, password = Upassword)
        #print(authobj)

        if authobj is not None:
            auth.login(request,authobj)
            print("Loged in")
            return redirect('login')
        else:
            # messages.Info(request,'invalid credentials')
            print("Not Loged in")
            #print(Uemail+Upassword)
            return redirect('/todos')
    else:
        return render(request,'todos/login.html')
    
def logout_views(request):
    logout(request)
    return redirect('/todos')

@api_view( ['GET'] )
def listapi(request):
    todos = todo.objects.all()
    serializer = todoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def saveasapi(request):
    serializer = todoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data)
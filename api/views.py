from django.shortcuts import render,redirect
from api.models import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def index(request) :
  students = Student.objects.all()
  query = ""

  if request.method == "POST" :
    if "add" in request.POST:
      name = request.POST.get("name")
      description = request.POST.get("description")
      image = request.FILES.get("userimage")
      Student.objects.create(
        name = name,
        description = description,
        image = image
      )
      messages.success(request,"Student created successfully")

    elif "update" in request.POST :
      id = request.POST.get("id")
      name = request.POST.get("name")
      description = request.POST.get("description")
      image = request.FILES.get("userimage")
      update_student = Student.objects.get(id = id)
      update_student.name = name
      update_student.description = description
      if image:
        update_student.image = image
      update_student.save()
      messages.success(request,"Student updated successfully")

    elif "delete" in request.POST :
      id = request.POST.get("id")
      Student.objects.get(id = id).delete()
      messages.success(request,"Student deleted successfully")

    elif "search" in request.POST :
      query = request.POST.get("searchquery")
      students = Student.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
  context = {"students":students,"query":query}
  return render(request,"index.html",context=context)

def signuppage(request) :
  if request.method == "POST" :
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = User.objects.filter(username = username)
    if user.exists() :
      messages.info(request, "User already exists")
      return redirect("/signup/")
    
    user = User.objects.create_user(
      username = username,
      password = password
    )
    messages.info(request, "Registered successfully")
    return redirect("/")
  return render(request,"signup.html")


def loginpage(request) :
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    if not User.objects.filter(username=username).exists() :
      messages.info(request,"Username not exists")
      return redirect("/login/")
    
    user = authenticate(username=username,password=password)
    if user is None :
      messages.info(request,"Password is incorrect")
      return render(request, "login.html")
    else:
      login(request,user)
      return redirect("/")
  return render(request, "login.html")
    
def logoutpage(request) :
  logout(request)
  return redirect("/login/")
from django.shortcuts import render
from api.models import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def index(request) :
  students = Student.objects.all()
  query = ""

  if request.method == "POST" :
    if "add" in request.POST:
      name = request.POST.get("name")
      description = request.POST.get("description")
      Student.objects.create(
        name = name,
        description = description
      )
      messages.success(request,"Student created successfully")

    elif "update" in request.POST :
      id = request.POST.get("id")
      name = request.POST.get("name")
      description = request.POST.get("description")
      update_student = Student.objects.get(id = id)
      update_student.name = name
      update_student.description = description
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
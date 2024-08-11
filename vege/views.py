from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='/login/')
def add_recipe(request):

    if request.method=="POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_rating = data.get('recipe_rating')

        Recipe.objects.create(recipe_name=recipe_name,recipe_desc=recipe_desc,recipe_rating=recipe_rating)
        return redirect("/recipe/")

    queryset=Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context={'recipies':queryset}

    return render(request,'recipe.html',context)

def update_recipe(request,id):
    queryset = Recipe.objects.get(id=id)

    if request.method=="POST":
        recipe_name = request.POST.get('recipe_name')
        recipe_desc = request.POST.get('recipe_desc')
        recipe_rating = request.POST.get('recipe_rating')

        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc
        queryset.recipe_rating = recipe_rating

        queryset.save()
        return redirect('/recipe/')
    context = {'recipe':queryset}
    return render(request,'update_recipe.html',context)

def deleted_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/recipe/")

def login_page(request):

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('/login/')
        
        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recipe/')

    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):

    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'Username Already taken')
            return redirect('/register/')

        user = User.objects.create(first_name=first_name,
                                   last_name=last_name,
                                   username=username)
        user.set_password(password)
        user.save()
        messages.info(request,"Account Created Successfully")
        return redirect('/register/')

    return render(request,'register.html')
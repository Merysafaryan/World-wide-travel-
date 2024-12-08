from django.shortcuts import render, redirect
from .models import Fav, Logo, HomeBgInfo, About, Project, Gallery, Team, ContactInfo, ContactUs
from .models import Rio

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactUs.objects.create(name=name, email=email, message=message)
        return redirect('index')
    fav_icon = Fav.objects.first()
    home_logo = Logo.objects.first()
    home_bg_info = HomeBgInfo.objects.first()
    about = About.objects.first()
    projects = Project.objects.all()
    rio_projects = Rio.objects.all()
    contact = ContactInfo.objects.first()
    return render(request, 'main/index.html', context={
        'fav_icon': fav_icon,
        'home_logo':home_logo,
        'home_bg_info':home_bg_info,
        'about':about ,
        'projects':projects,
        'rio_projects': rio_projects,
        'contact':contact
    })
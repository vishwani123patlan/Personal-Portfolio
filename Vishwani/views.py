from django.shortcuts import render
from Vishwani.models import About,Education,Gallery


def index(request):
    return render(request,'Home.html')

def about_details_view(request):
    Obj=About.objects.all()
    EduObj=Education.objects.all()

    return render(request,'About.html',{'disc':Obj,'Educ':EduObj,})

def gallery_view(request):
    Glry = Gallery.objects.all()
    return render(request,'Gallery.html',{'Galry':Glry})
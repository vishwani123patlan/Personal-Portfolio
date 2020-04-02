from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about_details_view,name='about'),
    path('gallery/',views.gallery_view,name='about'),
]
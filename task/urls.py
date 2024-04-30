from django.contrib import admin
from django.urls import path,include
from todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('todolist/',include('todolist.urls')),
    path('account/',include('users.urls')),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]

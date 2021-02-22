from django.urls import path
from django.conf.urls.static import static

from jobportal import settings
from jobs import views

urlpatterns = [
    path('',views.home),
    path('log',views.log,name='log'),
    path('register',views.register_data,name='register'),
    path('reg',views.reg),
    path('administrator',views.administrator, name='admin'),
    path('logging',views.logging),
    path('Home',views.Home,name='home'),
    path('edit/<int:id>', views.editfunction, name='edit'),
    path('delete/<int:id>', views.deletefunction, name='delete'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
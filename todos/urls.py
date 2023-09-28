from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('portfolio/', views.portfolio_index, name='index'),
    path('', views.login, name='index'),
    path('/insert/', views.insert, name='insert'),
    path('/delete/<int:todo_id>', views.delete, name='delete'),
    path('/register/',views.register,name='register'),
    path('/home/',views.index,name='login'),
    path('/logout/',views.logout_views, name='logout'),
    path('/edit/<int:todo_id>', views.edit, name='edit'),
    path('/api/', views.listapi, name='todolistapi'),
    path('/saveapi/', views.saveasapi, name='saveapi'),

    


] + static(settings.STATIC_URL, document = settings.STATIC_ROOT)

from django.urls import path
from .import views

urlpatterns = [
    path('recipe/', views.add_recipe),
    path('delete_recipe/<id>/', views.deleted_recipe),
    path('update_recipe/<id>/', views.update_recipe),
    path('login/',views.login_page),
    path('logout/',views.logout_page), 
    path('register/',views.register_page),
]

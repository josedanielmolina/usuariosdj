from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [

    path(
        'registar-usuario',
        views.UserRegisterView.as_view(),
        name = 'registrar-usuarios',
    ),

    path(
        'login',
        views.UserLogin.as_view(),
        name = 'login',
    ),

    path(
        'logout',
        views.LogoutView.as_view(),
        name = 'logout',
    ),

]
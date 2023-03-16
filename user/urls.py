
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(),name='home'),
    path("registration", views.RegisterUser.as_view(),name='registration'),
    path("login", views.LoginUser.as_view(),name='login'),
    path("logout", views.Logout.as_view(),name='logout'),
    # path("", views.home,name='home'),
    # path("registration", views.register_user,name='registration'),
    # path("login", views.login_user,name='login'),
    # path("logout", views.logout_user,name='logout'),
]

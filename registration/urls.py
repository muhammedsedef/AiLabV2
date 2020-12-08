from django.urls import path
from . import views
# from .views import UserRegisterView,CreateMember
from .views import CreateMember,LoginMember,LogoutMember,EditProfile,ResetPassword

urlpatterns = [
    # path('register/', UserRegisterView.as_view(), name = 'register'),
    path('register/', views.CreateMember, name = 'register'),
    path('login/', views.LoginMember, name = 'login'),
    path('edit_profile/', views.EditProfile, name = 'edit_profile'),
    path('reset_password/', views.ResetPassword, name = 'reset_password'),
    path('logout/', views.LogoutMember, name = 'logout'),
]

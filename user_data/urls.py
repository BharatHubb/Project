from django.urls import path
from .views import * 


urlpatterns =[
    path("registration/",reg_user,name="reg"),
    path("login/",user_login,name="user_login"),
    path("logout/",log_out,name="log_out"),
    path("login_page",login_page,name="login_page"),
    path("user-signup",user_signup,name="user_signup"),

    

]
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home_page,name= "home"),
    path('active-emp/',active_emp,name= "active_emp"),
    path('in-active-emp/',in_active_emp,name= "in_active_emp"),
    path('view-emp/<int:id>',show_detail,name= "show_emp"),
    path('update-emp/<int:id>',update_details,name= "update_emp"),
    path('soft-delete/<int:id>',soft_delete,name= "soft_delete"),
    path('hard-delete/<int:id>',hard_delete,name= "hard_delete"),
    path('view/<int:id>',view,name= "view"),
    path('restore/<int:id>',restore,name= "restore"),
    path('add-emp',add_emp,name= "add_emp"),
    path('create-csv',create_csv,name= "create_csv"),
    path('sample-create-csv',sample_create_csv,name= "sample_create_csv"),
    path('upload-csv',upload_csv,name= "upload_csv"),
    path('create-inactive-csv',create_inactive_csv,name= "create_inactive_csv"),

    

]
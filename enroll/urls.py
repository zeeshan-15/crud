from django.contrib import admin
from django.urls import path, include
from enroll import views

urlpatterns = [

    path('', views.User_Add_Show_View.as_view(), name='list_add_data'),
    path('delete/<int:id>', views.User_Delete_View.as_view(), name="delete_data"),
    path('<int:pk>', views.User_Update_View.as_view(), name="update_data"),
]

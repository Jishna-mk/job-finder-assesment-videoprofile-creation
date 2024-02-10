from django.urls import path
from .import views

urlpatterns=[
    path('',views.admin_signin,name="admin_signin"),
    path('admin_signout',views.admin_signout,name="admin_signout"),
    path('view_dashboard',views.view_dashboard,name="view_dashboard"),
    path('approve/<int:c_id>/',views.approve,name="approve"),
    path('remove/<int:c_id>/',views.remove,name="remove"),


]
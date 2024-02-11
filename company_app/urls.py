from django.urls import path
from .import views

urlpatterns=[
    path('post_job/',views.post_job,name="post_job"),
    path('company_job_list/',views.company_job_list,name="company_job_list"),
    path('company_job_details/<int:Job_id>/', views.company_job_details, name='company_job_details'),
    path('deletejob/<int:pk>',views.deletejob,name="deletejob"),
    path('companysignup/', views.companysignup, name='companysignup'),
    path('company_signin/', views.company_signin, name='company_signin'),
    path('company_signout',views.company_signout,name="company_signout"),
    path('all_applications/',views.all_applications,name="all_applications"),
    path('edit_job/<int:pk>/',views.edit_job, name='edit_job'), 
    path('video_cam',views.video_cam,name="video_cam"),
    path('employee-profile/', views.employee_profile_view, name='employee_profile'),
    path('view_company_messages/', views.view_company_messages, name="view_company_messages"),
    path('reply_message/<int:id>', views.reply_message, name="reply_message"),
    path('send_message_to_user/', views.send_message_to_user, name='send_message_to_user'),
    path('view-applicant/<int:id>/', views.view_applicant, name='view_applicant'),
    # path('view_application/<int:application_id>/', views.view_application, name='view_application'),

    # path('view_application/<int:application_id>/', views.view_user_application, name='view_user_application'),
    
]



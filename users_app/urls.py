from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('category',views.category,name="category"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name='signout'),
    path('job_list/',views.job_list,name="job_list"),
    path('testimonial',views.testimonial,name='testimonial'),
    path('job-detail/<int:Job_id>/', views.job_details, name='job_details'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('user_applications/', views.user_applications, name='user_applications'),
    path('withdraw_application/<int:application_id>/', views.withdraw_application, name='withdraw_application'),
    path("create_profile/",views.create_profile,name="create_profile"),
    path("view_user_profile/",views.view_user_profile,name="view_user_profile"),
    path('student-dashboard', views.student_dashboard,name='student-dashboard'),
    path('student_exam', views.student_exam,name='student_exam'),
    path('take-exam/<int:pk>', views.take_exam,name='take-exam'),
    path('start-exam/<int:pk>', views.start_exam,name='start-exam'),
    path('view-result', views.view_result, name='view-result'),
    path('check-marks/<int:pk>', views.check_marks, name='check-marks'),
    path('student-marks', views.student_marks, name='student-marks'),
    path('calculate-marks', views.calculate_marks, name='calculate-marks'),
    path('video/',views.video,name="video"),
    path('employee-list/', views.employee_list_view, name='employee_list'),
    path('send_message/<int:id>', views.send_message, name="send_message"),
    path('view_messages/', views.view_messages, name="view_messages"),

]
   
    

    
    

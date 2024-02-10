from django.urls import path
from .import views
urlpatterns=[
    path('dashboard', views.dashboard_view,name='dashboard'),
    path('exam', views.exam_view,name='exam'),
    path('add-exam', views.add_exam,name='add-exam'),
    path('view-exam', views.view_exam,name='view-exam'),
    path('delete-exam/<int:pk>', views.delete_exam,name='delete-exam'),


    path('question', views.question_view,name='question'),
    path('add-question', views.add_question,name='add-question'),
    path('view-question', views.view_question,name='view-question'),
    path('see-question/<int:pk>', views.see_question,name='see-question'),
    path('remove-question/<int:pk>', views.remove_question,name='remove-question'),
]
          
          

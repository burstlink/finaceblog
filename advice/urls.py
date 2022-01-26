from django.urls import path

from advice import views

urlpatterns = [
    path('', views.QuestionListView.as_view(), name="question_list"),
    path('create/', views.QuestionCreateView.as_view(), name="question_create"),
    path('<int:pk>/delete', views.QuestionDeleteView.as_view(), name="question_delete"),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name="question_detail"),
]

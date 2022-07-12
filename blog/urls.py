from . import views
from django.urls import path

urlpatterns = [
    path('',views.BlogHome.as_view()),
    path('list/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
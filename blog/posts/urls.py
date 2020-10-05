from django.urls import path
from . import views

urlpatterns=[
    path('postlist',views.PostList.as_view(),name='postlist'),
    path('postdetail/<int:pk>/', views.PostDetail.as_view(), name='postdetail'),
]
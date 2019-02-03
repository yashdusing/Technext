from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView

)
from django.views.decorators.http import require_POST
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    url('like/',views.like , name='like'),
    path('curr2/<int:pk>/',views.curr2,name='curr2'),
    path('ml/<int:pk>/<int:balance>/',views.ml,name='ml'),
    path('<int:pk>/<int:balance>/',views.home,name='home'),

]

#url('like/',views.like , name='like'),

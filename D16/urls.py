from django.urls import path
from .views import *


urlpatterns = [
    path('', Board.as_view(), name='board'),
    path('post/<int:pk>', ShowPost.as_view(), name='Post_show'),
    path('create/', CreatePost.as_view(), name='Post_create'),
]
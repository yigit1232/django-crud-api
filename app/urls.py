from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('api/post/list/',views.get_all_post),
    path('api/post/detail/<slug:slug>/',views.get_detail_post),
    path('api/post/create/',views.post_create),
    path('api/post/delete/<int:id>/',views.post_delete),
    path('api/post/update/<int:id>/',views.post_update.as_view())
]
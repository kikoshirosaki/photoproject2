from django.urls import path
from . import views

app_name='photos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/',views.CreatePhotoView.as_view(),name='post'),
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
    path('photos/<int:category>',views.CategoryView.as_view(),name='photos_cat'),
    path('user_list/<int:user>',views.UserView.as_view(),name='user_list'),
    path('photo_detail/<int:pk>',views.PhotoDetailView.as_view(),name='photo_detail'),
    path('maypage',views.MypageView.as_view(),name='mypage'),
    path('photo/<int:pk>/delete/',views.PhotoDeleteView.as_view(),name='photo_delete'),
    ]
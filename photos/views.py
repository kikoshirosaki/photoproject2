from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost


class IndexView(ListView):
    template_name='index.html'
    queryset=PhotoPost.objects.order_by('-posted_at')
    paginate_by=3

@method_decorator(login_required,name='dispatch')
class CreatePhotoView(CreateView):
    form_class=PhotoPostForm
    template_name='post_photo.html'
    success_url=reverse_lazy('photos:post_done')

    def form_valid(self, form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name='post_success.html'

class CategoryView(ListView):
    template_name='index.html'
    paginate_by=3

    def get_queryset(self):
        category_id=self.kwargs['category']
        categories=PhotoPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories

class UserView(ListView):
    template_name='index.html'
    paginate_by=3

    def get_queryset(self):
        user_id=self.kwargs['user']
        user_list=PhotoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list

class PhotoDetailView(DetailView):
    template_name='detail.html'
    model=PhotoPost

class MypageView(ListView):
    template_name='mypage.html'
    paginate_by=3

    def get_queryset(self):
        queryset=PhotoPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset

class PhotoDeleteView(DeleteView):
    template_name='photo_delete.html'
    model=PhotoPost
    success_url=reverse_lazy('photos:mypage')

    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)

class PhotoUpdateView(UpdateView):
    template_name='photo_detail.html'
    model=PhotoPost
    success_url=reverse_lazy('photos:mypage')

    def update(self,request,*args,**kwargs):
        return super().update(request,*args,**kwargs)


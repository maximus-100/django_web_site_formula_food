
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Category, Post, Profile, User, Ip, Comments
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.edit import FormMixin
from django.db.models import Count, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddCommentForm, AddPostForm
from .utils import get_client_ip
from django.core.paginator import Paginator


# Create your views here.


class HomePage(ListView):  # post_list.html
    model = Post
    template_name = 'web_site/index.html'
    paginate_by = 5


    def get_queryset(self):
        posts = self.model.objects.annotate(Count('likes'))
        data = []
        for post in posts:
            comment_count = Comments.objects.filter(post=post).count()
            user_image = Profile.objects.get(user=post.author).image_url()
            data.append({
                'post': post,
                'comment_count': comment_count,
                'user_image': user_image
            })
        return data

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        latest_post = Post.objects.all().order_by('-pk')
        context['latest_post'] = latest_post[:3]
        return context


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'web_site/post.html'
    form_class = AddCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.model.objects.get(pk=self.kwargs['pk'])
        comments = Comments.objects.filter(post=post)
        comment_count = comments.count()
        user_image = Profile.objects.get(user=post.author).image_url()
        like_info = post.likes.filter(id=self.request.user.id).exists()

        ip = get_client_ip(self.request)
        if Ip.objects.filter(ip=ip).exists():
            post.views.add(Ip.objects.get(ip=ip))  # Добавь просмотр
        else:
            Ip.objects.create(ip=ip)
            post.views.add(Ip.objects.get(ip=ip))  # Добавь просмотр

        comment_data = []
        for comment in comments:
            user = comment.name
            profile_image = Profile.objects.get(user=user).image_url()
            comment_data.append({
                'profile_image': profile_image,
                'comment': comment
            })

        detail = {
            'post': post,
            'comment_data': comment_data,
            'comment_count': comment_count,
            'user_image': user_image,
            'liked': like_info
        }
        context['detail'] = detail
        return context


def post_page(request):
    return render(request, 'web_site/post.html')


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'web_site/add_post.html'
    redirect_field_name = 'redirect-to'
    login_url = reverse_lazy('login')



class AddCommentView(CreateView):
    model = Comments
    form_class = AddCommentForm

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])
        body = form.cleaned_data['body']
        name = self.request.user
        comment = Comments(post=post, name=name, body=body)
        comment.save()

        return super(AddCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})


class ProductListByCategory(ListView):
    model = Post
    context_object_name = 'products'
    template_name = 'web_site/category_page.html'
    paginate_by = 3

    def get_queryset(self):
        products = Post.objects.filter(category__slug=self.kwargs['slug'])
        data = []
        for post in products:
            comment_count = Comments.objects.filter(post=post).count()
            user_image = Profile.objects.get(user=post.author).image_url()
            data.append({
                'post': post,
                'comment_count': comment_count,
                'user_image': user_image
            })
        return data


def page_t(request):
    objects = Category
    paginator = Paginator(objects, 2)
    page_name = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_name)
    return render(request, 'web_site/category_page.html', {'page_obj': page_objects})


def page_d(request):
    objects = Post
    paginator = Paginator(objects, 2)
    page_name = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_name)
    return render(request, 'web_site/index.html', {'page_obj': page_objects})


# class Search(ListView):
#     template_name = 'web_site/index.html'
#     context_object_name = 'web_post'
#     paginate_by = 3
#
#     def get_queryset(self):
#         return Post.objects.filter(title__icontains=self.request.GET.get('q'))
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['q'] = self.request.GET.get('q')
#         return context


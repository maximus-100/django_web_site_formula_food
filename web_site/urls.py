from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='index'),  # Вид пути, Кто за нее отвечает, Имя

    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='post_detail'),
    path('post/', post_page, name='post'),
    path('add/post/', AddPostView.as_view(), name='add'),
    path('comments/<int:pk>/add/', AddCommentView.as_view(), name='add_comment'),
    path('category/<slug:slug>/', ProductListByCategory.as_view(), name='category'),
    path('page_t/', page_t, name='page_t'),
    path('page_d/', page_d, name='page_d'),
    # path('search/', Search.as_view(), name='search')

]

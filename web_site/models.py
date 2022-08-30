from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse

# Create your models here.
User._meta.get_field('email')._unique = True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, default='Информация о себе', blank=True)
    profile_image = models.ImageField(upload_to='photo/profile/%Y/%m/%d/', blank=True)
    phone = models.CharField(max_length=30, default='+998(xx)xxx-xx-xx', blank=True)
    mobile = models.CharField(max_length=30, default='+998(xx)xxx-xx-xx', blank=True)
    address = models.CharField(max_length=120, default='Планета Замля', blank=True)
    website_url = models.CharField(max_length=255, default='#', blank=True)
    github_url = models.CharField(max_length=255, default='#', blank=True)
    instagram_url = models.CharField(max_length=255, default='#', blank=True)
    facebook_url = models.CharField(max_length=255, default='#', blank=True)
    telegram_url = models.CharField(max_length=255, default='#', blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def image_url(self):
        try:
            url = self.profile_image.url
        except:
            url = 'https://cdn-icons-png.flaticon.com/512/3135/3135715.png'
        return url


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')  # Имя отображения
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(upload_to='categories/',
                              null=True, blank=True,
                              verbose_name='Изображение')

    # id писать не надо. Django сам есго создаст

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Категория: pk={self.pk}, title={self.title}'


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    content = models.TextField(verbose_name='Описание статьи')  # Огромный текст
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания, возьмет автоматически время
    updated_at = models.DateTimeField(auto_now=True)  # Возьмет время при любом изменении объекта
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Изображение')
    # blank=True - не обязательное для заполнения  null=True - может быть пустой в базе
    # category_id INTEGER REFERENCES categories(category_id)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    # При удалении категории - удалить все новости ВОЛНОЙ
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)
    views = models.ManyToManyField(Ip, related_name='post_views', blank=True)


    def get_absolute_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.pk})

    def get_count_views(self):
        return self.views.count()  # Общее количество просмотров статьи

    def get_count_likes(self):
        return self.likes.count()

    def photo_url(self):
        try:
            url = self.photo.url
        except:
            url = 'https://www.raumplus.ru/upload/iblock/423/Skoro-zdes-budet-foto.jpg'
        return url

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Товар: pk={self.pk}, title={self.title}'


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

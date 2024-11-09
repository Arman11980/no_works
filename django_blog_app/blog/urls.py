from .views import PostListView
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('',PostListView.as_view(), name="blog-home"),
    path('',include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('logout/',auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    path('profile/', user_views.profile, name="profile"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

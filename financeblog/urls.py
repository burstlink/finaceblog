"""financeblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from profiles import views as profiles_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', profiles_views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
    path('profile/<int:pk>', profiles_views.profile, name="profile"),
    path('profile/update', profiles_views.update, name='update'),
    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='profiles/password_reset.html'), name='password_reset'),
    path('password-rest/confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(
        template_name='profiles/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-rest/done', auth_view.PasswordResetDoneView.as_view(
        template_name='profiles/password_reset_done.html'), name='password_reset_done'),
    path('password-rest/complete', auth_view.PasswordResetCompleteView.as_view(
        template_name='profiles/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

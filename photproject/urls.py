from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('photo.urls')),
    path('', include('accounts.urls')),
    path('password_reset/',
        auth_views.PasswordResetDoneView.as_view(
            template_name = "password_reset.html"),
        name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name = "password_reset_send.heml"),
        name='password_reset_done'),
    path('rest/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name = "password_reset_form.html"),
        name ='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name = "password_reset_done.html"),
        name ='password_reset_complete'),        
    ]

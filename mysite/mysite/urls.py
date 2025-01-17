"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from autoblog import auth_views, member_views, stripe_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member_views.home, name='home'),
    path('home/', member_views.home, name='home'),
    path('register/', auth_views.register, name='register'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('verification/', auth_views.verification, name='verification'),
    path('verifyEmail/<str:key>/', auth_views.verify_email, name='verify_email'),
    path('memberInfo/', member_views.member_info, name='member_info'),
    path('generateBlog/', member_views.generate_blog, name='generate_blog'),
    path('memberDash/', member_views.member_dashboard, name='member_dashboard'),
    path('settings/', member_views.settings, name='settings'),
    path('contact/', member_views.contact, name='contact'),
    path('taskStatus/<str:task_id>/', member_views.poll_task_status, name='task_status'),


    path('saveBlog/', member_views.save_blog, name='save_blog'),
    path('postBlog/', member_views.post_blog, name='post_blog'),
    path('deleteBlog/', member_views.delete_blog, name='delete_blog'),


    path('pay/', stripe_views.pay, name='pay'),
    path('pay/create-checkout-session/', stripe_views.create_checkout_session, name='checkout'),
    path('success/', stripe_views.success, name='success'),
    path('cancel/', stripe_views.cancel, name='cancel'),
    path('pay/cancel-subscription/', stripe_views.handle_subscription_cancelled, name='cancel-subscription'),
    path('pay/upgrade-subscription/', stripe_views.handle_subscription_update, name='upgrade-subscription'),
    path('webhook/', stripe_views.stripe_webhook, name='webhook'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
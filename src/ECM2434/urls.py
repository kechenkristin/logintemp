"""ECM2434 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import TemplateView

# from management.views import user, login_management, gamekeeper

urlpatterns = [
    path("admin/", admin.site.urls),


    # path("user/info/", user.user_info),
    # path("user/add/", user.user_add),
    #path("user/<int:uid>/edit/", user.user_edit),
    #path("user/<int:uid>/delete/", user.user_delete),

    #path("user/register/", user.user_register),
    #path("user/login/", login_management.user_login),
    #path("user/logout/", login_management.user_logout),
    #path("image/code/", login_management.image_code),

    #path("get/user", login_management.get_user),

    #path("gamekeeper/info/", gamekeeper.gamekeeper_info),
    #path("gamekeeper/add/", gamekeeper.gamekeeper_add),
    #path("gamekeeper/<int:uid>/edit/", gamekeeper.gamekeeper_edit),
    #path("gamekeeper/<int:uid>/delete/", gamekeeper.gamekeeper_delete),

    #path("gamekeeper/register/", gamekeeper.gamekeeper_register),
    #path("gamekeeper/login/", login_management.gamekeeper_login),
    #path("gamekeeper/logout/", login_management.gamekeeper_logout),

    # path("test/permission/add/", permission.views.gamekeeper_add),
    # path("test/permission/info/", permission.views.gamekeeper_info),
    
    # path("",permission.views.index, name="index"),

    # path("projects/", permission.views.project_listing, name="project"),
    # path("<slug:id>/", permission.views.project_detail, name="project_detail"),
    # path("project/new/", permission.views.create_project),

    # path("accounts/login/", permission.views.login_view),
    # path(r'^login/$', 'django.contrib.auth.views.login', {'template_name': '/login.html'}),


    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("login.urls")),
    # path("accounts/", include("accounts.urls")),

    # path("",permission.views.index, name="index"),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
]

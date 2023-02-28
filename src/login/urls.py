from django.urls import path

import login.views

# from permission.views import SignUpView

urlpatterns = [
    # path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/normaluser/", login.views.userRegister),
    path("signup/gamekeeper/", login.views.gamekeeperRegister),
    path("permission/test", login.views.login_test),
]

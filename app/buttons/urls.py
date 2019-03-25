from django.urls import path
from . import views

app_name = "buttons"
urlpatterns = [
        path("", views.mainview, name = "main_page"),
        path("code/submitcode", views.generatecode, name = "generatecode"),
        path("code/verifycode", views.verifycode, name = "verifycode"),
        path("try", views.tryy, name = "try"),
        path("tutorial", views.tutorial, name = "tutorial"),
        path("haha", views.download, name = "download"),
]

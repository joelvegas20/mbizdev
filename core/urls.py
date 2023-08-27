from django import views
from django.contrib import admin
from django.urls import include, path

from core.views import HomeView

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('projects/', include('apps.projects.urls'))
]
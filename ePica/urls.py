from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_view

urlpatterns = [
    path('', accounts_view.home, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]

from django.contrib import admin
from django.urls import path, include
from blogapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('blog/', include('blogapp.urls')),

]

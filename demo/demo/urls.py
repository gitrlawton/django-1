"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# Include is used to take the URL patterns from an app, and include them in 
# the Django project's main URL configuration.
from django.urls import include

# All the urls for our entire project.  Create urls here to link into
# our application.
urlpatterns = [
    # admin/ is the prefix.  This path is here by default upon proj creation.
    path('admin/', admin.site.urls),
    # "" is the prefix.  "" stands for the base (root) url of the project.  
    # This signifies that we will append the url patterns from myapp to the 
    # project's root url, which means they will be accessible from there.
    path("", include("myapp.urls"))
    # This allows us to have the same url endpoints in different applications,
    # and depending on what the prefix is, we can reach those different 
    # endpoints.  For example:  myapp/home  and   mysecondapp/home
]

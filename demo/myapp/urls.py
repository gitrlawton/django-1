## Where we'll place different url routes and then connect them to our views. ##

from django.urls import path
# Importing the app's views.py file.
from . import views

urlpatterns = [
    # When we go to the base url (localhost:5000), it will call the home
    # function in views.py.  These urls have now been configured WITHIN our
    # application, but they still need to be configured TO our project
    # (visit the inner project folder's urls.py file to do this.)
    path("", views.home, name="home"),
    
    # Make sure when adding another path, you include a comma after each
    # previous one.  There won't be an error for it, just that you haven't
    # closed the list (which is not actually the problem.)
    
    # The path to render the todos view.
    path("todos/", views.todos, name="Todos")
]
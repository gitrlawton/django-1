from django.shortcuts import render
from django.shortcuts import HttpResponse
# Import our TodoItem model for querying.
from .models import TodoItem

# Create your views here.

# Passing 'request' allows this route to handle query parameters and data
# that is inside the body of a request.
# This is not a route, this is a function that later needs to be connected
# to our application through a route or url. See the app's urls.py file.
def home(request):
    return HttpResponse("hello world!")


def todos(request):
    # Query (get) all the Todo items that exist in the database and store
    # them in a queryset named items.  This is similar to a list, and 
    # consists of all the rows of the TodoItem database table.
    items = TodoItem.objects.all()
    # Render a template named todos.html, which will display all the Todo
    # List items on it.  Next we'll need to create a path for this rendered 
    # data.  Do so in the app's urls.py file.
    # Note: the dictionary we're passing containing our todo items can
    # be referenced just like a list by using its key.  For example, 
    #  for element in todos:  will iterate through all the values in the 
    # dictionary (ie. our todo items).
    return render(request, "todos.html", {"todos": items})
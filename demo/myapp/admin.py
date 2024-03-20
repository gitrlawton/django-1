from django.contrib import admin
# Import the model we created.
from .models import TodoItem

# Register your database models here.  Registering allows the models to appear
# inside the admin panel, allowing us to modify and view them.

# Registering a model.
admin.site.register(TodoItem)
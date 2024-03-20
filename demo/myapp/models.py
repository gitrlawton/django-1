from django.db import models

# Create your database models here.

# A model, written as a python class.  Models represent database tables.
# Every new model creates a new table, where all the instances of that 
# model will be stored -- each on a new line.  The model specifies what
# data will populate each of the columns by utilizing instance variables.
class TodoItem(models.Model):
    # Fields written as instance variables.
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
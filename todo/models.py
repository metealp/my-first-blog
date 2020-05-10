from django.db import models

# Create your models here.
class Common(models.Model): #it was not necessary but tested abstract classes
    text = models.CharField(max_length=90, blank=False)
    class Meta:
        abstract=True

class Todo(Common):
    todo_id=models.AutoField(primary_key=True) #for naming id column 
    deadline=models.DateTimeField(blank=True, null=True) 
    #add reminders as one to many model
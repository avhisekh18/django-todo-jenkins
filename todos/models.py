from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Travel(models.Model):
    destination = models.CharField(max_length=50)
    

    def __str__(self):
        return self.destination
    
class Book(models.Model):
    Author_name = models.CharField(max_length=30)
    

    def __str__(self):
        return self.Author_name
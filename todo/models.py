from django.db import models

class Todo(models.Model) : # pk, id 등 models.Model 안에 존재
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name
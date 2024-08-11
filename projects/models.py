from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2180, null=True, blank=True)
    source_code = models.CharField(max_length=2180, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
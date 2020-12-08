import json

from django.db import models

# Create your models here.
from project.models import Project,ProjectFile


class Report(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='stats_project')
    algorithm = models.CharField(max_length=100)
    all_data = models.TextField()
    selected_files = models.ManyToManyField(ProjectFile)


    def get_output(self):
        return json.loads(self.all_data)

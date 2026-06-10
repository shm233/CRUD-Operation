from django.db import models

# Create your models here.

class CourseModel(models.Model):
    DEPT = [
        ('CSE', 'CSE'),
        ('EEE', 'EEE')
    ]
    title = models.CharField(max_length=255, null=True)
    mark = models.PositiveIntegerField(null=True)
    department = models.CharField(max_length=50, choices=DEPT, null=True)
    course_image = models.ImageField(upload_to='media/course', null=True)
    start_date = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.title}---{self.department}"

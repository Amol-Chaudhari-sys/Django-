from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class StudentsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False )


class Recepies(models.Model):
    User = models.ForeignKey(User , on_delete = models.SET_NULL, null=True , blank=True )
    recepie_name= models.CharField(max_length=100)
    description= models.TextField()
    image = models.ImageField(upload_to="recepies")
    view_count = models.IntegerField(default=1)

class Department(models.Model):
    department= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ["department"]
    
class StudentId(models.Model):
    student_id= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id

class Student(models.Model):
    department= models.ForeignKey(Department, related_name="depart" , on_delete=models.CASCADE)
    studentid = models. OneToOneField(StudentId , related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True )
    student_age = models.IntegerField(default=18)
    student_address= models.TextField()
    is_deleted= models.BooleanField(default = False)

    objects = StudentsManager()
    admin_objects = models.Manager()

    def __str__ (self) -> str:
        return self.student_name

    class Meta:
        ordering= ["student_name"]
        verbose_name = 'Student' 


class Subjects(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str :
        return self.subject_name


class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name= "studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects , on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.student_name} { self.subject.subject_name}"
    
    class Meta: 
        unique_together = ['student', 'subject']
class Report_card ( models.Model):
    student = models.ForeignKey(Student , related_name="Studerntreportcard", on_delete = models.CASCADE)
    student_rank = models.IntegerField()
    date_of_reportcard_generated = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student_rank' , 'date_of_reportcard_generated']


    



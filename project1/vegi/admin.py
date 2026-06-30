from django.contrib import admin
from .models import *
from django.db.models import Sum 

# Register your models here.

admin.site.register(Recepies)
admin.site.register(StudentId)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Subjects)

class SubjectListAdmin (admin.ModelAdmin):
    list_display = ( 'student' , 'subject' , "marks") 

admin.site.register(SubjectMarks , SubjectListAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display=("student" , 'student_rank' ,'total_marks' ,'date_of_reportcard_generated')
    ordering =['student_rank']

    def total_marks(self , obj):
        subjectmarks = SubjectMarks.objects.filter (student = obj.student)
        marks = (subjectmarks.aggregate(marks = Sum('marks')))
        return marks['marks']
        


admin.site.register(Report_card , ReportCardAdmin)




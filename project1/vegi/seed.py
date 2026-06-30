
from faker import Faker
import random 
from vegi.models import *
from django.db.models import  Sum
fake = Faker()


def Seed_db(n= 100) -> None:
    try:
        for _ in range(0,n):

            department_obj = Department.objects.all()
            department_index = random.randint(0, len (department_obj)-1)
            department = department_obj[department_index]
            student_id = f"STU-0{random.randint(100,999)}"      
            student_name = fake.name()
            student_email= fake.email()
            student_age = random.randint(30, 80)
            student_address =fake.address()

            studentid = StudentId.objects.create(student_id = student_id)
                        
            student= Student.objects.create(department= department , studentid =studentid , student_name= student_name, student_email = student_email , student_age = student_age , student_address = student_address )
    except Exception as e :
        print (e)
        
def seed_marks(n):
    students= Student.objects.all()
    subjects= Subjects.objects.all()
    try :
    
        for student in students:
            for subject in subjects:
                subjectmarks = SubjectMarks.objects.create(student = student , subject = subject , marks= random.randint(1, 99) , )
        
    except Exception as e :
        print (3)


def generate_reportcard ():
    
    i=1
    ranks = Student.objects.annotate(marks = Sum ('studentmarks__marks') ).order_by('-marks' , 'student_age')
    for rank in ranks :
        report_card= Report_card.objects.create(student = rank  ,student_rank = i  )
        i+=1

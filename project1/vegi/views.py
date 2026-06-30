from django.shortcuts import render , redirect 
from django.http import HttpResponse
from vegi.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator 
from django.db.models import Q , Sum

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
@login_required(login_url="/login_page/")
def recepies(request ):
    if request.method=="POST":
        data= request.POST
        image= request.FILES['image']
        recepie_name= data.get ('recepie_name')
        description = data.get('description')
        print(recepie_name , description)

        Recepies.objects.create( recepie_name=recepie_name, 
                                 description= description, 
                                 image= image ,)
        

        return redirect ( "/recepies/")
    recepie_list = Recepies.objects.all()
    
    if request.GET.get("Search"):
        recepie_list= recepie_list.filter(recepie_name__icontains = request.GET.get("Search"))
    context = {"page":"recepies" , "recepies":recepie_list}
    return render(request ,'recepies.html' , context )

def update_recepie(request , id ):
    query_set = Recepies.objects.get(id = id )

    if request.method =='POST':
        data= request.POST
        image= request.FILES.get ("image")
        recepie_name= data.get('recepie_name')
        description = data.get('description')


        query_set.recepie_name= recepie_name
        query_set.description = description

        if image :
            query_set.image= image 
        query_set.save()

        return redirect("/recepies/")


    context= {"recepie":query_set}
    return render(request ,"update_recepie.html",context )

def delete_recepie(request , id ):
    item = Recepies.objects.get(id= id )
    item.delete ()
    return redirect('/recepies/')
def logout_page(request):
    logout(request)

    return redirect ('/login_page/')



def login_page (request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
       

        if not User.objects.filter(username = username).exists():
            messages.error(request , "User not Exist ")
           
            return redirect("/login_page/")
        user = authenticate(username = username , password = password )
        

        if user is None:
            messages.error(request , "invalid Password ")
            
            return redirect ("/login_page/")
        else:
           
            login(request , user)
            
            return redirect ("/recepies/")

    return render(request, 'login_page.html')

def registration(request ):
    if request.method =="POST":
        data= request.POST
        first_name= data.get("first_name")
        last_name= data.get("last_name")
        user_name = data.get ("username")
        password = data.get("password")
        
        user= User.objects.filter(username= user_name)
        if user.exists():
            messages.info(request, "username  Already exist !")
            return redirect ("/registration/")

        user= User.objects.create( first_name= first_name,
        last_name= last_name,
        username= user_name
        )
        user.set_password(password)
        user.save()
        messages.info(request , "Sucessfully register ")
        return redirect ('/registration/')


    return render(request, 'registration.html')

def get_students(request):
    queryset = Student.objects.all()
    if request.GET.get("search"):
        search= request.GET.get("search")
        queryset= Student.objects.filter( Q (student_name__icontains = search )|
                                         Q(department__department__icontains = search)|
                                         Q( student_age__icontains = search) |
                                         Q(studentid__student_id__icontains = search ) |
                                         Q(student_email__icontains = search )
        )

    paginator = Paginator(queryset , 20 )
    page_no = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_no)

    return render(request , "report/students.html" , {"queryset" : page_obj})
from .seed import *
def see_marks(request , studentid):
    # generate_reportcard()
    queryset = SubjectMarks.objects.filter(student__studentid__student_id = studentid )
    total_marks  = queryset.aggregate( total_marks = Sum('marks'))

    

    return render(request , "report/result.html" , {"queryset": queryset , "total_marks" :total_marks  })
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .utils import send_email_to_client , send_email_with_attachment
from django.conf import settings

# Create your views here.
def home(request ):

    peoples =[{"name":"Amol", "Age":20,},
     {"name":"Vikas", "Age":19,},
     {"name":"Gaurav", "Age":22,},
     {"name":"Aditya", "Age":17,}]
    
    text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus, corrupti consequatur laborum nisi animi a autem molestiae aperiam earum similique repellendus rem, ipsa libero fugiat maxime odit dolorem laudantium est!"


    return render(request , "index.html" , context={"peoples":peoples , "text": text, "page": "Django Home"})
def sucess_page(request):
    
    return HttpResponse("<h1> this is sucessful Django page  </h1>")
def about(request):
    context={"page":"about"}
    return render(request , "about.html", context)
def contact(request ):
    context= {"page":"contact"}
    return render(request , "contact.html", context)

def send_email(request):
    subject = "this is heading of email by django "
    message = "this is message email body of the django "
    recipient_list = ["amolchaudha@gmail.com"]
    file_path =f"{settings.BASE_DIR}\summer.xlsx"
    send_email_with_attachment(subject , message ,  recipient_list , file_path )
    return redirect('/')


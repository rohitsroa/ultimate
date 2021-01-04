from django.shortcuts import render
from django.http import HttpResponse
from .models import QueryInfo
import datetime
from customauth.models import User, UserManager
from django.contrib import messages, auth
from .tables import QueryInfoTable
from django_tables2 import RequestConfig
import random
from django.views.generic.edit import UpdateView

# Create your views here.

def index(request):
    try:
        return render(request, 'pages/dashboard.html')
    except:
        return render(request, 'pages/error404.html')

def about(request):
    try:
        return render(request, 'pages/about.html')
    except:
        return render(request, 'pages/error404.html')

def faq_page(request):
    try:
        return render(request, 'pages/faq.html')
    except:
        return render(request, 'pages/error404.html')

def query_page(request):
    try:
        return render(request, 'pages/query.html')
    except:
        return render(request, 'pages/error404.html')

def query_table_page(request):
    try:
        QueryInfos = QueryInfo.objects.all()

        context = {
            'QueryInfos': QueryInfos
        }
        return render(request, 'pages/query_table.html', context)
    except:
        return render(request, 'pages/error404.html')

def status_page(request):
    try:
        return render(request, 'pages/status.html')
    except:
        return render(request, 'pages/error404.html')

def error_page(request):
        return render(request, 'pages/error404.html')

def add_query(request):
    print("FORM SUBMITTED")
    q_name = request.POST["name"]
    q_email = request.POST["email"]
    q_phone = request.POST["phone"]
    q_service = request.POST["service"]
    q_message = request.POST["message"]
    objM = User.objects.filter(department=q_service,manager=True)
    objE = User.objects.filter(department=q_service,engineer=True) 
    q_eng = objE[ random.randint(0,len(objE)-1)].userid
    q_man = objM[ random.randint(0,len(objM)-1)].userid

    q_object = QueryInfo(Name = q_name, Email = q_email, Phone = q_phone,Service = q_service, Message = q_message, Date = datetime.datetime.now(), Status = False, Manager_Name = q_man, Engineer_Name = q_eng)
    q_object.save()
    messages.success(request, 'Your Ticket Number is %d' %q_object.id)
    return render(request, 'pages/query.html')

def get_query(request):
    your_id = request.POST["query_number"]
    try:
        obj = QueryInfo.objects.get(id=your_id)

        context = {
            'name' : obj.Name, # = models.CharField(max_lengt, #h=50)
            'email' : obj.Email, # = models.CharField(max_lengt, #h=100)
            'phone'  : obj.Phone, # = models.CharField(max_lengt, #h=50)
            'service' : obj.Service, # = models.CharField(max_lengt, #h=100)
            'message' : obj.Message, # = models.TextField(max_lengt, #h=500)
            'date'  : obj.Date, # = models.DateTimeField(auto_no, #w=True)
            'status'  : obj.Status, # = models.BooleanField()
            'eng_name' : obj.Engineer_Name,
            'man_name' : obj.Manager_Name,
        }
        return render(request,"pages/yourstatus.html", context)
    except:
        messages.warning(request, 'Id Does Not Exist ! ! ')
        return render(request,"pages/status.html", {})

class QueryInfoUpdate(UpdateView):
    model = QueryInfo
    fields = ['status','department']
    template_name_suffix = '_update_form'

    
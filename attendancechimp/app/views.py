from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User  
import pytz
from django.utils import timezone
from datetime import datetime 

def dummypage(request):
     if request.method == "GET":
        return HttpResponse("No content here, sorry!")

def sum_view(request):
    n1 = request.GET.get('n1')
    n2 = request.GET.get('n2')
    if n1 is None or n2 is None:
        return HttpResponse("0")

    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        return HttpResponse("Invalid input. Please enter valid numbers.")

    result = n1 + n2
    return HttpResponse(str(result))

def time_view(request):
    central = pytz.timezone('America/Chicago')

    now = datetime.now(central)

    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    time_since_midnight = now - midnight

    hours, remainder = divmod(time_since_midnight.seconds, 3600)
    minutes = remainder // 60
    time_str = f"{hours:02}:{minutes:02}"

    return HttpResponse(time_str)

@csrf_exempt
def index(request):
    return render(request, 'app/index.html')


@csrf_exempt
def index_html(request):
    utc_now = timezone.now()
    central_tz = pytz.timezone('America/Chicago')
    current_time = utc_now.astimezone(central_tz)
    context = {'current_time': current_time.strftime('%Y-%m-%d %I:%M:%S %p')}
    return render(request, 'app/index.html', context)



@csrf_exempt
def handle_form(request):

    cname = request.POST['cname']
    num =  request.POST['cnum']

    print(cname, cnum)

    new_course = Course(cname, cnum)
    new_course.save()

    return render(request, 'app/index.html', {})

@csrf_exempt
def new(request):
    if request.method == "GET":
        return render(request, 'app/new.html', {})
    # elif request.method == "POST":
        # return HttpResponse("Error!")

@csrf_exempt
def createUser(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('University_Email')
        role = request.POST.get('role')
        password = request.POST.get('Password')

        if User.objects.filter(email=email).exists():
            return HttpResponse("Error: Email already exists. Please use a different email.")

        user = User(
            username=email,
            email=email,
            first_name=name,  
            password=make_password(password) 
        )
        user.save()

        return HttpResponse("You have signed up successfully!")

    return HttpResponse("Error: This endpoint only accepts POST requests.")

#from django.contrib.auth import authenticate, login
#from django.contrib import messages

#@csrf_exempt
#def login_view(request):
#    if request.method == "POST":
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        user = authenticate(request, username=username, password=password)

#        if user is not None:
#            login(request, user)
#            return redirect('index') 
#        else:
#            messages.error(request, "Invalid credentials. Please try again.")

#    return render(request, 'registration/login.html', {})


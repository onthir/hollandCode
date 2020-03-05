from django.shortcuts import render, redirect
from .models import Attribute, Session
from .forms import *
# Create your views here.

def home(request):
    # a generic page to ask for user information and create a session under their name
    if request.user.is_authenticated:
        sessions = Session.objects.filter(user=request.user)
        if sessions.count() >= 1:
            print("Yes")
            # load the last session
            session = sessions.first()
            return redirect("main:verified")
        else:
            # create new session
            if request.method == "POST":
                form = InitializeForm(request.POST)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.user = request.user
                    data.save()
                    return redirect("main:verified")
            else:
                form = InitializeForm()
            return render(request, 'main/index.html', {"form": form})
    else:
        return redirect("accounts:login_user")
    # last_session = 
    
    return render(request, 'main/index.html')

def realisticQ(request):
    if request.user.is_authenticated:
        # choices for realistic
        realistic = Attribute.objects.filter(holland_code=1)

        # check form
        if request.method == "POST":
            attributes = request.POST.getlist("attributes")

        return render(request, 'main/questions.html', {"questions": realistic})
    else:
        return redirect("accounts:login_user")
# investigative
def investigativeQ(request):
    # choices for realistic
    investigative = Attribute.objects.filter(holland_code=2)

    # check form
    if request.method == "POST":
        attributes = request.POST.getlist("attributes")

    return render(request, 'main/questions.html', {"questions": investigative})

# artistic
def artisticQ(request):
    # choices for realistic
    artistic = Attribute.objects.filter(holland_code=3)

    # check form
    if request.method == "POST":
        attributes = request.POST.getlist("attributes")

    return render(request, 'main/questions.html', {"questions": artistic})

# social
def socialQ(request):
    # choices for realistic
    social = Attribute.objects.filter(holland_code=4)

    # check form
    if request.method == "POST":
        attributes = request.POST.getlist("attributes")
        print(attributes)


    return render(request, 'main/questions.html', {"questions": social})

# enterprising
def enterprisingQ(request):
    # choices for realistic
    enterprising = Attribute.objects.filter(holland_code=5)

    # check form
    if request.method == "POST":
        attributes = request.POST.getlist("attributes")

    return render(request, 'main/questions.html', {"questions": enterprising})

# conventional
def conventionalQ(request):
    # choices for realistic
    conventional = Attribute.objects.filter(holland_code=6)

    # check form
    if request.method == "POST":
        attributes = request.POST.getlist("attributes")

    return render(request, 'main/questions.html', {"questions": conventional})
def questions(request):
    # start session page for the user to test
    questions = Attribute.objects.all()
    realistic = Attribute.objects.filter(holland_code=1)
    investigative = Attribute.objects.filter(holland_code=2)
    artistic = Attribute.objects.filter(holland_code=3)
    social = Attribute.objects.filter(holland_code=4)
    enterprising = Attribute.objects.filter(holland_code=5)
    conventional = Attribute.objects.filter(holland_code=6)


    left = [realistic, investigative, artistic, social, enterprising, conventional]
    for attribute in left:
        # get all the values form the form submitted
        if request.method == "POST":
            # THIS WILL GET ALL THE RECOMMENDAITONS
            rAttributes = request.POST.getlist('realistic')
            print(rAttributes)
            return render(request, "main/questions.html", {"questions": attribute})
            
    context = {
        "questions": realistic,
        
    }
    return render(request, 'main/questions.html', context)

# create session for each session
def create_session(user, full_name, email):
    session = Session(user=user, full_name=full_name, email=email)
    session.save()
    return session

def nextQuestion(attr):
    # 
    context = {
        "questions": attr
    }
    return render("main/questions.html", context)


# verified page
def verified(request):
    if request.user.is_authenticated:
        sessions = Session.objects.filter(user=request.user)
        if sessions.count() >= 1:
            print("Session in Progress")
    return render(request, "main/verified.html")
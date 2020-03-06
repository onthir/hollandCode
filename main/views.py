from django.shortcuts import render, redirect
from .models import Attribute, Session
from .forms import *
# Create your views here.

def getSession(user):
    usr = Session.objects.get(user=user)
    return usr

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

        session = getSession(request.user)

        if not session.completed:
            # check form
            if request.method == "POST":
                attributes = request.POST.getlist("attributes")
                session.rScore = len(attributes)
                session.save()

                # redirect to the next page i.e investigative
                return redirect("main:iQ")
                # print score
                print(session.rScore)
            return render(request, 'main/questions.html', {"questions": realistic, "title": "Realistic"})
        else:
            return redirect("main:end_test")
    else:
        return redirect("accounts:login_user")
# investigative
def investigativeQ(request):
    # choices for realistic
    investigative = Attribute.objects.filter(holland_code=2)

    if request.user.is_authenticated:
        session = getSession(request.user)

        if not session.completed:
            # check form
            if request.method == "POST":
                attributes = request.POST.getlist("attributes")
                session.iScore = len(attributes)
                session.save()

                return redirect("main:aQ")
            return render(request, 'main/questions.html', {"questions": investigative, "title": "Investigative"})
    else:
        return redirect("accounts:login")
# artistic
def artisticQ(request):
    # choices for realistic
    artistic = Attribute.objects.filter(holland_code=3)

    # 
    if request.user.is_authenticated:
        session = getSession(request.user)
        
        if not session.completed:
            # check form
            if request.method == "POST":
                attributes = request.POST.getlist("attributes")
                session.aScore = len(attributes)
                session.save()

                # 
                return redirect("main:sQ")
            return render(request, 'main/questions.html', {"questions": artistic, "title": "Artistic"})
        else:
            return redirect("main:end_test")
    else:
        return redirect("accounts:home")

# social
def socialQ(request):
    # choices for realistic
    social = Attribute.objects.filter(holland_code=4)

    # check login
    if request.user.is_authenticated:
        session = getSession(request.user)
        if not session.completed:
            # check form
            if request.method == "POST":
                attributes = request.POST.getlist("attributes")
                session.sScore = len(attributes)
                session.save()

                return redirect("main:eQ")
            return render(request, 'main/questions.html', {"questions": social, "title": "Social"})
        else:
            return redirect("main:end_test")
    else:
        return redirect("accounts:login")

# enterprising
def enterprisingQ(request):
    # choices for realistic
    enterprising = Attribute.objects.filter(holland_code=5)

    # check login
    if request.user.is_authenticated:
        session = getSession(request.user)

        if not session.completed:
            # check form
            if request.method == "POST":
                attributes = request.POST.getlist("attributes")
                session.eScore = len(attributes)
                session.save()

                return redirect("main:cQ")
            return render(request, 'main/questions.html', {"questions": enterprising, "title": "Enterprising"})
        else:
            return redirect("main:end_test")
    else:
        return redirect("accounts:login")

# conventional
def conventionalQ(request):
    # choices for realistic
    conventional = Attribute.objects.filter(holland_code=6)
    if request.user.is_authenticated:
        session = getSession(request.user)

        if not session.completed:
            # check form
            if request.method == "POST":
                attributes = request.POST.getlist("attributes")
                session.cScore = len(attributes)
                session.save()

                return redirect("main:end_test")
                # at this point user should have the option to finish the quiz and should be prompted to change everything
            return render(request, 'main/questions.html', {"questions": conventional, "title": "Conventional"})

        else:
            return redirect("main:end_test")
    else:
        return redirect("accounts:login")



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

# ask for whether they want to end the result
def endTest(request):
    if request.user.is_authenticated:
        # get the user's session
        session = Session.objects.get(user=request.user)
        if session.completed == True:
            return redirect("main:results")
        else:
            session.completed = True
            session.save()
            return redirect("main:results")
    else:
        return rediret("accounts:login")
                # you cannot access this pge

# results page
def results(request):
    if request.user.is_authenticated:

        # get the session
        session = Session.objects.get(user=request.user)

        if session.completed == True:
            # seperate the results
            r = session.rScore
            i = session.iScore
            a = session.aScore
            s = session.sScore
            e = session.eScore
            c = session.cScore
            
            # create the dictionary of the itesms
            resultQuery = {
                "Realistic": r,
                "Investigative": i,
                "Artistic": a,
                "Social": s,
                "Enterprising": e,
                "Conventional": c
            }
            # keys
            keys = list(resultQuery.keys())

            # values
            values = list(resultQuery.values())
        

            reversedScore = sorted(resultQuery.items(), key=lambda kv: kv[1], reverse=True)
            top3 = reversedScore[:3]

            # create the link
            linkBuild = "https://www.onetonline.org/explore/interests/"

            # loop 
            listResults = []
            for top in top3:
                first = top[0]
                linkBuild += first + "/"
                listResults.append(first)
            
            # final verdict result
            verdict = ''
            for top in top3:
                character = top[0]
                verdict += character.capitalize() + ", "

            verdict = verdict[0:len(verdict)-2]

            # get context to display in the html view page
            context = {
                "verdict": verdict,
                "resultQuery": resultQuery,
                "listResults": listResults,
                "session": session,
                "keys": keys,
                "values": values,
                "linkBuild": linkBuild
            }

            # render the result template
            return render(request, 'main/results.html', context)
            # get top three out of the results
        else:
            return redirect("main:home")

        
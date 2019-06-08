from django.shortcuts import render
from .models import FeedbackData, ContactData, CoursesData
from .forms import FeedBackForm,ContactForm
from  django.http import HttpResponse
import  datetime
date1 = datetime.datetime.now()


def base1_view(request):
    return render(request,'base1.html')


def home_view(request):
    return render(request,'home.html')


def contact_view(request):
    if request.method == "POST":
        cform = ContactForm(request.POST)
        if cform.is_valid():
            name = cform.cleaned_data.get("name")
            email = cform.cleaned_data.get("email")
            mobile = cform.cleaned_data.get("mobile")
            courses = cform.cleaned_data.get("courses")
            shifts = cform.cleaned_data.get("shifts")
            loctions = cform.cleaned_data.get("locations")
            gender = cform.cleaned_data.get("gender")
            start_date = cform.cleaned_data.get("start_date")

            data = ContactData(
                name=name,
                email=email,
                mobile=mobile,
                courses=courses,
                shifts=shifts,
                locations=loctions,
                gender=gender,
                start_date=start_date
            )
            data.save()
            cform = ContactForm()
            return render(request,'contact.html',{'cform':cform})
        else:
            return HttpResponse("Invalid Input Data")
    else:
        cform = ContactForm()
        return render(request, 'contact.html', {'cform': cform})


def courses_view(request):
    courses = CoursesData.objects.all()
    return render(request,'courses.html',{'courses':courses})


def team_view(request):
    return render(request,'team.html')


def ourteam_view(request):
    return render(request,'ourteam.html')


def gallery_view(request):
    return render(request,'gallery.html')


def feed_back(request):
    if request.method == "POST":
        fform = FeedBackForm(request.POST)

        if fform.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')

            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform = FeedBackForm()
            fdata = FeedbackData.objects.all()
            return render(request, 'feedback.html', {"fform": fform, "fdata": fdata})

        else:
            return HttpResponse("Invalid User")
    else:
        fform = FeedBackForm()
        fdata = FeedbackData.objects.all()
        return render(request,'feedback.html',{"fform":fform,"fdata":fdata})
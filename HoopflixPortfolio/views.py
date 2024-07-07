from django.shortcuts import render
from HoopflixPortfolio.models import contactForm

def Hoopflix (request):
    return render(request, 'Hoopflix.html')

def Home (request):
    return render(request, 'Home.html')

def Portfolio (request):
    return render(request, 'Portfolio.html')

def Contacts (request):
    if request.method=='POST':
        FullName = request.POST['FullName']
        Email = request.POST['Email']
        Message = request.POST['Message']

        contact = contactForm(FullName=FullName, Email=Email, Message=Message)
        contact.save()
        print("the contact has been saved to the database")

    return render(request, 'Contacts.html')

from django.shortcuts import render
from .models import Appointments

# Create your views here.
def  show_all(request):
    context={}
    a=Appointments.objects.all()
    context['details'] = a
    print(a)
    template_name = 'task/testpage.html'
    return render(request, template_name, context)
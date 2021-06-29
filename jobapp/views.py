from django.shortcuts import render
from jobapp.models import hydjobs,bangjobs,chennijobs,punejobs
# Create your views here.


def home(request):
    return render(request,'jobapp/home.html')

def hydjobsinfo(request):
    job_list=hydjobs.objects.order_by('date')
    return render(request,'jobapp/hydjobs.html',context={'job_list':job_list})
def bangjobsinfo(request):
    job_list=hydjobs.objects.order_by('company')
    return render(request,'jobapp/bangjobs.html',context={'job_list':job_list})
def chennijobsinfo(request):
    job_list=hydjobs.objects.order_by('date')
    return render(request,'jobapp/hydjobs.html',context={'job_list':job_list})
def punejobsinfo(request):
    job_list=hydjobs.objects.order_by('date')
    return render(request,'jobapp/hydjobs.html',context={'job_list':job_list})

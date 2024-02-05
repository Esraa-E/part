from django.shortcuts import render

# Create your views here.
def secondfun(request):
    return render(request,'mySecondApplication/secondpage.html',{'message':'Hello from second application'})
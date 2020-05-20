from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Answer
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
	
	if request.method=="POST":
		name = request.POST['name']
		return render(request,'slambook.html',{'name':name})
	else:
		return render(request,'home.html')


def slambook(request):
    i = Answer()
    fs = FileSystemStorage()
    if request.method=="POST":
        i.image = request.FILES['image']
        i.filename = fs.save(i.image.name, i.image)
        i.uploaded_file_url = fs.url(i.filename)
        i.name = request.POST['name']
        i.relationship = request.POST['relationship']
        i.nick_name = request.POST['nick_name']
        i.like = request.POST['like']
        i.dislike = request.POST['dislike']
        
        i.video = request.FILES['video']
        i.filename1 = fs.save(i.video.name, i.video)
        i.uploaded_file_url1 = fs.url(i.filename1)
       
        i.gift = request.POST['gift']
        i.last_word = request.POST['last_word']
        i.message = request.POST['message']
        i.save()
        messages.info(request,"saved")
        return render(request, 'slambook.html', {'uploaded_file_url': i.uploaded_file_url })
        
        
    
        
def thank(request):
	return render(request,'thank.html')
	
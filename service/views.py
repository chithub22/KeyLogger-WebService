from django.shortcuts import render
from .models import Post
import os
# Create your views here.
def mainPage(request):
    post = Post.objects.all()
    return render(request,'service/indexPage.html', {'Post':post})
def SpyActive(request):
    return render(request,'service/SpyActive.html')
    
def read_file(request):
    f = open('static/log.txt', 'r')
    file_contents = f.read()
    if file_contents.find("space") > 0:
        f.write('\n')
    f.close()
    args = {'result' : file_contents }
    return render(request, "service/SpyActive.html", args)
from django.shortcuts import render, HttpResponse

def hello_teacher(request):
    return render(request, 'teacher/chatbox.html')
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, It's at the polls index.")

def detail(request, question_id):
    return HttpResponse('Here is the question %s.' %question_id)

def results(request, question_id):
    response = "Here is the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
    
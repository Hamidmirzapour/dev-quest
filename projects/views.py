from django.shortcuts import render
from django.http import HttpResponse

def get_projects(request):
    return HttpResponse('All the projects to show')

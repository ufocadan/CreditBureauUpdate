from django.shortcuts import render

def index(request):
    return render(request, 'scoring/index.html')

def questionnaire(request):
    return render(request, 'scoring/questionnaire.html')  # Create this template if not already present
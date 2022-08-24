from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'firstForm/index.html')

# def student_page(request):
#     return render(request,'firstForm/firstForm.html')
def student_page(request):
    print(request.POST)
    print(request.FILES)
    form = StudentForm()
    context ={
        'form': form 
    }
    return render(request,'firstForm/firstForm.html', context) 
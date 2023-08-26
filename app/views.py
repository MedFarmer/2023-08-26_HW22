from django.shortcuts import redirect, render
from django.conf import settings
from .models import Image, Student
from .forms import StudentForm
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
import os

def home(request):
    data = Image.objects.all()
    print(data)
    if request.method == 'POST':
        img = Image.objects.create(image = request.FILES['image'])
        img.save()
        return render(request, 'home.html', {'data':data})
    else:
        return render(request, 'home.html', {'data':data})
    
def delete(request, id):
    data = Image.objects.get(id=id)
    print(data.image)
    path = os.path.join(settings.MEDIA_ROOT, str(data.image))
    os.remove(path)
    data.delete()
    return redirect('home')

def students(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'students.html', context)

class StudentsCreate(FormView):
    template_name = 'add.html'
    form_class = StudentForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        grade = form.cleaned_data['grade']
        adding = Student(name=name, grade=grade)
        adding.save()
        
        return super().form_valid(form)
from django.shortcuts import render, redirect
from .models import Studentlar
from .forms import StudentForm

def studentlar_ruyxati(request):
    studentlar = Studentlar.objects.all()
    return render(request, 'studentlar_ruyxati.html', {'studentlar': studentlar})

def student_qushish(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ruyxat')

    return render(request, 'student_qushish.html', {'form': form})

def studentni_uchirish(request, id):
    uchirish = Studentlar.objects.get(id=id)
    if uchirish.name.lower() == 'firdavs':
        return redirect('ruyxat')

    uchirish.delete()

    return redirect('ruyxat')

def studentni_tahrirlash(request, id):
    student = Studentlar.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ruyxat')
    
    return render(request, 'studentni_tahrirlash.html', {'form': form})
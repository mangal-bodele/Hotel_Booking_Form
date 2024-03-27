from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Hotel
from .forms import HotelForm
@login_required(login_url='login_url')
def add_hotel(request):
    template_name = 'crud_app/add.html'
    form = HotelForm()
    if request.method =="POST":
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form':form}
    return render(request, template_name, context)
@login_required(login_url='login_url')
def show_hotel(request):
    template_name = 'crud_app/show.html'
    hotels = Hotel.objects.all()
    context = {'hotels':hotels}
    return render(request, template_name, context)

def update_hotel(request,pk):
    template_name='crud_app/add.html'
    obj = Hotel.objects.get(id=pk)
    form = HotelForm(instance=obj)
    if request.method == "POST":
        form = HotelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def cancel_hotel(request,pk):
    obj = Hotel.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request,'crud_app/confirm.html')




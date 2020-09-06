from django.shortcuts import render,redirect
from .models import Car
from .forms import CarForm
from django.contrib import messages
# Style your List and Detail views to use Bootstrap components.
# Now that your List and Detail views look all pretty, we can probably make them look even better if each object had an image. So, add a new field to the Car model called img and make sure the field stores images and is optional.
# Once you have the img field, make sure that the image gets displayed in the List and Detail views.
# Next, we want to complete our CRUD features. We still need the following views:
# Create view
# Update view
# Delete view
# The views have been partially written for you, complete them. You've also been provided with the URLs, so don't worry about that!
def car_list(request):
    cars = Car.objects.all()
    context = {
    "cars": cars,
    }
    return render(request, 'car_list.html', context)


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {
    "car": car,
    }
    return render(request, 'car_detail.html', context)




def car_create(request):
    form = CarForm()
    if request.method == "POST":
         form = CarForm(request.POST, request.FILES)
         if form.is_valid():
              form.save()
              messages.success(request, 'created successfully')
              return redirect('car-list')
    context = {
        "form":form,
        }
    return render(request, 'car_create.html', context)


def car_update(request, car_id):
    car_obj = Car.objects.get(id=car_id)
    form = CarForm(instance=car_obj)
    if request.method == "POST":
          form = CarForm(request.POST, request.FILES, instance=car_obj)
          if form.is_valid():
                form.save()
                messages.info(request, 'updated successfully.')
                return redirect('car-list')
    context = {
    "car_obj": car_obj,
    "form":form,
    }

    return render(request, 'car_update.html', context)



def car_delete(request, car_id):
    car_obj = Car.objects.get(id=car_id)
    car_obj.delete()
    messages.error(request, 'deleted successfully.')
    return redirect('car-list')

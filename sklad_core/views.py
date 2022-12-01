import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from flask import redirect
from .models import Truck, Product, InfoByDate
from accounts.models import User


from django.shortcuts import get_object_or_404
from .forms import TruckForm, ProductForm, ProductToEditForm, InfoByDateForm

def base(request):
    return render(request, 'sklad_temp/base.html')

def home(request):
    trucks = Truck.objects.all()
    form = TruckForm()
    user_truck = Truck.objects.get(store_emp_id=request.user.id)
    context = {
        'trucks' : trucks,
        'form':form,
        'usertruck':user_truck, 
    }
    return render(request, 'home.html', context)


def getDetails(request, pk):
    user = Truck.objects.get(pk = pk)
    products = Product.objects.filter(truck=user.pk)
    ovqatlar = Product.objects.filter(truck = user.pk, category='Ovqat')
    suvlar = Product.objects.filter(truck = user.pk, category='Suv')
    total_sum = sum([x.summ for x in products])

    context = {
        'ovqatlar':ovqatlar,
        'suvlar':suvlar,
        'total_sum' : total_sum,
        # 'infbd': infbd_form,
        'pk':pk,
        'truck_of_user':user,
        }
    
    return render(request, 'products.html', context)
    
def getDetailsTest(request, pk):
    user1 = Truck.objects.get(pk = pk)
    products1 = Product.objects.filter(truck=user1.pk)
    ovqatlar = Product.objects.filter(truck = user1.pk, category='Ovqat')
    suvlar = Product.objects.filter(truck = user1.pk, category='Suv')
    total_sum1 = sum([x.summ for x in products1])
    user = get_object_or_404(User, pk=request.user.id)
    truck = get_object_or_404(Truck, store_emp_id = user)
    usertr = Truck.objects.get(store_emp_id = request.user.id)
    products = Product.objects.filter(truck = usertr.pk)
    
    if request.method == "POST":
        form = InfoByDateForm(request.POST, user = truck)
        if form.is_valid():
            print('form is valid-------------------------')
            day = form.cleaned_data['day']
            dbday = InfoByDate.objects.get(truck_id = usertr, day = day)
            if dbday:
                print("already in db")
                dbday.delete()
                form.save()
                # return HttpResponse('success')
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)
            # print("-------------------",day)
            else:
                form.save()
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)
        print('form is not valid')
    else:
        form = InfoByDateForm(user = truck)
    context = {
        'ovqatlar':ovqatlar,
        'suvlar':suvlar,
        # 'infbd': infbd_form,
        'pk':pk,
        'truck_of_user':user1,
        # ---------------
        "form": form,
        "total_sum" : total_sum1,
        "usertr" : usertr,
        }
       
    return render(request, 'sample.html', context)

def add_truck(request):
    if request.method == "POST":
        form = TruckForm(request.POST)
        if form.is_valid():
            usrid = form.cleaned_data['store_emp_id']
            trid = Truck.objects.filter(store_emp_id = usrid)
            if trid:
                print('already in database', trid, '-------------------')
            else:
                truck = form.save()
                return HttpResponse(
                    status=204,
                    headers={
                        'HX-Trigger': json.dumps({
                            "movieListChanged": None,
                            "showMessage": f"{truck.name} added."
                        })
                    })
    else:
        form = TruckForm()
    return render(request, 'sklad_temp/truck_form.html', {
        'form': form,
    })

def create_product(request):
    template = 'add_prod.html'
    user = get_object_or_404(User, pk=request.user.id)
    truck = get_object_or_404(Truck, store_emp_id = user)
    print("user -----------", user)
    form = ProductForm(request.POST or None, user=truck)
    if form.is_valid():
        form.save()
        return redirect('detail')   

    context = {"form": form}

    return render(request, template, context)

def update_product(request, pk):
    template = 'editprod.html'
    book = get_object_or_404(Product, pk=pk)
    print("update---------------", book)
    form = ProductToEditForm()
    form = ProductToEditForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('detail')
    context = {"form": form}
    return render(request, template, context)    

def send_report(request):
    template = 'report.html'
    user = get_object_or_404(User, pk=request.user.id)
    truck = get_object_or_404(Truck, store_emp_id = user)

    usertr = Truck.objects.get(store_emp_id = request.user.id)
    products = Product.objects.filter(truck = usertr.pk)
    total_sum = sum([x.summ for x in products])
    print(usertr)
    form = InfoByDateForm(request.POST or None, user=truck)
    if form.is_valid():
        form.save()
        return redirect('detail')   

    context = {
        "form": form,
        "total_sum" : total_sum,
        "usertr" : usertr,
        }

    return render(request, template, context)

def truck_data(request, pk):
    data = InfoByDate.objects.filter(truck_id = pk)
    print(pk)
    context = {
        'otchet':data,
        'pk_id':pk,
    }
    return render(request, 'truck_data.html', context)


def bmonth(request, month, pk, year):
    
    data = InfoByDate.objects.filter(month=month, truck_id = pk, year = year)

    total_left_sum = sum([x.total_left for x in data])

    context = {
        "bmd": data,
        'ttls':total_left_sum,
        'trpk' : pk,
        'month':month,
        'year':year,
    }

    print([x.date for x in data])

    return render(request, 'bmonth.html', context)

def bday(request, month, pk, year, day):
    data = InfoByDate.objects.get(month=month, truck_id = pk, year = year, day=day)

    context = {
        'data' : data,
        'month':month,
        'trpk':pk,
        'year':year,
    }

    # return HttpResponse()
    return render(request, 'bday.html', context)


def delete_view(request, pk):

    context ={}
    obj = get_object_or_404(Product, pk = pk)
 
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("home")
 
    return render(request, "delete_view.html", context)
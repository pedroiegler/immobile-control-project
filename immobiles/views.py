from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from immobiles.models import Immobile, ImmobileImage, Customer
from .forms import CustomerForm, ImmobileForm, RegisterLocationForm

def create_customer(request):
    form = CustomerForm()

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('immobiles:list-customer')
        
    return render(request, 'immobiles/customer/create/index.html', {'form': form})

def list_customer(request):
    customers = Customer.objects.all().order_by('id')
    return render(request, "immobiles/customer/list/index.html", {'customers': customers})

def update_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('immobiles:list-customer') 
    
    return render(request, 'immobiles/customer/update/index.html', {'form': form, 'customer': customer})



def create_immobile(request):
    form = ImmobileForm()
    if request.method == 'POST':
        form = ImmobileForm(request.POST, request.FILES)
        if form.is_valid():
            immobile = form.save()
            files = request.FILES.getlist('immobile') 
            if files:
                for f in files:
                    ImmobileImage.objects.create(
                        immobile=immobile, 
                        image=f)
            return redirect('immobiles:list-immobile')  
    return render(request, 'immobiles/immobile/create/index.html', {'form': form})

def list_immobile(request):
    immobiles = Immobile.objects.filter(is_locate=False)
    context = { 'immobiles': immobiles }

    return render(request, 'immobiles/immobile/list/index.html', context)

def update_immobile(request, pk):
    immobile = get_object_or_404(Immobile, pk=pk)
    form = ImmobileForm(instance=immobile)

    if request.method == "POST":
        form = ImmobileForm(request.POST, instance=immobile)
        if form.is_valid():
            form.save()
            return redirect('immobiles:list-immobile') 
    
    return render(request, 'immobiles/immobile/update/index.html', {'form': form, 'immobile': immobile})


def create_register(request, id):
    get_locate = Immobile.objects.get(id=id) 
    form = RegisterLocationForm()  
    if request.method == 'POST':
        form = RegisterLocationForm(request.POST)
        if form.is_valid():
            location_form = form.save(commit=False)
            location_form.immobile = get_locate 
            location_form.save() 

            immo = Immobile.objects.get(id=id)
            immo.is_locate = True
            immo.save()

            return redirect('immobiles:list-immobile') 
    context = {'form': form, 'location': get_locate}
    return render(request, 'immobiles/register/create/index.html', context)


def list_report(request):
    immobile = Immobile.objects.all()  
    is_locate = request.GET.get("is_locate")
    get_type_item = request.GET.get("type_item")
    get_client = request.GET.get('client') 
    get_dt_start = request.GET.get('dt_start')
    get_dt_end = request.GET.get('dt_end')

    if get_client: 
        immobile = Immobile.objects.filter(
					Q(reg_location__client__name__icontains=get_client) | 
					Q(reg_location__client__email__icontains=get_client))
        
    if get_dt_start and get_dt_end: 
        immobile = Immobile.objects.filter(
						reg_location__created_on__range=[get_dt_start,get_dt_end])

    if is_locate:
        immobile = Immobile.objects.filter(is_locate=is_locate)

    if get_type_item:
        immobile = Immobile.objects.filter(type_item=get_type_item)

    return render(request, 'immobiles/report/list/index.html', {'immobiles': immobile})
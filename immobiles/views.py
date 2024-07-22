from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
    customers_count = customers.count()
    get_customer = request.GET.get("customer")

    if get_customer:
        customers = Customer.objects.filter(
            Q(name__icontains=get_customer) |
            Q(email__icontains=get_customer)
        )

    paginator = Paginator(customers, 10)
    page = request.GET.get("page")

    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    context = {
        'customers': customers, 
        'customers_count': customers_count,
    }
    
    return render(request, "immobiles/customer/list/index.html", context)

def update_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('immobiles:list-customer') 
    
    return render(request, 'immobiles/customer/update/index.html', {'form': form, 'customer': customer})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('immobiles:list-customer')


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
    immobile_count = immobiles.count()
    get_immobile = request.GET.get('immobile') 
    get_type_item = request.GET.get('type_item')

    if get_immobile:
        immobiles = Immobile.objects.filter(
            Q(code__icontains=get_immobile) |
            Q(address__icontains=get_immobile)
        )

    if get_type_item:
        immobiles = Immobile.objects.filter(type_item=get_type_item)

    paginator = Paginator(immobiles, 10)
    page = request.GET.get("page")

    try:
        immobiles = paginator.page(page)
    except PageNotAnInteger:
        immobiles = paginator.page(1)
    except EmptyPage:
        immobiles = paginator.page(paginator.num_pages)

    context = { 
        'immobiles': immobiles,
        'immobile_count': immobile_count,
    }

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

def delete_immobile(request, pk):
    immobile = get_object_or_404(Immobile, pk=pk)
    immobile.delete()
    return redirect('immobiles:list-immobile')

def delete_image(request, image_id):
    image = get_object_or_404(ImmobileImage, id=image_id)
    image.delete()
    return JsonResponse({'status': 'success'})

def create_register(request, id):
    get_locate = Immobile.objects.get(id=id)
    form = RegisterLocationForm()
    
    if request.method == 'POST':
        form = RegisterLocationForm(request.POST, request.FILES)
        if form.is_valid():
            location_form = form.save(commit=False)
            location_form.immobile = get_locate
            location_form.save()
            
            immo = Immobile.objects.get(id=id)
            immo.is_locate = True
            immo.save()

            return redirect('immobiles:list-report')
    
    images = ImmobileImage.objects.filter(immobile=id)
    images_data = [{"image_url": image.image.url} for image in images]
    images_count = len(images_data)

    context = {
        'form': form,
        'location': get_locate,
        'images_data': images_data,
        'images_count': images_count,
    }
    return render(request, 'immobiles/register/create/index.html', context)


def list_report(request):
    immobile = Immobile.objects.all()  
    is_locate = request.GET.get("is_locate")
    get_type_item = request.GET.get("type_item")
    get_client = request.GET.get('customer') 
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

    paginator = Paginator(immobile, 10)
    page = request.GET.get("page")

    try:
        immobile = paginator.page(page)
    except PageNotAnInteger:
        immobile = paginator.page(1)
    except EmptyPage:
        immobile = paginator.page(paginator.num_pages)

    return render(request, 'immobiles/report/list/index.html', {'immobiles': immobile})
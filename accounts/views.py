from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import orderForm, createUserForm , customerForm
from .filters import OrderFilter
from .decorators import authenticatedUser, allowedUser, admin_only



@authenticatedUser
def registerPage(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username') # for getting just username from the form
            group = Group.objects.get(name = 'customer') # fetching group to add the group with name customer
            user.groups.add(group)

            customer.objects.create(
                user = user,
            )
            


            messages.success(request, 'account is successfully created for ' + username)
            return redirect('loginPage')

    context = {'form':form}
    return render(request, 'accounts/Register.html', context)

@authenticatedUser
def loginPage(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('userPage')
        else:
            messages.info(request, 'username or password is incorrect')
            return render(request, 'accounts/Login.html', context)


    
    return render(request, 'accounts/Login.html', context)

    

@login_required(login_url = 'loginPage') # restricting to view home page without login

@admin_only
def home(request):
    customers = customer.objects.all()
    orders = order.objects.all()
    noOfOrders = orders.count()
    noOfCustomers = customers.count()

    pendingOrders = orders.filter(status = 'pending').count()
    deliveredOrders = orders.filter(status = 'delivered').count()

    context = {'orderList': orders , 'customerList' : customers, 'noOfOrders': noOfOrders, 'noOfCustomers': noOfCustomers, 
    'pendingOrders': pendingOrders, 'deliveredOrders': deliveredOrders }
    return render(request,'accounts/dashboard.html', context)



@login_required(login_url = 'loginPage')
@allowedUser(allowed_roles = ['admin'])

def products(request):
    products  = product.objects.all()


    return render(request,'accounts/products.html',{'productList': products})


@login_required(login_url = 'loginPage')
@allowedUser(allowed_roles = ['admin'])

def customers(request,pk):
    Customer = customer.objects.get(id = pk)
    Order = Customer.order_set.all()
    orderCount = Order.count()


    myFilter = OrderFilter(request.GET, queryset = Order)
    Order= myFilter.qs
    context = {'Customer': Customer, 'Order' : Order, 'orderCount': orderCount, 'myFilter': myFilter}
    return render(request,'accounts/customers.html', context)




@login_required(login_url = 'loginPage')
@allowedUser(allowed_roles = ['admin'])

def createOrder(request, pk):
    Customer = customer.objects.get(id = pk)
    inlineFormSet = inlineformset_factory(customer, order, fields = ('product','status'), extra = 10)
    orderForm = inlineFormSet(queryset = order.objects.none(), instance = Customer)

    # form = orderForm(initial = {'customer': Customer})
    if request.method == 'POST':
        #form = orderForm(request.POST)
        orderForm = inlineFormSet(request.POST, instance = Customer)

        if orderForm.is_valid():
            orderForm.save()
            return redirect('/')
    context = {'formset': orderForm}
    return render(request, 'accounts/orderForm.html' , context)



@login_required(login_url = 'loginPage')
@allowedUser(allowed_roles = ['admin'])

def updateOrder(request,pk):
    Order = order.objects.get(id = pk)
    form  = orderForm(instance = Order)
    if request.method == 'POST':
        form = orderForm(request.POST, instance = Order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/orderForm.html' , context)




@login_required(login_url = 'loginPage')
@allowedUser(allowed_roles = ['admin'])

def deleteOrder(request, pk):

    Order = order.objects.get(id = pk)
    if request.method == "POST":
        Order.delete()
        return redirect('/')

    context = {'item': Order}
    return render(request, 'accounts/delete.html', context)






@login_required(login_url = 'loginPage')
def logoutUser(request):
    logout(request)
    return redirect('loginPage')






@login_required(login_url = 'loginPage')
@allowedUser(allowed_roles = ['customer'])

def userPage(request):
    orders = request.user.customer.order_set.all()
    noOfOrders = orders.count()
    pendingOrders = orders.filter(status = 'pending').count()
    deliveredOrders = orders.filter(status = 'delivered').count()
    context = {'Order': orders, 'pendingOrders': pendingOrders, 'deliveredOrders': deliveredOrders , 'noOfOrders': noOfOrders }
    return render(request, 'accounts/user.html', context)


@login_required(login_url = 'loginPage')
@allowedUser(allowed_roles = ['customer'])
def settings(request):
    customer = request.user.customer
    Form = customerForm(instance = customer)
    context = {'Form': Form}
    if request.method == 'POST':
        Form = customerForm(request.POST, request.FILES, instance = customer)

        if Form.is_valid():

            Form.save()
            return redirect('settings')

    return render(request, 'accounts/setting.html', context)
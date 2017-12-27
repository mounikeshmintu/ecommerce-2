from django.shortcuts import render,get_object_or_404
from shop.forms import ContactForm,LoginForm,RegisterForm
from django.contrib.auth import authenticate,login
from django.views.generic import ListView
from shop.models import Product
# Create your views here.
def form(request):
    contact_form =ContactForm(request.POST or None)
    context={

        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)


    return render(request,"shop/index2.html",context)
def loginform(request):
    form = LoginForm()
    if form.is_valid():
        print("hey form is correct")
        susername = form.cleaned_data.get("username")
        spassword = form.cleaned_data.get("password")
        user= authenticate(request,username='susername',password='spassword')
        if user is not None:
            login(request,user)
    context={
        'login':form
    }
    return render(request,"shop/login.html",context)
def registerform(request):
    form = RegisterForm()
    if form.is_valid():
        print("hey form is correct")
        susername = form.cleaned_data.get("username")
        susername = form.cleaned_data.get("email")
        spassword = form.cleaned_data.get("password")
        spassword2 = form.cleaned_data.get("password2")
        # user= authenticate(request,username='susername',password='spassword')
        # if user is not None:
        #     login(request,user)
    context={
        'register':form
    }
    return render(request,"shop/register.html",context)
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_path='shop/product_list.html'

def product_list_view(request):
    queryset= Product.objects.all()
    context={
        'qs':queryset

    }
    return render(request,"shop/product_list.html",context)
class ProductDetailView(ListView):
    queryset = Product.objects.all()
    template_path='shop/product_list.html'

    def product_detail_view(request,ListView):
        instance=get_object_or_404(Product,pk=pk)
        context={
            'detailobj':instance

        }
        return render(request,"shop/product_list.html",context)

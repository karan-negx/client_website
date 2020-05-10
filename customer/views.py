import logging
_logger = logging.getLogger(__name__)
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView ,View
from .forms import SignUpForm, LoginForm, CustomerForm
from .models import Customer


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'customers/signup.html'

    def get(self,request):
        form = SignUpForm()
        return render(request,"customers/signup.html",{"form":form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        # _logger.error("request------------->%r",request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            pwd = request.POST.get("password")
            customer = Customer(email=email,password = pwd)
            customer.save()
            return HttpResponseRedirect(reverse('customer:login'))
        return render(request, "customers/signup.html",{"form":form})


class LogIn(View):

    def get(self,request, *args, **kwargs):
        form = LoginForm()
        return render(request,"customers/login.html",{"form":form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password")
            try:
                customer = get_object_or_404(Customer,username = username, password = password)
                _logger.error("customer ======> %r",customer)
            except Exception as e:  
                _logger.error("error =====> %r",str(e))
            else:
                customer_id = customer.id
                return HttpResponseRedirect(
                    reverse('customer:customer_view',kwargs={'id': customer_id}))
        return render(request, "customer/login.html",{"form":form})


class CustomerView(View):

    def get(self, request):
        return render(request, "customer/customer_dashboard.html")
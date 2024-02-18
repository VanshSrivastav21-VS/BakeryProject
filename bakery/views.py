from django.shortcuts import render, redirect
from .models import Product, MenuItem, Order, Category, ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login


def home(request):
    return render(request, 'bakery/home.html')

def menu(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'menu.html', {'products': products, 'categoryies': categories})

def order(request):
    if request.method == 'POST':
        produc_id = request.POST.get('menu_item_id')
        quantity = int(request.POST.get('quantity', 0))
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')

        menu_item = MenuItem.objects.get(pk=produc_id)
        order = Order.objects.create(
            menu_item=menu_item,
            quantity=quantity,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone
        )
        return redirect('order_confirm', order_id=order.pk)
    else:
        menu_items = MenuItem.objects.all()
        return render(request, 'order.html', {'menu_items': menu_items})
    
def order_confirm(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'home.html', {'order': order})

def about(request):
    return render(request, 'bakery/about.html')

def contact(request):
    if request.method == 'POST':
        # Process form submission
        # You can access form data using request.POST
        # For example:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the database or perform any other necessary actions

        # Example of saving the form data to a ContactForm model
        ContactForm.objects.create(name=name, email=email, message=message)

        # Display a success message
        messages.success(request, 'Your message has been sent successfully!')
        
        # Redirect to the contact page again or to a thank you page
        return redirect('contact')

    # If the request method is GET, render the contact page template
    return render(request, 'contact.html')

def submit_contact(request):
    if request.method == 'POST':
        # Process the form data
        # Example: Saving the form data to the database
        
        # Redirect to a success page
        return HttpResponseRedirect(reverse('home'))
    else:
        # Handle GET requests or other cases
        # Example: Render a form template
        return render(request, 'contact_form.html', contact)
    
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')  # Redirect back to signup page

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('signup')  # Redirect back to signup page

        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return redirect('signup')  # Redirect back to signup page

        # Create the new user
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()

        messages.success(request, "Account created successfully. You can now login.")
        return redirect('login')  # Redirect to login page after successful signup

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use the renamed login function
            return redirect('home')  # Redirect to the home page upon successful login
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')  # Redirect back to the login page
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return render('home')
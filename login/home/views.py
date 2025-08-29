from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.utils.dateparse import parse_date
from .models import Register
from .models import Register, Booking, Contact
from django.utils import timezone
from django.contrib import messages

# Register
def Register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        # Check if passwords match
        if password != confirm_password:
            return render(request, 'register.html', {'error': "Passwords do not match"})
        
        hashed_password = make_password(password)

        if Register.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': "Username already exists"})
        if Register.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': "Email already exists"})
        
        Register.objects.create(
            username=username,
            email=email,
            password=hashed_password
        )
        return redirect("home")  # after successful registration

    return render(request, "register.html")  # GET request → show form


# Login
def Login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me') == 'on'
        
        try:
            user = Register.objects.get(email=email)
            # Check hashed password
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                
                # Session expiry
                if remember_me:
                    request.session.set_expiry(2592000)  # 30 days
                else:
                    request.session.set_expiry(0)  # Until browser closes
                    
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': "Invalid credentials"})
        except Register.DoesNotExist:
            return render(request, 'login.html', {'error': "Invalid credentials"})
    
    return render(request, 'login.html')  # GET request → show login page


# Home
def home_view(request):
    if 'user_id' not in request.session:
        return redirect('login')   

    try:
        user = Register.objects.get(id=request.session['user_id'])
        return render(request, 'home.html', {'user': user})
    except Register.DoesNotExist:
        request.session.flush()  # clear session safely
        return redirect('login')


# Logout
def logout_view(request):
    request.session.flush()  
    return redirect('login')
from django.shortcuts import render


def book_view(request):
    if 'user_id' not in request.session:
        return redirect('login')  

    user = Register.objects.get(id=request.session['user_id'])

    if request.method == "POST":
        transport_type = request.POST.get("transport_type")  # Bus/Train/Flight
        from_station = request.POST.get("from_station")
        to_station = request.POST.get("to_station")
        journey_date = parse_date(request.POST.get("journey_date"))
        seats = int(request.POST.get("seats", 1))
        status = request.POST.get("status", "confirmed")  # ✅ Allow confirmed/cancelled

        if not journey_date:
            return render(request, "book.html", {"error": "❌ Invalid journey date"})

        Booking.objects.create(
            user=user,
            transport_type=transport_type,
            from_station=from_station,
            to_station=to_station,
            journey_date=journey_date,
            seats=seats,
            status=status
        )
        return render(request, "book.html", {"success": f"✅ {transport_type} ticket booked successfully!"})

    return render(request, "book.html")
def my_bookings_view(request):
    if 'user_id' not in request.session:
        return redirect('login')

    user = Register.objects.get(id=request.session['user_id'])
    bookings = Booking.objects.filter(user=user).order_by('-journey_date')

    return render(request, "my_bookings.html", {"bookings": bookings, "user": user})



def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.status = "Cancelled"
    booking.save()
    return redirect("my_bookings")
def contact_view(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to database
        Contact.objects.create(fullname=fullname, email=email, message=message)

        messages.success(request, " Your message has been sent successfully!")
        return redirect("contact") 

    return render(request, "contact.html")



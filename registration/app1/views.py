from django.shortcuts import render,HttpResponse,redirect
#manually added to import users from admin
from django.contrib.auth.models import User
#manually added to import vendors from models
# from models import Vendor
# from .models import Vendor
from django.db import connection
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
#24-5-23
from django.contrib import messages
# Create your views here.

# manually added as on 18/5/23
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')



from django.contrib import messages

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            messages.error(request, "Your Password and confirm password are not the same")
        else: 
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, "User created successfully!")
    
    return render(request, 'signup.html')




def LoginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message = "Username or Password incorrect"
            messages.error(request, error_message)
            
        
    return render(request,'login.html')

# def LoginPage(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('pass')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             error_message = "Username or Password incorrect"
#             return render(request, 'login.html', {'error_message': error_message})
        
#     return render(request, 'login.html')

# def LoginPage(request):
#     error_message = None  # Initialize error message variable

#     if request.method == "POST":
#         username = request.POST.get('username')
#         pass1 = request.POST.get('pass')
#         user = authenticate(request, username=username, password=pass1)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             error_message = "Username or Password incorrect"  # Set the error message

#     return render(request, 'login.html', {'error_message': error_message})




def LogoutPage(request):
    logout(request)
    return redirect('login')


# 22-5-23
#23-5-23
from django.http import HttpResponse, JsonResponse
@login_required(login_url='login')
def Insertvendor(request):
    if request.method == 'POST':
        vendor_name = request.POST.get('vendor_name')
        # vendor_code = request.POST.get('vendor_code')
        vendor_address = request.POST.get('vendor_address')
        vendor_gstin = request.POST.get('vendor_gstin')
        contact_number = request.POST.get('contact_number')
        email_id = request.POST.get('email_id')
        
        # vendor = Vendor(vendor_name=vendor_name,vendor_address=vendor_address, vendor_gstin=vendor_gstin, contact_number=contact_number, email_id=email_id)
        # vendor.save()
        
        cursor = connection.cursor()
        args = [vendor_name, vendor_address, vendor_gstin, contact_number, email_id]
        cursor.callproc('sp_testing', args)
        
        # Fetch results if needed // CHANGED THE CODE ON 23-5-23
        results = cursor.fetchall()
        cursor.close()
        if results :
          
            message = results[0][0]
            print(message)  # Assuming the message is returned as the first column of the first row
        else:
            message = None

        return render(request, 'insertvendor.html', {'message': message})

    return render(request, 'insertvendor.html')
    #     print(results)
        
    #     # Send a response to the frontend
    #     response_data = {
            
    #         'results': results
    #     }
    #     return JsonResponse(response_data)
    
    # return render(request, "insertvendor.html")

#23-05-23
@login_required(login_url='login')
def FormDetails(request):
    if request.method == 'POST':
        gst_no = request.POST.get('p_gstin_number')
        # ven_code = request.POST.get('p_vendor_code')
        hsn_code = request.POST.get('p_hsn_code')
        inv_num = request.POST.get('p_invoice_number')
        inv_date = request.POST.get('p_invoice_date')
        inv_value = request.POST.get('p_invoice_value')
        paid_status = request.POST.get('p_paid_status')
        qty = request.POST.get('p_qty')
        cost = request.POST.get('p_cost')
        prj_batchcode = request.POST.get('p_project_batch_code')
        finacial_year = request.POST.get('p_financial_year')
        # gstper = request.POST.get('p_gstper')
        igst = request.POST.get('p_igst')
        cgst = request.POST.get('p_cgst')
        sgst = request.POST.get('p_sgst')
        
        
        cursor = connection.cursor()
        args = [gst_no,hsn_code,inv_num, inv_date ,inv_value,paid_status,qty ,cost,prj_batchcode ,finacial_year,igst ,cgst,sgst]
        cursor.callproc('prdtesting', args)
        
        # Fetch results if needed
        results = cursor.fetchall()
        cursor.close()
        if results:
            message = results[0][0]  # Assuming the message is returned as the first column of the first row
        else:
            message = None

        return render(request, 'form.html', {'message': message})

    return render(request, 'form.html')



# just using to check the other pages in this used has dummy home.html -- create a base html once its crt.
def BaseView(request):
        
        return render(request,'base.html')



#<for GSTIN DETAILS TO BE DISPLAYED in website when they enter the user creditors gstin pin it will fetch all the data record ------30 05 2023--------------#>
from django.shortcuts import render
from django.db import connection

def Search_gstin(request):
    if request.method == 'POST':
        gstin_number = request.POST.get('gstin_number')

        # Call the stored procedure to fetch data from the MySQL database
        with connection.cursor() as cursor:
            cursor.callproc('sp_GetGSTINDetails', [gstin_number])  
            result = cursor.fetchall()

        # Pass the retrieved data to the template for rendering
        return render(request, 'gstindetails.html', {'result': result})

    return render(request, 'gstindetails.html')


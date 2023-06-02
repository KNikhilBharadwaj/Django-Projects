from django.shortcuts import render
from django.db import connection
from django.contrib import messages

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")
# =============================Vendor Form================================================
def insert(request):
    if request.method == "POST":
        Vendor_Name = request.POST.get('Vendor_Name')  
        Vendor_Address = request.POST.get('Vendor_Address')
        GSTIN_Number = request.POST.get('GSTIN_Number')
        Contact_Number = request.POST.get('Contact_Number')
        Vendor_Email_ID = request.POST.get('Vendor_Email_ID')
        print(Vendor_Name,  Vendor_Address, GSTIN_Number, Contact_Number, Vendor_Email_ID)

        args = [Vendor_Name, Vendor_Address, GSTIN_Number, Contact_Number, Vendor_Email_ID]

        try:
            cursor = connection.cursor()
            cursor.callproc('sp_creditors3', args)
            results = cursor.fetchall()
            cursor.close()

            if results:
                message = results[0][0]
            else:
                message = None

            return render(request, 'index.html', {'message': message})

        except Exception as e:
            # Handle the exception or display the error message
            error_message = str(e)
            return render(request, 'index.html', {'error_message': error_message})

    return render(request, "index.html")

# =========================Sundrycreditors Form===========================================================


def insert1(request):
    if request.method == "POST":
        gst = request.POST.get('gstin')  
        # vendorCode = request.POST.get('vendorCode')
        hsncode = request.POST.get('hsncode')
        invoicenumber= request.POST.get('invoicenumber')
        invoicedate = request.POST.get('invoicedate')
        paidstatus = request.POST.get('paidstatus')
        quantity= request.POST.get('quantity')
        cost= request.POST.get('cost')
        projectbatchcode= request.POST.get('projectbatchcode')
        financialyear= request.POST.get('financialyear')
        GSTPercentage= request.POST.get('GSTPercentage')
        CGST= request.POST.get('CGST')
        SGST= request.POST.get('SGST')
        IGST= request.POST.get('IGST')
    
        print(projectbatchcode,financialyear,GSTPercentage,CGST,SGST,IGST,gst, hsncode, invoicenumber, invoicedate, paidstatus,quantity,cost)

        args = [projectbatchcode,financialyear,GSTPercentage,CGST,SGST,IGST,gst, hsncode, invoicenumber, invoicedate, paidstatus,quantity,cost]

        try:
            cursor = connection.cursor()
            cursor.callproc('tbl_productgenerator12345', args)
            results = cursor.fetchall()
            cursor.close()

            if results:
                message = results[0][0]
            else:
                message = None

            return render(request, 'page2.html', {'message': message})

        except Exception as e:
            # Handle the exception or display the error message
            error_message = str(e)
            return render(request, 'page2.html', {'error_message': error_message})

    return render(request, "page2.html")
# ==========================================================================================================insert==============


def fixednav(request):
    return render(request, "fixednav.html")

def page2(request):
    return render(request, "page2.html")



# ==============================================================================
# from django.shortcuts import render
# # from .models import Ultimate
# from django.db import connection
# from django.contrib import messages


# def home(request):
#     return render(request, "home.html")

# def index(request):
#     return render(request, "index.html")

# def insert(request):
#     if request.method == "POST":
#         Vendor_Name = request.POST.get('Vendor_Name')  
#         Vendor_Code = request.POST.get('Vendor_Code')
#         Vendor_Address = request.POST.get('Vendor_Address')
#         GSTIN_Number = request.POST.get('GSTIN_Number')
#         Contact_Number = request.POST.get('Contact_Number')
#         Vendor_Email_ID = request.POST.get('Vendor_Email_ID')
#         print(Vendor_Name, Vendor_Code, Vendor_Address, GSTIN_Number, Contact_Number, Vendor_Email_ID)
          
#         # query = Ultimate(Vendor_Name=Vendor_Name, Vendor_Code=Vendor_Code, Vendor_Address=Vendor_Address, GSTIN_Number=GSTIN_Number, Contact_Number=Contact_Number, Vendor_Email_ID=Vendor_Email_ID)
#         # query.save()

#         args = [Vendor_Name, Vendor_Code, Vendor_Address, GSTIN_Number, Contact_Number, Vendor_Email_ID]
        
#         cursor = connection.cursor()
#         cursor.callproc('sp_creditors1', args) 
#         # res = cursor.callproc('sp_name', args)
#         results = cursor.fetchall()
#         cursor.close()
#         if results:
#             message = results[0][0]  # Assuming the message is returned as the first column of the first row
#         else:
#             message = None

#         return render(request, 'index.html', {'message': message})
#         # print(results)
#         # # messages.success(request,'Data is Submited Succefully...!!')

#     return render(request, "index.html")
    

# def page2(request):
#     return render(request, "page2.html")

# def fixednav(request):
#     return render(request, "fixednav.html")

from django.shortcuts import render,HttpResponse,redirect
from .models import Hospital,Asset,Complaint_history,PurchaseOrder
# from Synergy.forms import Asset
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from .forms import UserLoginForm,ComplaintForm,updatecomplaintform,updateuserform,UserRegisterForm,PurchaseOrderform

from django.core.mail import send_mail , get_connection,EmailMessage
import random
from django.conf import settings

import razorpay
from django.conf import settings

# # Create your views here.

def home(request):
    return render(request,'home.html')

def index(request):
    if request.user.is_authenticated:

        u = Hospital.objects.filter(user = request.user)

        context = {'u' : u}

        return render(request,'index.html', context)
    
    else:

        return render(request, 'index.html')



@login_required(login_url='/login')
def addHospital(request):
    if request.method == "GET":
        u = User.objects.all()

        context = {'data':u}
        return render(request,'addhospital.html',context)
    else:
        user = request.POST['user']

        u = User.objects.get(username = user)
        # username = request.POST["user"]
        hospital_name = request.POST["hospital_name"]
        contact = request.POST["contact"]
        address = request.POST["address"]
        pincode = request.POST["pincode"]
        admin_name = request.POST["admin_name"]

       
    obj = Hospital.objects.create(user=u,hospital_name=hospital_name, contact=contact,address=address,
                              pincode=pincode,admin_name=admin_name)
    obj.save()

    return redirect('/addhospital/view')



def update_hospital(request, id):
    if request.method == 'GET':
        hospital = Hospital.objects.get(id=id)
        user = User.objects.all()
        context = {'hospital': hospital}
        context['users'] = user
        return render(request, 'updatehospital.html', context)
    
    else:
        hospital = Hospital.objects.get(id=id)
        user_id=request.POST['user']
        u = User.objects.get(id = user_id)
        hospital.user = u
        hospital.hospital_name = request.POST['hospital_name']
        hospital.contact = request.POST['contact']
        hospital.address = request.POST['address']
        hospital.pincode = request.POST['pincode']
        hospital.admin_name = request.POST['admin_name']
        hospital.save()
        return redirect('/addhospital/view')
  
    
@login_required(login_url='/login')
def deleteHospital(request, id):
    hospital = Hospital.objects.filter(id=id)
    if hospital.exists():
        hospital.delete()
    return redirect('/addhospital/view')



def readhospital(request):
    hosp = Hospital.objects.all()
    context = {'data':hosp}
    
    return render(request,'showhospital.html',context)

@login_required(login_url='/login')
def add_asset(request):
    if request.method == "GET":
        hospitals = Hospital.objects.all()

        context = {'data':hospitals}
        return render(request,'addAsset.html',context)
    
    else:
        hosptial = request.POST['hospital_name']

        hos = Hospital.objects.get(id = hosptial)


        asset_name = request.POST["asset_name"]
        asset_type =request.POST["asset_type"]
        purchase_date = request.POST["purchase_date"]
        warranty_start_date = request.POST["warranty_start_date"]
        contract_end_date = request.POST["contract_end_date"]
        contract_type = request.POST["contract_type"]
        installed_at = request.POST["installed_at"]
        status = request.POST["status"]
        
       
    obj = Asset.objects.create( hospital = hos,asset_name= asset_name,asset_type=asset_type, purchase_date=purchase_date, warranty_start_date=warranty_start_date,
                              contract_end_date=contract_end_date,contract_type=contract_type,installed_at=installed_at,status=status)
    obj.save()
    return redirect('/asset/view')   #hospital_id=hospital_id

def update_asset(request, id):
    if request.method == 'GET':
        asset = Asset.objects.get(id=id)
        hospitals = Hospital.objects.all()
        context = {
            'asset': asset,
            'hospitals': hospitals
        }
        return render(request, 'updateasset.html', context)
    
    else:
        asset = Asset.objects.get(id=id)
        asset.hospital_id = request.POST['hospital']
        asset.asset_name = request.POST['asset_name']
        asset.asset_type = request.POST['asset_type']
        asset.purchase_date = request.POST['purchase_date']
        asset.warranty_start_date = request.POST['warranty_start_date']
        asset.contract_end_date = request.POST['contract_end_date']
        asset.contract_type = request.POST['contract_type']
        asset.installed_at = request.POST['installed_at']
        asset.status = request.POST['status']
        asset.save()
        return redirect('/asset/view')


@login_required(login_url='/login')
def deleteAsset(request,id):
    asset = Asset.objects.filter(id=id)
    if asset.exists():
        asset.delete()
    return redirect('/asset/view')





# def readAsset(request):
#     asset = Asset.objects.all()
#     context = {'data':asset}
    
#     return render(request,'AssetDetails.html',context)
def readAsset(request):
    
    if request.user.is_superuser:
        hospital = Hospital.objects.all()
        assets = Asset.objects.all()
        context = {
            'hospital': hospital,
            'assets': assets,
        }
        
        
        return render(request, 'AssetDetails.html', context)
    
    elif request.user.is_staff:

        hospital = Hospital.objects.get(user = request.user)
        assets = Asset.objects.filter(hospital = hospital)
        
        context = {
            'hospital': hospital,
            'assets': assets,
        }
        return render(request, 'AssetDetails.html', context)
    else:

        return HttpResponse("You are not authorized")


def hospitalAsset(request, hospital_id):
    hospital = Hospital.objects.get(id=hospital_id)
    assets = Asset.objects.filter(hospital=hospital)
    context = {
        'hospital': hospital,
        'assets': assets,
    }
    return render(request, 'hospital_assets.html', context)
  
 
def userRegister(request):
    if request.method == "GET":
        form = UserRegisterForm()
        context = {'form':form}
        return render(request,'register.html',context)

    else:

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            password = form.cleaned_data['password']
            confirmPassword = form.cleaned_data['confirmPassword']

            if password == confirmPassword:

                user = form.save(commit = False) # purpose of commit is that the data dosen't get saved
                                                 # in data base ,only in user variable
                user.set_password(password) # this statement sets password in star/hash format
                
                user.save()                 # this statement saves data in database
                
                return redirect('/')

        else:

            return HttpResponse('form not saved')

# def userLogin(request):
#     if request.method == 'GET':
#         form = UserLoginForm()
#         context = {'form': form}
#         return render(request, 'UserLogin.html', context)
#     else:
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
            

#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 return HttpResponse('Username or password is incorrect')
#         else:
#             return render(request, 'UserLogin.html', {'form': form})

def userLogin(request):
    if request.method == 'GET':
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'UserLogin.html', context)
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            x = User.objects.get(username = username)
            
            u = Hospital.objects.filter(user=x)

            print(u)
            context = {}
            context['u']=u
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('Username or password is incorrect')
        else:
            return HttpResponse("Not a Valid Data")

def userLogout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login')
def readuser(request):
    users = User.objects.get(user=users)
    context = {'data': users}
    return render(request, 'showuser.html', context)

def updateuser(request, rid):
    if request.method == 'GET':
        user = User.objects.get(id=rid)
        form = updateuserform(instance=user)
        context = {'form': form}
        return render(request, 'updateuser.html', context)
    else:
        user = User.objects.get(id=rid)
        form = updateuserform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/users/view')
        else:
            return HttpResponse('User Not Saved')
        


@login_required(login_url='/login')
def add_complaint(request):
    hospitals = Hospital.objects.all()
    assets = Asset.objects.all()
    
    if request.method == 'GET':
        form = ComplaintForm()

        context = {
            'form': form,
            'hospitals': hospitals,
            'assets': assets
        }
        return render(request, 'add_complaint.html', context)
    elif request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/complaints/view')
        else:
            print(form.errors)
            context = {
                'form': form,
                'hospitals': hospitals,
                'assets': assets
        }
        return render(request, 'add_complaint.html', context)
    





@login_required(login_url='/login')
def update_complaint(request,rid):
    # complaint = Complaint_history.objects.filter(id=id).first()
    if request.method == 'GET':
        complaint = Complaint_history.objects.get(id = rid)
        print(complaint)
        form = updatecomplaintform(instance=complaint)
        context = {'form': form}
        print("error")
        return render(request,'update_complaint.html',context)
    
        # form.fields['hospital'].initial = complaint.hospital     // if instance used form.fields does not use
        # form.fields['asset'].initial = complaint.asset
        # form.fields['problem_description'].initial = complaint.problem_description
        # form.fields['service_report'].initial = complaint.service_report
        # form.fields['date_reported'].initial = complaint.date_reported
        # form.fields['date_resolved'].initial = complaint.date_resolved
        # form.fields['resolved'].initial = complaint.resolved
        # form.fields['resolution_note'].initial = complaint.resolution_note
        # form.fields['status'].initial = complaint.status


    else:
        complaint = Complaint_history.objects.get(id = rid)
        form = updatecomplaintform(request.POST,request.FILES,instance=complaint)

        if form.is_valid():
            form.save()
            return redirect('/complaints/view')
        
        else:
            return HttpResponse('complaint Not Saved')


@login_required(login_url='/login')
def delete_complaint(request, id):
    complaint = Complaint_history.objects.filter(id=id)
    if complaint.exists():
        complaint.delete()
    return redirect('/complaints/view')

# @login_required(login_url='/login')
# def read_complaints(request):
#     complaints = Complaint_history.objects.all()
#     context = {'complaints': complaints}
#     return render(request, 'complaint_list.html', context)

def read_complaints(request):
    
    if request.user.is_superuser:
        complaints = Complaint_history.objects.all()
        context = {'complaints': complaints}
        return render(request, 'complaint_list.html', context)
        
    elif request.user.is_staff:

        hospital = Hospital.objects.get(user = request.user)
        complaints = Complaint_history.objects.filter(hospital = hospital)
        
        context = {'complaints': complaints}

        return render(request, 'complaint_list.html', context)
    else:

        return HttpResponse("You are not authorized")



@login_required(login_url='/login')
def asset_complaints(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    print("error")
    complaints = Complaint_history.objects.filter(asset=asset)
    context = {'asset': asset, 'complaints': complaints}
    return render(request, 'asset_complaints.html', context)        

def buy_equipment(request):
    client = razorpay.Client(auth=(settings.KEY_ID,settings.KEY_SECRET))
    payment = client.order.create({'amount':500*100,'currency':'INR','payment_capture':1})
    context = {'data':payment}
    context['amount'] = int(500*100)
    return render(request,'payment.html',context)
    #return render(request,'payment.html')



@login_required(login_url='/login')
def addPurchaseOrder(request):
    if request.method == "GET":
        form = PurchaseOrderform()
        context = {'form':form}
        return render(request,'addequipment.html',context)
    else:
        form = PurchaseOrderform(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('/equipment/view')
        else:
            context = {'error':'product not saved'}
            print(form.cleaned_data['assetname'])
            print(form.cleaned_data['discription'])
            print(form.cleaned_data['supplier'])
            print(form.cleaned_data['total_cost'])
            return HttpResponse("Data Not valid")



def readorder(request):
    order = PurchaseOrder.objects.all()
    context = {'data':order}
    
    return render (request,'showequipment.html',context)
# ---------------------------------------------------------------------------------------------------

def forgot_password(request):
    if request.method == "GET":

        return render(request,'emailreturn.html')

    else:

        email = request.POST['email']

        request.session['email'] = email

        user = User.objects.filter(email = email).exists()

        if user:

            otp = random.randint(1000,9999)

            request.session['email_otp'] = otp



            with get_connection(

                host = settings.EMAIL_HOST,
                port = settings.EMAIL_PORT,
                username = settings.EMAIL_HOST_USER,
                password = settings.EMAIL_HOST_PASSWORD,
                use_tls = settings.EMAIL_USE_TLS
            ) as connection:

                subject = "OTP Verification"
                email_from = settings.EMAIL_HOST_USER
                recipetion_list = [ email ]
                message = f"OTP is {otp}"   # "OTP is "+ otp

            EmailMessage(subject,message,email_from, recipetion_list,connection = connection).send()

            # return HttpResponse("Email Send")
            return redirect('/verify_otp')
 
        else:

            return HttpResponse("user not registered")   


def verify_otp(request):

    if request.method == "GET":

        return render(request,'otpverification.html')

    else:
        user_otp = int(request.POST['otp'])

        email_otp = int(request.session['email_otp'])

        print("user otp:",user_otp)
        print("email otp:",email_otp)

        if user_otp == email_otp:

            return redirect('/change_password')

                

                # return HttpResponse('ok')
        else:

            return redirect('/forgot_password')



def change_password(request):

    if request.method == "GET":

        return render(request,'newpassword.html')

    else:

        email = request.session['email']

        password = request.POST['password']

        confirmPassword = request.POST['confirmpassword']

        if password == confirmPassword:

            user = User.objects.get(email = email)

            user.set_password(password)

            user.save()

            return redirect('/login')
            #return HttpResponse("Password changed")

        else:

            return HttpResponse("password and confirm Password does not match")
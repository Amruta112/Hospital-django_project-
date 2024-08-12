from django import forms
from Synergy.models import Hospital, Asset,Complaint_history,PurchaseOrder
from django. contrib.auth.models import User



# class UpdateHospitalForm(forms.ModelForm):
#     class Meta:
#         model = Hospital
#         fields = ['hospital_name', 'contact', 'address', 'pincode', 'admin_name']

# class AssetForm(forms.ModelForm):
#     class Meta:
#       model = Asset
#       fields = ['hospital','asset_name','asset_type','purchase_date','warranty_start_date','contract_end_date','contract_type',
#                 'installed_at','status']
#       exclude = []


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    confirmPassword = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password','confirmPassword']
        exclude = []




class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget = forms.PasswordInput)


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint_history
        fields = ['hospital','asset', 'problem_description', 'service_report', 'date_reported', 'date_resolved', 'resolved', 'resolution_note', 'status']

class updatecomplaintform(forms.ModelForm):
    class Meta:
        model = Complaint_history
        fields = ['hospital','asset','problem_description','service_report','date_reported','date_resolved','resolved','resolution_note','status']
        exclude = []        

class updateuserform(forms.ModelForm):
    class Meta:
        model = User
        feilds = ['username','password']
        exclude = []
 
class PurchaseOrderform(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        feilds = ['assetname','discription','supplier','total_cost']
        exclude = []
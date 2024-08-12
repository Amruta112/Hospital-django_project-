from django.contrib import admin
from django.urls import path
from Synergy import views

urlpatterns = [
    path('', views.index),
    path('login/', views.userLogin),
    path('logout/', views.userLogout),
    path('users/view', views.readuser),
    path('addhospital/', views.addHospital),
    path('updatehospital/<id>/', views.update_hospital),
    path('deletehospital/<id>/', views.deleteHospital),
    path('addhospital/view', views.readhospital),
    path('addasset/', views.add_asset),
    path('updateasset/<id>/', views.update_asset),
    path('deleteasset/<id>/', views.deleteAsset),
    path('asset/view', views.readAsset),
    path('users/view', views.readuser),
    path('register',views.userRegister),
    path('updateuser/<rid>/', views.updateuser),
    # path('respectedAsset/<rid>',views.hospitalAsset),
    path('respectedAsset/<hospital_id>', views.hospitalAsset),
    path('addcomplaints/', views.add_complaint),
    path('complaints/update/<rid>', views.update_complaint),
    path('deletecomplaints/<id>', views.delete_complaint),
    path('complaints/view/', views.read_complaints),
    path('complaints/asset/<asset_id>', views.asset_complaints),
    path('buy/',views.buy_equipment),
    path('addequipment/',views.addPurchaseOrder),
    path('equipment/view/',views.readorder), 

    path('forgot_password',views.forgot_password),
    path('verify_otp',views.verify_otp),
    path('change_password',views.change_password),
    path('home',views.home)

]



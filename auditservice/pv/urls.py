from django.urls import path
from django.contrib.auth import  views as auth_views

from . import views

app_name ='pv'

urlpatterns = [
        # path('',views.login_view, name='log'),
        path('logout', views.logout_request, name="logout"),
        path('change-password/', views.change_password, name='change_password'),
        path('dashboard/',views.Dashboard.as_view(), name='dashboard'),
        path('principal/', views.PrincipalDash, name ='principal'),
        path('pv/register/',views.PvCreateView, name ='pv-register'),
        path('pv/honurarium/',views.HunCreateView, name = 'pv-honurarium'),
        path('pv/benefit/', views.benefitCreateView.as_view(),name = 'pv-benefit'),
        path('userdash/', views.UserDash, name ='userdash'),
        path('usersearch/', views.Usersearch, name ='usersearch'),
        path('principalsearch/', views.Prinsearch, name ='princsearch'),
        path('registeredpv/', views.PvList.as_view(), name ='registeredpv'),
        path('movedtochest/', views.Total_moved_to_chest.as_view(), name ='movetochest'),

        path('pv/<int:pk>/update',views.PvUpdateView.as_view(), name ='pvupdate'),
        path('pv/<int:pk>/update/honurarium',views.HunUpdateView.as_view(), name ='hunupdate'),
        path('pv/<int:pk>/update/honurarium/benefit',views.BenefitUpdateView.as_view(), name ='benefithunupdate'),
        # path('pv/<int:pk>/standardupadte',views.standardPvUpdateView.as_view(), name ='pvupdatestandard'),
        path('pv/<int:pk>',views.PvDetailView.as_view(), name ='pv-detail'),
        path('pv/<int:pk>/hon',views.HonDetailView.as_view(), name ='hondetails'),
        # path('pv/<int:pk>',views.PvDetailprintView.as_view(), name ='pv-print'),
        path('pv/registedmonth/', views.Total_Processed_PV.as_view(), name ='monthlyregistedpv'),
        path('pv/completedmonth/', views.Total_completed_PV.as_view(), name ='monthlycompletedpv'),
        path('pv/returnedmonth/', views.Total_returned_PV.as_view(), name ='monthlyreturnedpv'),
        path('pv/cancelledmonth/', views.Total_cancelled_PV.as_view(), name ='monthlycancelledpv'),
        path('pv/withoding/', views.Total_withholding_PV.as_view(), name ='withholding'),

        path('pv/nonwithoding/', views.Nonwitholding.as_view(), name ='nonwithholding'),
        path('pv/accountableimpress/',views.accountableimpress.as_view(), name ='accimpress'),
        path('pv/nonaccountableimpress/',views.nonaccountableimpress.as_view(), name ='nonaccimpress'),
        path('pv/search/',views.Search, name ='search'),

        path('pv/registeredp/csv',views.getfile, name= 'registedcsv'),
        path('pv/total/csv',views.totalfile, name= 'totalregisteredcsv'),
        path('pv/completedpv/csv',views.completedfile, name= 'completedpvcsv'),
        path('pv/returneddpv/csv',views.returnedfile, name= 'returnedpvcsv'),
        path('pv/cancelledpv/csv',views.cancelledfile, name= 'cancelledcsv'),
        path('pv/withholding/csv',views.withholdingtax, name= 'withholdingtaxcsv'),
        path('pv/nonwithholding/csv',views.Nonwitholdings, name= 'nonwithholdingtaxcsv'),
        path('pv/accountableimpress/csv',views.accountableimpresss, name= 'accountableimpresscsv'),
        path('pv/nonaccountableimpress/csv',views.nonaccountableimpresss, name= 'nonaccountableimpresscsv'),
        path('pv/beneficiaries/csv',views.beneficiariess, name= 'beneficiariescsv'),
        path('pv/movetochest/csv',views.chestcsv, name= 'movetochestcsv'),

      ]
 

  
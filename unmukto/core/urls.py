from django.urls import path
from .views import AccountInformationListCreateView, ResetPasswordCreateView, LoginCreateView, IncidentListCreateView, PriceListView

urlpatterns = [
    path('api/account-info/', AccountInformationListCreateView.as_view(), name='account_information_list_create'),
    path('api/reset-password/', ResetPasswordCreateView.as_view(), name='reset_password_form_create'),
    path('api/login/', LoginCreateView.as_view(), name='login_form_create'),
    path('api/incidents/', IncidentListCreateView.as_view(), name='incident_list_create'),
    path('api/prices/', PriceListView.as_view(), name='price_list'),
]
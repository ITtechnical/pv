import django_filters
from django import forms
from django_filters import DateFilter , CharFilter
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class PvFilter(django_filters.FilterSet):
    Pv_reference = CharFilter(field_name='Pv_reference',lookup_expr='exact')
    start_date =DateFilter(field_name="Date_recieved",lookup_expr='gte',label='Start Date',
                           widget=DateInput(
                               attrs={
                                   'class': 'datepicker'
                               }
                           )

                           )
    end_date =DateFilter(field_name="Date_recieved",lookup_expr='lte',label='End Date',
                           widget=DateInput(
                               attrs={
                                   'class': 'datepicker'
                               }
                           ))

    class Meta:
        model = Pv
        fields = ['Pv_reference','Type_of_pv','Status','start_date','end_date']


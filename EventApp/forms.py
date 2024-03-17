from django import forms
from . models import*

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'customer_name':forms.TextInput(attrs={"placeholder":"Enter your name","style": "width:300px;height:35px"}),
            'customer_phone':forms.TextInput(attrs={"placeholder":"Enter phone number","style": "width:300px;height:35px"}),
            'booking_date':DateInput()
            }

        labels={
            'customer_name':"Customer Name:",
            'customer_phone':"Customer Phone:",
            'name':"Event Name:",
            'booking_date':"Booking Date:",
        }
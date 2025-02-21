from django import forms 
from . models import Booking
class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        
        widgets={
            'booking_date':DateInput(),
        }
        
        labels={
            'std_name':"Student Name:",
            'std_phn':"Student Phone:",
            'name':"Event Name:",
            'booking_date':"Booking Date:",
        }
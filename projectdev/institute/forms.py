from django import forms
from multiselectfield import MultiSelectFormField

class FeedBackForm(forms.Form):
    name = forms.CharField(
        label="Enter your Name",
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label='Enter your Rating',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter your Fedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'your feedback'
            }
        )
    )


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Enter YOUR Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )

    email = forms.EmailField(
        label="Enter YOUR Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }
        )
    )

    mobile = forms.IntegerField(
        label="Enter YOUR Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Mobile Number'
            }
        )
    )

    COURSES_CHOCIES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('ui', 'UI'),
        ('rest', 'Rest API')
    )
    courses = MultiSelectFormField(max_length=200,choices=COURSES_CHOCIES)

    SHIFT_CHOICES = (
        ('mrg', 'Morning'),
        ('aftn', 'AfterNoon'),
        ('evng', 'Evening'),
        ('night', 'Night')
    )
    shifts = MultiSelectFormField(max_length=200,choices=SHIFT_CHOICES)

    LOCATION_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Banglore'),
        ('che', 'Chennai'),
        ('pune', 'Pune')
    )
    location = MultiSelectFormField(max_length=200,choices=LOCATION_CHOICES)

    GENDER_CHOICES = (
        ('m','Male'),
        ('f','Female')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(),choices=GENDER_CHOICES
    )
    start_date = forms.DateField(
        widget=forms.SelectDateWidget()
    )
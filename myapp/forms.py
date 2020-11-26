from django import forms

list1 = [('M','Male'),('F','Female')]
class StudentForm (forms.Form):
    Name = forms.CharField(label='Name',required=True)
    Address = forms.CharField(label='Address',widget=forms.Textarea)
    Gender = forms.ChoiceField(choices=list1,widget=forms.RadioSelect)
    FileUpload = forms.FileField()

    def clean_Name(self):
        value = self.cleaned_data['Name']
        if value.isupper():
            raise forms.ValidationError('Name must be lowercase')
        return value

class MailSendingForm(forms.Form):
    subject = forms.CharField()
    message = forms.CharField()
    frommail= forms.CharField()
    tomail = forms.CharField()
    attachment = forms.FileField()


class ContactLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

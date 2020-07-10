from django import forms
from pv.models import Pv
from django.contrib.auth import authenticate, get_user_model
from .import models
from pv.models import Staff
from datetime import date
# from .widget import XDSoftDateTimePickerInput
User = get_user_model()

class DateInput(forms.DateInput):
    input_type = 'date'

class GeneralpvForm(forms.ModelForm):

    def clean(self,*args, **kwargs):
        today = date.today()
        pvtype = self.cleaned_data.get('Type_of_pv')
        tochest = self.cleaned_data.get('returned_to_chest')
        status = self.cleaned_data.get('Status')
        returndate = self.cleaned_data.get('Date_returned')
        Daterecieved = self.cleaned_data.get('Date_recieved')
        Datereturn = self.cleaned_data.get('Date_returned')
        remarks = self.cleaned_data.get('Remarks')
        net = self.cleaned_data.get('Net_amount')
        if pvtype:
            if pvtype != "General":
                raise forms.ValidationError({'Type_of_pv': ["Please Chose General in the Type of Pv",]})
            elif status == "Returned" and not returndate:
                raise forms.ValidationError({'Date_returned': ["Please Enter Date Retured To Accounts",]})
            elif status != "Returned" and returndate:
                raise forms.ValidationError({'Date_returned': ["Please remove date returned",]})
            elif net < 0 :
                raise forms.ValidationError({'Net_amount': ["Net Amount cannot be less than 0",]})
            elif tochest > 0.00 and not remarks:
                raise forms.ValidationError({'Remarks': ["Please enter remarks",]})
        return super(GeneralpvForm, self).clean(*args, **kwargs)

    class Meta():
        model= models.Pv
        fields =('Type_of_accounts','IA_code','Date_recieved','Pv_reference','Source_of_Funding','Cost_center','Type_of_pv','Payee','Description','Account_code','Gross_amount','Withholding_tax','Net_amount','Status','Acc_Impress','Date_returned','returned_to_chest','Remarks')

        widgets ={
                 'Date_recieved' : DateInput() ,
                 'Date_returned' : DateInput(),

        }
        labels  = {
        'returned_to_chest':'Return To Chest (0.00 if not applicable)',
        'Withholding_tax':' Tax (0.00 if not applicable)',
        'Type_of_pv':' Type of Pv (Please chose only General)',
        'Account_code':' Acc Code',
        }





class HonpvForm(forms.ModelForm):

    def clean(self,*args, **kwargs):
        today = date.today()
        pvtype = self.cleaned_data.get('Type_of_pv')
        tochest = self.cleaned_data.get('returned_to_chest')
        status = self.cleaned_data.get('Status')
        returndate = self.cleaned_data.get('Date_returned')
        Daterecieved = self.cleaned_data.get('Date_recieved')
        Datereturn = self.cleaned_data.get('Date_returned')
        remarks = self.cleaned_data.get('Remarks')
        net = self.cleaned_data.get('Net_amount')
        if pvtype:
            if pvtype != "Honorarium":
                raise forms.ValidationError({'Type_of_pv': ["Please Chose Honorarium in the Type of Pv",]})
            elif status == "Returned" and not returndate:
                raise forms.ValidationError({'Date_returned': ["Please Enter Date Retured To Accounts",]})
            elif net < 0 :
                raise forms.ValidationError({'Net_amount': ["Net Amount cannot be less than 0",]})
            elif status != "Returned" and returndate:
                raise forms.ValidationError({'Date_returned': ["Please remove date returned",]})
            elif tochest > 0.00 and not remarks:
                raise forms.ValidationError({'Remarks': ["Please enter remarks",]})
        return super(HonpvForm, self).clean(*args, **kwargs)

    class Meta():
        model= models.Pv
        fields =('Type_of_accounts','IA_code','Date_recieved','Pv_reference','Source_of_Funding','Cost_center','Type_of_pv','Description','Account_code','Gross_amount','Withholding_tax','Net_amount','Status','Acc_Impress','Date_returned','returned_to_chest','Remarks')
        widgets ={
                 'Date_recieved' : DateInput(),
                 'Date_returned' : DateInput(),

        }
        labels  = {
        'returned_to_chest':'Return To Chest (0.00 if not applicable)',
        'Withholding_tax':' Tax (0.00 if not applicable)',
        'Type_of_pv':' Type of Pv (Please chose only Honurarium)',
        'Account_code':' Acc Code',
        }







class BenefitForm(forms.ModelForm):

    def clean(self,*args, **kwargs):
        staffname = self.cleaned_data.get('name')
        refrence = self.cleaned_data.get('Pv_reference')
        if refrence and staffname :

            if Staff.objects.filter(Pv_reference=refrence, name=staffname).exists():
                raise forms.ValidationError({'name': ["This Staff Is Already A Beneficiary To This Pv",]})

        return super(BenefitForm, self).clean(*args, **kwargs)

    class Meta():
        model = Staff
        fields =("__all__")
        widgets ={
                 'Date_added' : DateInput() ,

        }



class UpdateBenefitForm(forms.ModelForm):

    class Meta():
        model = models.Staff
        fields =("__all__")

    def clean(self,*args, **kwargs):
        pvtype = self.cleaned_data.get('Type_of_pv')
        tochest = self.cleaned_data.get('returned_to_chest')
        status = self.cleaned_data.get('Status')
        returndate = self.cleaned_data.get('Date_returned')
        if pvtype:
            if pvtype != "Honorarium":
                raise forms.ValidationError('Please Chose Honorarium in the Type of Pv')
            elif status == "Returned" and not returndate:
                raise forms.ValidationError('Please Enter Date Retured To Accounts')

        return super(UpdateBenefitForm, self).clean(*args, **kwargs)


class UpdatepvForm(forms.ModelForm):

    def clean(self,*args, **kwargs):
        today = date.today()
        pvtype = self.cleaned_data.get('Type_of_pv')
        tochest = self.cleaned_data.get('returned_to_chest')
        status = self.cleaned_data.get('Status')
        returndate = self.cleaned_data.get('Date_returned')
        Daterecieved = self.cleaned_data.get('Date_recieved')
        Datereturn = self.cleaned_data.get('Date_returned')
        remarks = self.cleaned_data.get('Remarks')
        net = self.cleaned_data.get('Net_amount')
        if pvtype:
            if pvtype != "General":
                raise forms.ValidationError({'Type_of_pv': ["Please Chose General in the Type of Pv",]})
            elif status == "Returned" and not returndate:
                raise forms.ValidationError({'Date_returned': ["Please Enter Date Retured To Accounts",]})
            elif net < 0 :
                raise forms.ValidationError({'Net_amount': ["Net Amount cannot be less than 0",]})
            elif status != "Returned" and returndate:
                raise forms.ValidationError({'Date_returned': ["Please remove date returned",]})
            elif tochest > 0.00 and not remarks:
                raise forms.ValidationError({'Remarks': ["Please enter remarks",]})
        return super(UpdatepvForm, self).clean(*args, **kwargs)

    class Meta():
        model= models.Pv
        fields =('Type_of_accounts','IA_code','Date_recieved','Pv_reference','Source_of_Funding','Cost_center','Type_of_pv','Payee','Description','Account_code','Gross_amount','Withholding_tax','Net_amount','Status','Acc_Impress','Date_returned','returned_to_chest','Remarks')
        widgets ={
                     'Date_returned': DateInput(),
                     'Date_recieved': DateInput() ,
            }


class HunUpdatepvForm(forms.ModelForm):

    def clean(self,*args, **kwargs):
        today = date.today()
        pvtype = self.cleaned_data.get('Type_of_pv')
        tochest = self.cleaned_data.get('returned_to_chest')
        status = self.cleaned_data.get('Status')
        returndate = self.cleaned_data.get('Date_returned')
        Daterecieved = self.cleaned_data.get('Date_recieved')
        Datereturn = self.cleaned_data.get('Date_returned')
        remarks = self.cleaned_data.get('Remarks')
        net = self.cleaned_data.get('Net_amount')
        if pvtype:
            if pvtype != "Honorarium":
                raise forms.ValidationError({'Type_of_pv': ["Please Chose Honorarium in the Type of Pv",]})
            elif status == "Returned" and not returndate:
                raise forms.ValidationError({'Date_returned': ["Please Enter Date Retured To Accounts",]})
            elif net < 0 :
                raise forms.ValidationError({'Net_amount': ["Net Amount cannot be less than 0",]})
            elif status != "Returned" and returndate:
                raise forms.ValidationError({'Date_returned': ["Please remove date returned",]})
            elif tochest > 0.00 and not remarks:
                raise forms.ValidationError({'Remarks': ["Please enter remarks",]})
        return super(HunUpdatepvForm, self).clean(*args, **kwargs)


    class Meta():
        model= models.Pv
        fields =('Type_of_accounts','IA_code','Date_recieved','Pv_reference','Source_of_Funding','Cost_center','Type_of_pv','Description','Account_code','Gross_amount','Withholding_tax','Net_amount','Status','Acc_Impress','Date_returned','returned_to_chest','Remarks')
        widgets ={
                     'Date_returned': DateInput(),
                     'Date_recieved': DateInput() ,
            }


class standardUpdatepvForm(forms.ModelForm):

    def clean(self,*args, **kwargs):
        today = date.today()
        pvtype = self.cleaned_data.get('Type_of_pv')
        tochest = self.cleaned_data.get('returned_to_chest')
        status = self.cleaned_data.get('Status')
        returndate = self.cleaned_data.get('Date_returned')
        Daterecieved = self.cleaned_data.get('Date_recieved')
        Datereturn = self.cleaned_data.get('Date_returned')
        remarks = self.cleaned_data.get('Remarks')
        net = self.cleaned_data.get('Net_amount')
        if pvtype:
            if pvtype != "General":
                raise forms.ValidationError({'Type_of_pv': ["Please Chose General in the Type of Pv",]})
            elif status == "Returned" and not returndate:
                raise forms.ValidationError({'Date_returned': ["Please Enter Date Retured To Accounts",]})
            elif net < 0 :
                raise forms.ValidationError({'Net_amount': ["Net Amount cannot be less than 0",]})
            elif status != "Returned" and returndate:
                raise forms.ValidationError({'Date_returned': ["Please remove date returned",]})
            elif tochest > 0.00 and not remarks:
                raise forms.ValidationError({'Remarks': ["Please enter remarks",]})
        return super(standardUpdatepvForm, self).clean(*args, **kwargs)


    class Meta():
        model= models.Pv
        fields =('Type_of_accounts','IA_code','Date_recieved','Pv_reference','Source_of_Funding','Cost_center','Type_of_pv','Payee','Description','Account_code','Gross_amount','Withholding_tax','Net_amount','Status','Acc_Impress','Date_returned','returned_to_chest','Remarks')
        widgets ={
                     'Date_returned': DateInput(),
                     'Date_recieved': DateInput() ,
            }



class UserLoginForm(forms.Form):
    username =forms.CharField(label='Staff ID')
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self,*args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username or Password incorrect')
            if not user.check_password(password):
                raise forms.ValidationError('Username or Password incorrect')
            if not user.is_active:
                raise forms.ValidationError('Username or Password incorrect')
        return super(UserLoginForm, self).clean(*args, **kwargs)

    class Meta():
        model= models.User
        fields = ('username','password')

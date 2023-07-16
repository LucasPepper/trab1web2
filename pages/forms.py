from django import forms

from .models import Aluno, Turma

class AlunoForm(forms.ModelForm):
 
    class Meta:
        model = Aluno
        fields = ['name', 'hotel_Main_Img']

# class ProductForm(forms.ModelForm):
#     title = forms.CharField(label='', 
#                             widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
#     email = forms.EmailField()
#     description = forms.CharField(required=False, 
#                                 widget=forms.Textarea(attrs={
#                                     "placeholder": "Your Description",
#                                     "class": "new-class-name",
#                                     "id": "my-id-for-textarea",
#                                     "rows": 5,
#                                     "cols": 20
#                                 }))
#     price = forms.DecimalField(initial=1.99)

#     class Meta:
#         model = Product
#         fields = [
#             'title',
#             'description',
#             'price'
#         ]

#     def clean_title(self, *args, **kwargs):
#         title = self.cleaned_data.get('title')
#         if not "LPS" in title:
#             raise forms.ValidationError("This is not a valid title")
#         if not "LP" in title:
#             raise forms.ValidationError("This is not a valid title")
#         return title

#     def clean_email(self, *args, **kwargs):
#         email = self.cleaned_data.get('email')
#         if not "edu" in email:
#             raise forms.ValidationError("This is not a valid Email")
#         if not email.endswith("com"):
#             raise forms.ValidationError("This is not a valid Email")
#         return email
    
# class RawProductForm(forms.Form):
#     title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
#     description = forms.CharField(required=False, 
#                                   widget=forms.Textarea(attrs={
#                                       "placeholder": "Your Description",
#                                       "class": "new-class-name",
#                                       "id": "my-id-for-textarea",
#                                       "rows": 20,
#                                       "cols": 20
#                                   }))
#     price = forms.DecimalField(initial=1.99)


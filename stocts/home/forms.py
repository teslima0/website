from django import forms
from .models import Post, Category,Comment
from django import forms
from django.core import validators
from django.core.validators import RegexValidator
from django.forms.widgets import TextInput
#choices=[('Entertainment','Entertainment'),('Sport','Sport'),('Politics','Politics')]
choices=Category.objects.all().values_list('name','name')
choices_list=[]
for item in choices:
  choices_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','author','category','body','snippet','header_image')

        widgets={
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
          'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'tamar','type':'hidden'}),
          #'author': forms.Select(attrs={'class': 'form-control'}),
          'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
          'body': forms.Textarea(attrs={'class': 'form-control'}),
          'snippet': forms.Textarea(attrs={'class': 'form-control'}),



        }


class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body','snippet')

        widgets={
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
          #'author': forms.Select(attrs={'class': 'form-control'}),
          'body': forms.Textarea(attrs={'class': 'form-control'}),
          'snippet': forms.Textarea(attrs={'class': 'form-control'}),


        }


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')

        widgets={
          'name': forms.TextInput(attrs={'class': 'form-control'}),
         
          'body': forms.Textarea(attrs={'class': 'form-control'}),
          


        }
class CgpCal(forms.Form):
    nums1 = forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums2= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums3=forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums4= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums5= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums6=forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums7 = forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums8= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums9=forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums10= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums11= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums12 = forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums13= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums14=forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums15= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums16= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums17=forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums18 = forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums19= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums20=forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    
class AgeCal(forms.Form):
    birth_day = forms.CharField(max_length=2, widget=TextInput(attrs={'pattern':'[0-9]+'}))
    b_month= forms.CharField(max_length=2,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    b_yrs=forms.CharField(max_length=4,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    g_day = forms.CharField(max_length=2,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    g_month= forms.CharField(max_length=2,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    g_yrs=forms.CharField(max_length=4, widget=TextInput(attrs={'pattern':'[0-9]+'}))

class InputForm(forms.Form):
    pred=forms.CharField(label='Test Input', validators=[RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")]
    ,max_length=150, widget=forms.Textarea(attrs={'class':"form-control"}))

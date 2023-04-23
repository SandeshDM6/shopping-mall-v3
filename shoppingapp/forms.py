from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib import auth

from shoppingapp.models import *
from ckeditor.widgets import CKEditorWidget


    

class JobForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Store Title :"
        self.fields['location'].label = "Store Location :"
        self.fields['salary'].label = "Avg Spend :"
        self.fields['description'].label = "Job Description :"
        self.fields['tags'].label = "Tags :"
        self.fields['last_date'].label = "Submission Deadline :"
        #self.fields['company_name'].label = "Branch Name :"
        self.fields['url'].label = "Logo :"



        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Starbucks',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg : 1st Floor',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': '$5 - $150',
            }
        )
        self.fields['tags'].widget.attrs.update(
            {
                'placeholder': 'Use comma separated. eg: Coffee, Sandwhich ',
            }
        )                        
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',
                
            }
        )        
        # self.fields['company_name'].widget.attrs.update(
        #     {
        #         'placeholder': 'Starbucks',
        #     }
        # )           
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'Logo',
            }
        )   
         


    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "category",
            "salary",
             "description",
            "tags",
            "last_date",
            # "company_name",
            # "company_description",
            "url",
            "picture"
            ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Service is required")
        return job_type

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("category is required")
        return category


    def save(self, commit=True):
        job = super(JobForm, self).save(commit=False)
        if commit:
            
            job.save()
        return job








class JobEditForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Store Title :"
        self.fields['location'].label = "Store Location :"
        self.fields['salary'].label = "Avg Spend :"
        self.fields['description'].label = "Store Description :"
        # self.fields['tags'].label = "Tags :"
        self.fields['last_date'].label = "Dead Line :"
        #self.fields['company_name'].label = "Branch Name :"
        self.fields['url'].label = "Website :"


        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Starbucks',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg : 1st Floor',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': '$5 - $150',
            }
        )                 
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',
            }
        )        
        # self.fields['company_name'].widget.attrs.update(
        #     {
        #         'placeholder': 'Company Name',
        #     }
        # )           
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )    

    
        last_date = forms.CharField(widget=forms.TextInput(attrs={
                    'placeholder': 'Service Name',
                    'class' : 'datetimepicker1'
                }))

    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "category",
            "salary",
            "description",
            "last_date",
           # "company_name",
          #  "company_description",
            "url"
            ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Store Type is required")
        return job_type

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("Category is required")
        return category


    def save(self, commit=True):
        job = super(JobEditForm, self).save(commit=False)
      
        if commit:
            job.save()
        return job


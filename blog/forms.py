from django import forms 
from .models import Post

class Form_list(forms.ModelForm):
	class Meta:
		model=Post
		fields=(
		  'title',
		  'text',
		)

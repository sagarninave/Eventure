from django import forms
from .models import gallery

class dataform(forms.ModelForm):
	class Meta:
		model = gallery
		fields = [
			'title',
			'description',
			'file'
		]

class imagedataform(forms.Form):
	title = forms.CharField(
							label='Post Title',
							widget=forms.TextInput(
										attrs={
												'placeholder':'Title',
											}
										)
							)
	description = forms.CharField(
									required=False,
									widget=forms.Textarea(
										attrs={
												'class':'textarea_class',
												'id':'textarea_id',
												'rows':5,
												'cols':50,
												}
											)
										)
	file = forms.FileField()
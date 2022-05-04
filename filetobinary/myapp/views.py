from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse 

# Create your views here.

def model_form_upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			file = open('media/documents/supriya.txt', 'r')
			newfile= open('newfile','w')
			file = (str(file))
			bin_result = ''.join(format(ord(x), '08b') for x in file)   
			print("The string that we obtain binary conversion is ",bin_result) 


			newfile.write(bin_result)

			 

			# file.close()
			newfile.close()
			# form.save()
			return HttpResponse('file created')
	else:
		form = DocumentForm()
	return render(request, 'model_form_upload.html', {
		'form': form
	})

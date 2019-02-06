from django.http import HttpResponse
from .models import events, students
from django.template import loader

def index(request):
	records = events.objects.all()
	students_records = students.objects.all()
	template = loader.get_template('events/index.html')
	context = {'records' : records, 'students_records' : students_records}
	return HttpResponse(template.render(context, request))

#def details(request, record_id):
#	return HttpResponse("hello")
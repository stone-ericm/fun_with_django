from django.shortcuts import render
from django.views.generic import View
from .forms import CreatePost
from django.http import HttpResponse
# Create your views here.
class Index(View):
	template = 'hacker/index.html'

	def get(self, request):
		return render(request, self.template, {})

class Create(View):
	template = 'hacker/index.html'
	def get(self, request):
		context = {
			'forms': CreatePost()
		}
		return HttpResponse(CreatePost())
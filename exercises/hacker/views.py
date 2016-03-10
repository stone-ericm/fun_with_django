from django.shortcuts import render
from django.views.generic import View
from .forms import CreatePost
from django.http import HttpResponse, JsonResponse
from hacker.models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class Index(View):
	template = 'hacker/index.html'

	def get(self, request):
		posts = Post.objects.all().order_by('-updated_at')
		context = {'posts': posts,}
		# user = authenticate(username = 'stonehengee', password='admin')
		# login(request, user)
		if request.user.is_authenticated():
			user = request.user
			# user = User.objects.get(username=username)
			# user_posts = Post.objects.filter(user=user.id)
			context['user'] = user
		return render(request, self.template, context)

class Create(View):
	template = 'hacker/index.html'
	def get(self, request):
		return HttpResponse(CreatePost().as_p())
	def post(self, request):
		print("CAN ANYONE SEE ME?")
		form = CreatePost(request.POST)
		post = form.save(commit=False)
		# post.user=request.user
		post.save()
		return JsonResponse(post.to_json())
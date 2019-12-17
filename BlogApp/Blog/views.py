from django.shortcuts import render
from django.http import HttpResponse

posts=[
	{
		'author': 'User1',
		'title': 'Blog post 1',
		'content': 'User1 content',
		'date_post': '17  December,2019',
	},
	{
		'author': 'User2',
		'title': 'Blog post 2',
		'content': 'User2 content',
		'date_post': '17  December,2019',
	}
]
def home(request):
	context = {
		'posts':posts
	}
	return render(request, 'Blog/homepage.html', context)

def about(request):
	return render(request, 'Blog/aboutpage.html',{'title': 'About'})

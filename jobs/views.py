from django.shortcuts import render

from .models import Category

# Create your views here.
def home(request):
	categories = Category.objects.all()
	template = "home.html"
	context = {
		"categories":categories,
	}
	return render(request, template, context)
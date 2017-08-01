from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Category, Job
from .forms import JobForm


# Create your views here.
def home(request):
    categories = Category.objects.all()
    template = "home.html"
    context = {
        "categories": categories,
    }
    return render(request, template, context)


@login_required
def post_job(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        job = form.save(commit=False)
        job.poster = request.user
        job.save()
        return redirect('home')

    template = "post_job.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def browse_jobs(request):
    jobs = Job.objects.all()
    template = "browse_jobs.html"
    context = {
        "jobs": jobs,
    }
    return render(request, template, context)

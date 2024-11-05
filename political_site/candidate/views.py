from django.shortcuts import render, get_object_or_404, redirect
from .models import Candidate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
# Home Page View


@login_required
def home(request):
    candidates = Candidate.objects.all()
    return render(request, 'home.html', {'candidates': candidates})

# Candidate Details Page View


@login_required
def candidate_detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    return render(request, 'candidate_detail.html', {'candidate': candidate})

# Vote View (Restrict to logged-in users)


@login_required
def vote(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    candidate.vote_count += 1
    candidate.save()
    return redirect('results')

# Results Page View


def results(request):
    candidates = Candidate.objects.all()
    return render(request, 'results.html', {'candidates': candidates})


# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

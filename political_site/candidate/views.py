from django.shortcuts import render, get_object_or_404, redirect
from .models import Candidate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Home Page View
@login_required
def home(request):
    """
    Render the home page with a list of all candidates.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered home page with candidates.
    """
    candidates = Candidate.objects.all()
    return render(request, 'home.html', {'candidates': candidates})

# Candidate Details Page View
@login_required
def candidate_detail(request, candidate_id):
    """
    Render the candidate detail page for a specific candidate.
    
    Args:
        request: The HTTP request object.
        candidate_id (int): The ID of the candidate to be displayed.
    
    Returns:
        HttpResponse: The rendered candidate detail page.
    """
    candidate = get_object_or_404(Candidate, id=candidate_id)
    return render(request, 'candidate_detail.html', {'candidate': candidate})

# Vote View (Restrict to logged-in users)

@login_required
def vote(request, candidate_id):
    """
    Increment the vote count for a specific candidate.
    
    Args:
        request: The HTTP request object.
        candidate_id (int): The ID of the candidate to vote for.
    
    Returns:
        HttpResponseRedirect: Redirects to the results page after voting.
    """
    candidate = get_object_or_404(Candidate, id=candidate_id)
    candidate.vote_count += 1
    candidate.save()
    return redirect('results')


# Results Page View
def results(request):
    """
    Render the results page with the vote counts for all candidates.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered results page with candidates' vote counts.
    """
    candidates = Candidate.objects.all()
    return render(request, 'results.html', {'candidates': candidates})


# Signup View
def signup(request):
    """
    Render the signup page and handle user registration.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered signup page or a redirect to the home page after successful registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

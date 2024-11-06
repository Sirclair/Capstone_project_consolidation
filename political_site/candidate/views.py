from django.shortcuts import render, get_object_or_404, redirect
from .models import Candidate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    """
    View function for the home page.
    
    Retrieves and displays a list of all candidates.
    
    Args:
        request (HttpRequest): The request object.
        
    Returns:
        HttpResponse: The rendered home page with a list of candidates.
    """
    candidates = Candidate.objects.all()
    return render(request, 'home.html', {'candidates': candidates})


@login_required
def candidate_detail(request, candidate_id):
    """
    View function for displaying candidate details.
    
    Retrieves and displays details of a specific candidate based on the candidate ID.
    
    Args:
        request (HttpRequest): The request object.
        candidate_id (int): The ID of the candidate to be displayed.
        
    Returns:
        HttpResponse: The rendered candidate details page.
    """
    candidate = get_object_or_404(Candidate, id=candidate_id)
    return render(request, 'candidate_detail.html', {'candidate': candidate})


@login_required
def vote(request, candidate_id):
    """
    View function for casting a vote for a candidate.
    
    Increments the vote count for a specific candidate based on the candidate ID.
    Redirects to the results page after voting.
    
    Args:
        request (HttpRequest): The request object.
        candidate_id (int): The ID of the candidate to be voted for.
        
    Returns:
        HttpResponseRedirect: Redirects to the results page.
    """
    candidate = get_object_or_404(Candidate, id=candidate_id)
    candidate.vote_count += 1
    candidate.save()
    return redirect('results')


def results(request):
    """
    View function for displaying voting results.
    
    Retrieves and displays a list of all candidates and their vote counts.
    
    Args:
        request (HttpRequest): The request object.
        
    Returns:
        HttpResponse: The rendered results page with a list of candidates and their vote counts.
    """
    candidates = Candidate.objects.all()
    return render(request, 'results.html', {'candidates': candidates})


def signup(request):
    """
    View function for user signup.
    
    Handles user registration using the UserCreationForm. If the form is valid, 
    the user is created and logged in. Otherwise, the signup form is displayed.
    
    Args:
        request (HttpRequest): The request object.
        
    Returns:
        HttpResponse: The rendered signup page with the signup form.
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

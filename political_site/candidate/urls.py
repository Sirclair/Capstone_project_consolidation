
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('candidate/<int:candidate_id>/', views.candidate_detail, name='candidate_detail'),  # Candidate details page
    path('results/', views.results, name='results'),  # Results page
    path('vote/<int:candidate_id>/', views.vote, name='vote'),  # Voting functionality
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]

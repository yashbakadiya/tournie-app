from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile, Organize, Participating


# def home(request):
#     context = {
#         'organize': Organize.objects.all(),
#         'title': 'Home'
#     }
#     return render(request, 'part/home.html',context)

class CreatedListView(ListView):
    model = Organize
    context_object_name = 'organizes'
    template_name = 'part/home.html'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

class CreatedListViewMore(ListView):
    model = Organize
    context_object_name = 'organizes'
    template_name = 'part/create.html'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Participate'
        return context

  

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} account is created!')
            # user = authenticate(username=username,password=request.POST['password1'])
            user = User.objects.get(username=username)
            login(request,user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return   render(request,'part/register.html',{'form': form, 'title':'Join Now'})

@login_required
def accounts(request):
    return render(request, 'part/accounts.html', {'title':'Account'})

@login_required
def organizer(request):
    return render(request, 'part/organizer.html', {'title':'Organizer'})

@login_required
def participate(request):
    return render(request, 'part/participate.html', {'title':'Participate'})

class organize(LoginRequiredMixin, CreateView):
    model = Organize
    fields = ['tournament_name', 'organizer_name','discipline', 'size', 'participants', 'prize_pool', 'banner', 'description', 'youtube_account', 'instagram_account', 'discord_account', 'twitter_account', 'country']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Tournament'
        return context

    def form_valid(self, forme):
        forme.instance.author = self.request.user
        return super().form_valid(forme)

class OrganizeDetailView(DetailView):
    model = Organize

class EditOrganize(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Organize
    fields = ['tournament_name', 'organizer_name','discipline', 'size', 'participants', 'prize_pool', 'banner', 'description', 'youtube_account', 'instagram_account', 'discord_account', 'twitter_account', 'country']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)        

    def test_func(self):
        organize = self.get_object()
        if self.request.user == organize.author:
            return True
        return False

class DeleteOrganize(LoginRequiredMixin, DeleteView):
    model = Organize
    success_url = '/'

    def test_func(self):
        organize = self.get_object()
        if self.request.user == organize.author:
            return True
        return False

class participatingTeam(LoginRequiredMixin, CreateView, ListView):
    model = Participating
    fields = ['email', 'team_Name', 'contact_No', 'tournament_Name', 'player_1_IGN', 'player_2_IGN', 'player_3_IGN', 'player_4_IGN', 'player_5_IGN', 'player_6_IGN', 'player_7_IGN', 'team_LOGO']

    def get_context_data(self, **kwargs):
        context = super(participatingTeam, self).get_context_data(**kwargs)
        context['orgs'] = Organize.objects.filter(id=self.kwargs['pk'])
        context['title'] = 'Participate'
        return context

    def form_valid(self, forme):
        forme.instance.author = self.request.user
        return super().form_valid(forme)
        
    def test_func(self):
        participating = self.get_object()
        if self.request.user == participating.author:
            return True
        return False

class participatingPlayer(LoginRequiredMixin, CreateView, ListView):
    model = Participating
    fields = ['email', 'player_Name', 'contact_No', 'team_LOGO', 'tournament_Name']

    def get_context_data(self, **kwargs):
        context = super(participatingPlayer, self).get_context_data(**kwargs)
        context['orgs'] = Organize.objects.filter(id=self.kwargs['pk'])
        context['title'] = 'Participate'
        return context

    def form_valid(self, forme):
        forme.instance.author = self.request.user
        return super().form_valid(forme)

    def test_func(self):
        participating = self.get_object()
        if self.request.user == participating.author:
            return True
        return False        

class ParticipantListView(ListView):
    model = Participating
    context_object_name = 'participant'
    template_name = 'part/views.html'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orgs'] = Organize.objects.all()
        context['title'] = 'Participants'
        return context

class CreatedListViewMoreMore(ListView):
    model = Participating
    context_object_name = 'participant'
    template_name = 'part/viewmore.html'  
    
    def get_context_data(self, **kwargs):
        context = super(CreatedListViewMoreMore, self).get_context_data(**kwargs)
        context['orgs'] = Organize.objects.all()
        context['title'] = 'Participated'
        return context              

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('accounts') 

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title':'Profile'
    }
    return render(request, 'part/profile.html', context)

def ContactUs(request):
    return render(request, 'part/contact_us.html', {'title':'Contact Us'})    

def Post(request):
    return render(request, 'part/post.html', {'title':'Post'})    

def FaqAndGuide(request):
    return render(request, 'part/faq.html', {'title':'FAQ And Guide'})  
    
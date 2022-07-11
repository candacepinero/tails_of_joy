from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pet

# Home view
def home(request):
    return render(request, 'home.html')

# index view
@login_required
def pets_index(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'pets/index.html', {'pets': pets})

# detail view
@login_required
def pets_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'pets/detail.html', {'pet': pet})

# sign up view
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        error_message = 'Invalid sign up - try again'
        form = UserCreationForm()
        context = {'form': form, 'error_message': error_message}
        return render(request, 'registration/signup.html', context)

# create view
class PetCreate(LoginRequiredMixin,  CreateView):
    model = Pet
    fields = ['name', 'age', 'gender', 'lives_in', 'personality']
    success_url = '/pets/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# update view
class PetUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    fields = ['age', 'lives_in',  'personality']

class PetDelete(LoginRequiredMixin, DeleteView):
    model = Pet
    success_url = '/pets/'
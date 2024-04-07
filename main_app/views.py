from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Rarity
from .forms import FeedingForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
  print(finch_id)
  finch = Finch.objects.get(id=finch_id)
  id_list = finch.rarities.all().values_list('id')
  rarities_finch_doesnt_have = Rarity.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', {'finch': finch, 'feeding_form': feeding_form, 'rarities': rarities_finch_doesnt_have})

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)


def assoc_rarity(request, finch_id, rarity_id):
  Finch.objects.get(id=finch_id).rarities.add(rarity_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_rarity(request, finch_id, rarity_id):
  Finch.objects.get(id=finch_id).rarities.remove(rarity_id)
  return redirect('detail', finch_id=finch_id)





class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches'



class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'

class RarityList(ListView):
  model = Rarity

class RarityDetail(DetailView):
  model = Rarity

class RarityCreate(CreateView):
  model = Rarity
  fields = '__all__'

class RarityUpdate(UpdateView):
  model = Rarity
  fields = ['name', 'color']

class RarityDelete(DeleteView):
  model = Rarity
  success_url = '/rarities/'



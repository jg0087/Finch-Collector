from django.shortcuts import render

finches = [
  {'name': 'Doky', 'breed': 'Pine', 'description': 'pink and blue', 'age': 5},
  {'name': 'Nala', 'breed': 'Evening', 'description': 'red and white', 'age': 2},
]


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})
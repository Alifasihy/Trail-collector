from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Trail
from .forms import MaintainingForm

class TrailCreate(CreateView) :
    model = Trail
    fields = '__all__'

class TrailUpdate(UpdateView) :
    model= Trail
    fields =['terrian', 'description','length'] 
    context_object_name = 'trail'

class TrailDelete(DeleteView) :
    model= Trail
    success_url ='/trails/' 
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trails_index(request):
    trails = Trail.objects.all()
    return render(request,'trails/index.html', {'trails': trails})
def trails_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    maintaining_form = MaintainingForm()
    return render(request, 'trails/detail.html', {
        'trail': trail, 'maintaining_form': maintaining_form})

def add_maintaining(request, trail_id):
  form = MaintainingForm(request.POST)

  if form.is_valid():
    maintaining = form.save(commit=False)
    maintaining.trail_id = trail_id
    maintaining.save()

  return redirect('detail', trail_id=trail_id)
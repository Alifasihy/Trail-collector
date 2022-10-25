from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Trail


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trails_index(request):
    trails = Trail.objects.all()
    return render(request,'trails/index.html', {'trails': trails})
def trails_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    return render(request, 'trails/detail.html', {'trail': trail})
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
from django.shortcuts import render


class Trail: 
 def __init__(self, name, terrian, description, lenght):
    self.name = name
    self.terrian = terrian
    self.description = description
    self.lenght =lenght
trails =[
Trail('Bruce', 'rocky', 'long long long', 500),
Trail('Ganaraska', 'foresty', 'asdfasdfasdf asdf',12)
    ]
    


def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trails_index(request):
    return render(request,'trails/index.html',{'trails': trails})
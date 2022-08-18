from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .models import todo
from.forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
class listview(ListView):
    model=todo
    template_name = 'index.html'
    context_object_name ='set1'

class detailviews(DetailView):
    model=todo
    template_name='details.html'
    context_object_name='task'

class updateview(UpdateView):
    model=todo
    template_name='update.html'
    context_object_name='task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoapp:detailview',kwargs={'pk': self.object.id})
class deleteview(DeleteView):
    model=todo
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:listview')


def Home(request):
    set1=todo.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        Set= todo(name=name,priority=priority,date=date)
        Set.save()

    return render(request,'index.html',{'set1':set1})

def delete(request,taskid):
    set2=todo.objects.get(id=taskid)
    if request.method =="POST":
        set2.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,fieldid):
     todo1=todo.objects.get(id=fieldid)
     form=todoform(request.POST or None,instance=todo1)
     if form.is_valid():
         form.save()
         return redirect('/')
     return render(request,'update.html',{'todo':todo1,'form':form})







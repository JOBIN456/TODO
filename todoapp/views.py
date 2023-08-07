from django.shortcuts import render
from .models import duty
from django.shortcuts import redirect
from .forms import Todo
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.views.generic import DeleteView
class Tasklistview(ListView):
    model=duty
    template_name='index.html'
    context_object_name='task'

class Taskdetailview(DetailView):
    model=duty
    template_name="detail.html"
    context_object_name="tw"
class Taskupdate(UpdateView):
    model=duty
    template_name="update.html"
    context_object_name="tw"
    fields=('name','priorty','date')
    def get_success_url(self):
        return reverse_lazy('cbd',kwargs={'pk':self.object.id})
class Taskdelete(DeleteView):
    model=duty
    template_name="delete.html"
    success_url= reverse_lazy('cbv')
    





# Create your views here.
def ABC(request):
    task=duty.objects.all()
    if request.method =='POST':
        name=request.POST.get('name','')
        priorty=request.POST.get("priorty",'')
        date=request.POST.get("date",'')
        g1=duty(name=name,priorty=priorty,date=date)
        g1.save()
    return render(request,"index.html",{"task":task})
def delete(request,id):
    if request.method=='POST':
        dn=duty.objects.get(id=id)
        dn.delete()
        return redirect("/")
    return render( request, "delete.html")
def update(request,id):
    f=duty.objects.get(id=id)
    f1=Todo(request.POST or None, instance=f)
    if f1.is_valid():
        f1.save()
        return redirect("/")
    return render(request,'edit.html',{'f':f,"f1":f1})    


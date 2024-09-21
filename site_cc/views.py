from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Clube, Categoria
from .forms import ClubeForm, ClubeEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def pagina_principal(request):
    return render(request,'pagina_principal.html',{})

def about(request):
    return render(request, 'about.html')

class clubesView(LoginRequiredMixin, ListView):
    model = Clube
    template_name = 'clubs.html'
    ordering = ['-dataDeCriacao']

    def get_context_data(self, *args, **kwargs):
        context = super(clubesView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = Categoria.objects.all()
        return context
    
def login_user(request):
    if request.method =="POST":
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are logged in."))
            return redirect('pagina_principal')


        else:   
            messages.success(request, ("An error occured. Try again"))
            return redirect('login') 
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You logged out"))
    return redirect('pagina_principal')

def CategoriaView(request, cats):
    categoria_clube = Clube.objects.filter(categoria__nome=cats.replace('-', ' '))
    return render(request, 'categorias.html', {'cats': cats.replace('-', ' '), 'categoria_clube': categoria_clube})


class HomePageView(ListView):
    model = Clube
    template_name = 'pagina_principal.html'
    ordering = ['-dataDeCriacao']

class ClubDetailView(DetailView):
    model = Clube
    template_name = 'clubDetail.html'

class AddCategoriaView(CreateView):
    model = Categoria
    template_name = 'addCategoria.html'
    fields = '__all__'
    success_url = reverse_lazy('addClube')

class AddClubView(CreateView):
    model = Clube
    form_class = ClubeForm
    template_name = 'addClube.html'

class UpdateClubView(UpdateView):
    model = Clube
    template_name = 'updateClube.html'
    form_class = ClubeEditForm

class DeleteClubView(DeleteView):
    model = Clube
    template_name = 'deleteClube.html'
    success_url = reverse_lazy('pagina_principal')



class meusclubesDetailView(ListView):
    model = Clube
    template_name = 'myclubes.html'
    ordering = ['-dataDeCriacao'] 

    def get_queryset(self):
        queryset = Clube.objects.filter(moderador=self.request.user).order_by('-dataDeCriacao')
        print(queryset)  # Para depuração
        return queryset

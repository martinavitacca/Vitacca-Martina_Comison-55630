from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html") 

def about(request):
    return render(request, "aplicacion/about.html") 
    
@login_required
def seinen(request):
    contexto = {'mangas': Seinen.objects.all()}
    return render(request, "aplicacion/seinen.html", contexto)

@login_required
def shounen(request):
    contexto = {'mangas': Shounen.objects.all()}
    return render(request, "aplicacion/shounen.html", contexto)

@login_required
def manhwa(request):
    contexto = {'manhwas': Manhwa.objects.all()}
    return render(request, "aplicacion/manhwa.html", contexto)

@login_required
def shoujo(request):
    contexto = {'mangas': Shoujo.objects.all()}
    return render(request, "aplicacion/shoujo.html", contexto) 

@login_required
def manga(request):
    contexto = {'mangas': Manga.objects.all()}
    return render(request, "aplicacion/manga.html", contexto) 


# View/Create/Update/Delete Review
class ReviewList(LoginRequiredMixin, ListView):
    model = Review

class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'username', 'comment', 'rating']
    success_url = reverse_lazy('review')

class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['comment', 'rating']
    success_url = reverse_lazy('review')

class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('review')


# Update/Delete Seinen Categorie
@login_required
def updateSeinen(request, seinen_id):
    seinen = Seinen.objects.get(id=seinen_id)
    if request.method == "POST":
        miForm = SeinenForm(request.POST)
        if miForm.is_valid():
            seinen.chapter = miForm.cleaned_data.get('chapter')
            seinen.volume = miForm.cleaned_data.get('volume')
            seinen.current_estado = miForm.cleaned_data.get('current_estado')
            seinen.save()
            return redirect(reverse_lazy('seinen'))
    else:
        miForm = SeinenForm(initial={
            'title': seinen.title,
            'chapter': seinen.chapter,
            'volume': seinen.volume,
            'estado': seinen.current_estado,   
        })  
    
    return render(request, "aplicacion/seinen_form.html", {'form': miForm})

class SeinenDelete(LoginRequiredMixin, DeleteView):
    model = Seinen
    success_url = reverse_lazy('seinen')


# Update/Delete Shounen Categorie
@login_required
def updateShounen(request, shounen_id):
    shounen = Shounen.objects.get(id=shounen_id)
    if request.method == "POST":
        miForm = ShounenForm(request.POST)
        if miForm.is_valid():
            shounen.chapter = miForm.cleaned_data.get('chapter')
            shounen.volume = miForm.cleaned_data.get('volume')
            shounen.current_estado = miForm.cleaned_data.get('current_estado')
            shounen.save()
            return redirect(reverse_lazy('shounen'))
    else:
        miForm = ShounenForm(initial={
            'title': shounen.title,
            'chapter': shounen.chapter,
            'volume': shounen.volume,
            'estado': shounen.current_estado,   
        })  
    
    return render(request, "aplicacion/shounen_form.html", {'form': miForm})

class ShounenDelete(LoginRequiredMixin, DeleteView):
    model = Shounen
    success_url = reverse_lazy('shounen')


# Update/Delete Manhwa Categorie
@login_required
def updateManhwa(request, manhwa_id):
    manhwa = Manhwa.objects.get(id=manhwa_id)
    if request.method == "POST":
        miForm = ManhwaForm(request.POST)
        if miForm.is_valid():
            manhwa.chapter = miForm.cleaned_data.get('chapter')
            manhwa.volume = miForm.cleaned_data.get('volume')
            manhwa.current_estado = miForm.cleaned_data.get('current_estado')
            manhwa.save()
            return redirect(reverse_lazy('manhwa'))
    else:
        miForm = ManhwaForm(initial={
            'title': manhwa.title,
            'chapter': manhwa.chapter,
            'volume': manhwa.volume,
            'estado': manhwa.current_estado,   
        })  
    
    return render(request, "aplicacion/manhwa_form.html", {'form': miForm})

class ManhwaDelete(LoginRequiredMixin, DeleteView):
    model = Manhwa
    success_url = reverse_lazy('manhwa')


# Update/Delete Shoujo Categorie
@login_required
def updateShoujo(request, shoujo_id):
    shoujo = Shoujo.objects.get(id=shoujo_id)
    if request.method == "POST":
        miForm = ShoujoForm(request.POST)
        if miForm.is_valid():
            shoujo.chapter = miForm.cleaned_data.get('chapter')
            shoujo.volume = miForm.cleaned_data.get('volume')
            shoujo.current_estado = miForm.cleaned_data.get('current_estado')
            shoujo.save()
            return redirect(reverse_lazy('shoujo'))
    else:
        miForm = ShoujoForm(initial={
            'title': shoujo.title,
            'chapter': shoujo.chapter,
            'volume': shoujo.volume,
            'estado': shoujo.current_estado,   
        })  
    
    return render(request, "aplicacion/shoujo_form.html", {'form': miForm})

class ShoujoDelete(LoginRequiredMixin, DeleteView):
    model = Shoujo
    success_url = reverse_lazy('shoujo')


# Create/Update/Delete Custom Manga Entry
@login_required
def createManga(request):    
    if request.method == "POST":
        miForm = MangaForm(request.POST)
        if miForm.is_valid():
            manga_title = miForm.cleaned_data.get('title')
            manga_chapter = miForm.cleaned_data.get('chapter')
            manga_volume = miForm.cleaned_data.get('volume')
            manga_currten_estado = miForm.cleaned_data.get('current_estado')
            manga = Manga(title=manga_title, 
                          chapter=manga_chapter,
                          volume=manga_volume,
                          current_estado=manga_currten_estado
                          )
            manga.save()
            return redirect(reverse_lazy('manga'))
    else:
        miForm = MangaForm()

    return render(request, "aplicacion/manga_form.html", {"form":miForm})

class MangaUpdate(LoginRequiredMixin, UpdateView):
    model = Manga
    fields = ['title', 'chapter', 'volume', 'current_estado']
    success_url = reverse_lazy('manga')
    
class MangaDelete(LoginRequiredMixin, DeleteView):
    model = Manga
    success_url = reverse_lazy('manga')


# Login / Register
def user_login(request):
    if request.method == "POST":
        loginForm = AuthenticationForm(request, data=request.POST)
        if loginForm.is_valid():
            usuario = loginForm.cleaned_data.get('username')
            password = loginForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatars/default.jpg"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/home.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': loginForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': loginForm, 'mensaje': f'Los datos son inválidos'})

    loginForm = AuthenticationForm()      

    return render(request, "aplicacion/login.html", {'form':loginForm})   


def register(request):
    if request.method == "POST":
        miForm = UserRegisterForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/home.html")
    else:
        miForm = UserRegisterForm()      
    return render(request, "aplicacion/register.html", {"form":miForm})  


# Edit Profile
@login_required
def editUserProfile(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/home.html")
        else:
            return render(request,"aplicacion/edit_profile.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/edit_profile.html", {'form': form, 'usuario': usuario.username})


# Avatar 
@login_required
def addAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            former_avatar = Avatar.objects.filter(user=u)
            if len(former_avatar) > 0:
                for i in range(len(former_avatar)):
                    former_avatar[i].delete()
                    
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/home.html")
    else:
        form = AvatarForm()
    return render(request, "aplicacion/add_avatar.html", {'form': form })


# Searcher
def searchSeinen(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        mangas = Seinen.objects.filter(title__icontains=patron)
        contexto = {'mangas': mangas}
        return render(request, 'aplicacion/seinen.html', contexto)
    return HttpResponse("No se ingreso ningun dato")

def searchShounen(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        mangas = Shounen.objects.filter(title__icontains=patron)
        contexto = {'mangas': mangas}
        return render(request, 'aplicacion/shounen.html', contexto)
    return HttpResponse("No se ingreso ningun dato")

def searchManhwa(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        manhwas = Manhwa.objects.filter(title__icontains=patron)
        contexto = {'manhwas': manhwas}
        return render(request, 'aplicacion/manhwa.html', contexto)
    return HttpResponse("No se ingreso ningun dato")

def searchShoujo(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        mangas = Shoujo.objects.filter(title__icontains=patron)
        contexto = {'mangas': mangas}
        return render(request, 'aplicacion/shoujo.html', contexto)
    return HttpResponse("No se ingreso ningun dato")
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# el signo . indica el directorio actual o la aplicación actual
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {"form": form})


def post_edit(request, pk):
    # Obtenermos el modelo (base de datos) el registro mediante clave
    post = get_object_or_404(Post, pk=pk)
    # Si la petición es por post (envío de datos por formulario)
    if request.method == 'POST':
        # Reemplaza los valores del formuario por la instancia consultada (registros de la base)
        form = PostForm(request.POST, instance=post)
        # Verifica si los datos son correctos y completos
        if form.is_valid():
            # Prepara los datos para guardar, pero no los guarda (en espera)
            post = form.save(commit=False)
            # Toma por defecto usuario: modifica registro
            post.author = request.user
            # Asignna fecha actual de publicación
            post.published_date = timezone.now()
            # Confirma los registros y guarga
            post.save()
            # redirecciona a la página principal de artiuclos
            return redirect('post_detail', pk=post.pk)
    else:
        # asigna a una variable objeto el QuerySet
        form = PostForm(instance=post)
        # Pasa el RecordSet a la plantilla, con los datos cargados
    return render(request, 'blog/post_edit.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from .models import Post, Categoria, Autor

# Vista principal del blog
def index(request):
    # Obtener los últimos 3 posts publicados
    ultimos_posts = Post.objects.filter(
        fecha_publicacion__isnull=False
    ).order_by('-fecha_publicacion')[:3]

    # Obtener categorías para el sidebar
    categorias = Categoria.objects.all()

    context = {
        'ultimos_posts': ultimos_posts,
        'categorias': categorias,
    }
    return render(request, 'index.html', context)

# Vista para listar todos los posts
def posts_list(request):
    # Obtener todos los posts publicados
    posts = Post.objects.filter(
        fecha_publicacion__isnull=False
    ).order_by('-fecha_publicacion')

    # Paginación: 6 posts por página
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()

    context = {
        'page_obj': page_obj,
        'categorias': categorias,
    }
    return render(request, 'posts.html', context)

# Vista para detalle de un post
class PostDetalleView(DetailView):
    model = Post
    template_name = 'blog/postdetalle.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        # Artículos relacionados por categorías
        categorias_post = post.categorias.all()
        context['relacionados'] = Post.objects.filter(
            categorias__in=categorias_post,
            fecha_publicacion__isnull=False
        ).exclude(id=post.id).distinct()[:3]

        # Categorías para el sidebar
        context['categorias'] = Categoria.objects.all()

        # Comentarios del post
        context['comentarios'] = post.comentarios.filter(
            comentario_padre__isnull=True
        ).order_by('-fecha_comentario')

        return context

# Vista para posts por categoría
def posts_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    posts = Post.objects.filter(
        categorias=categoria,
        fecha_publicacion__isnull=False
    ).order_by('-fecha_publicacion')

    # Paginación
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()

    context = {
        'page_obj': page_obj,
        'categoria_actual': categoria,
        'categorias': categorias,
    }
    return render(request, 'blog/posts_categoria.html', context)

# Vista para posts por autor
def posts_por_autor(request, autor_id):
    autor = get_object_or_404(Autor, id_autor=autor_id)

    posts = Post.objects.filter(
        autor_post=autor,
        fecha_publicacion__isnull=False
    ).order_by('-fecha_publicacion')

    # Paginación
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()

    context = {
        'page_obj': page_obj,
        'autor': autor,
        'categorias': categorias,
    }
    return render(request, 'blog/posts_autor.html', context)

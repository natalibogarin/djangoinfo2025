"""
URL configuration for proyectoInfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.blogInfo import views
from apps.blogInfo.views import PostDetalleView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('blog_auth.urls')),

    # Página principal
    path('', views.index, name='index'),

    # Lista de posts
    path('posts/', views.posts_list, name='posts'),

    # Detalle de un post
    path('post/<int:id>/', PostDetalleView.as_view(), name='post-detalle'),

    # Posts por categoría
    path('categoria/<int:categoria_id>/', views.posts_por_categoria, name='posts-categoria'),

    # Posts por autor
    path('autor/<int:autor_id>/', views.posts_por_autor, name='posts-autor'),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

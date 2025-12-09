from django.contrib import admin
from .models import Post, Categoria, Comentario, Autor

# Register your models here.
class AutorAdmin(admin.ModelAdmin):
  fields=('user', 'nombre', 'email', 'biografia')
  list_display = ("nombre", "email")
  search_fields = ("email",)
  list_filter = ("nombre",)

class PostAdmin(admin.ModelAdmin):
  list_display = ("titulo", "autor_post", "fecha_publicacion", "fecha_creacion")
  list_filter = ("fecha_publicacion", "categorias", "autor_post")
  search_fields = ("titulo", "contenido")
  filter_horizontal = ("categorias",)
  date_hierarchy = "fecha_publicacion"
  ordering = ("-fecha_publicacion",)

  fieldsets = (
      ('Información del Post', {
          'fields': ('titulo', 'autor_post', 'contenido')
      }),
      ('Categorías', {
          'fields': ('categorias',)
      }),
      ('Fechas', {
          'fields': ('fecha_publicacion', 'fecha_actualizacion'),
          'classes': ('collapse',)
      }),
  )

class CategoriaAdmin(admin.ModelAdmin):
  list_display = ("nombre",)
  search_fields = ("nombre",)

class ComentarioAdmin(admin.ModelAdmin):
  list_display = ("autor_comentario", "post", "fecha_comentario")
  list_filter = ("fecha_comentario", "post")
  search_fields = ("contenido_comentario", "autor_comentario__username")
  date_hierarchy = "fecha_comentario"

admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Comentario, ComentarioAdmin)
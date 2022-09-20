from django.contrib import admin

from .models import Categoria, Tatoo


class CategoriaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Categoria, CategoriaAdmin)


@admin.register(Tatoo)
class TatooAdmin(admin.ModelAdmin):
    ...

# Register your models here.

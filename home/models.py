from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=165)
    preco = models.CharField(max_length=16)
    descricao = models.TextField(max_length=2000)

    def __str__(self) -> str:
        return self.categoria

class Tatoo(models.Model):
    imagem = models.ImageField(upload_to='media/%Y/%m/%d/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return self.categoria
    
    

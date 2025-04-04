from django.shortcuts import render
from .models import Produto

def home(request):
    produtos = Produto.object.all()
    return render(request, 'home.html', {'produtos':produtos})

    def detauls(request, produto_id):
        produto = get_object_or_404(Produito, pk=produto_id)
        return render(request, 'details.html', {'produto':produto})

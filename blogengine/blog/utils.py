from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)  #Вoзвращает на странице ошибку 404 если переходишь по несуществующему адресу
        return render(request, self.template, context={self.model.__name__.lower(): obj})


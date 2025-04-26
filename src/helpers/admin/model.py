from django.contrib import admin
from django.db import models

from djangoql.admin import DjangoQLSearchMixin


class CustomModelAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    def get_list_display(self, request):
        exclude = self.exclude if self.exclude else []
        fields = [
            field.name for field in self.model._meta.get_fields() if
            not isinstance(field, (models.ManyToManyField, models.ManyToOneRel, models.ForeignKey))
            and field.name not in exclude
        ]
        return fields

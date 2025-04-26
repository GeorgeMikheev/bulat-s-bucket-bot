from django.contrib import admin
from django.utils.safestring import mark_safe
from djangoql.admin import DjangoQLSearchMixin

from bot.models import Quotation


@admin.register(Quotation)
class QuotationAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = [
        "id",
        "text",
        "human",
        "image_tag"
    ]

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "-"

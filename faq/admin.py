from django.contrib import admin
from .models import FAQ
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'language_display', 'formatted_answer')

    def formatted_answer(self, obj):
        return format_html(obj.answer)

    formatted_answer.short_description = _("Answer")

    def language_display(self, obj):
        return ", ".join([lang for lang in ['en', 'hi', 'bn'] if getattr(obj, f'question_{lang}', None)])

admin.site.register(FAQ, FAQAdmin)

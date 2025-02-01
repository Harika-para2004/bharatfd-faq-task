from django.db import models
from django.utils.translation import gettext_lazy as _
from googletrans import Translator
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))
    question_hi = models.TextField(_("Question (Hindi)"), blank=True, null=True)
    question_bn = models.TextField(_("Question (Bengali)"), blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()

        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text

        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text

        super().save(*args, **kwargs)

    def get_translation(self, lang):
        return getattr(self, f'question_{lang}', self.question)

    def __str__(self):
        return self.question

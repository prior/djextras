from django.db import models
from django import forms
from sanetime import sanetime

class SaneTimeFormField(forms.DateTimeField):
    pass

class SaneTimeField(models.BigIntegerField):

    description = "A field to hold sanetimes (i.e. microseconds since epoch)."

    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(SaneTimeField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not isinstance(value, sanetime):
            value = sanetime(value)
        return value

    def get_prep_value(self, value):
        return int(value)

    #def formfield(self, **kwargs):
        #defaults = {'form_class': SaneTimeFormField}
        #defaults.update(kwargs)
        #return super(SaneTimeFormField, self).formfield(**defaults)



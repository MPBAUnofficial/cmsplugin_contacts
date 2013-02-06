from django.db import models
from django.conf import settings
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField
import os

import easy_thumbnails


class Contacts(CMSPlugin):
    def copy_relations(self, oldistance):
        for old_person in oldistance.person_set.all():
            new_person = Person()
            new_person.contact = self
            new_person.name = old_person.name
            new_person.surname = old_person.surname
            new_person.email = old_person.email
            new_person.telephone = old_person.telephone
            new_person.image = old_person.image
            new_person.description = old_person.description
            new_person.save()


    def __unicode__(self):
        return _(u'%(count)d contact(s)') % {'count': self.person_set.count()}


class Person(models.Model):

    contact = models.ForeignKey(Contacts)
    name = models.CharField(
                                _("name"), 
                                max_length=30,
                                help_text=_("the contact name"),
                            )

    surname = models.CharField(
                                  _("surname"), 
                                  max_length=60,
                                  help_text=_("the contact surname"),
                              )

    email = models.CharField(
                                _("email"), 
                                max_length=30,
                                help_text=_("the contact email adress"),
                            )

    telephone = models.CharField(
                                    _("telephone"), 
                                    max_length=15,
                                    help_text=_("the contact telephone number"),
                                )
    image = FilerImageField( 
                                null=True, 
                                blank=True,
                                verbose_name=_("image")
                           )

    description = models.TextField(
                                      _("description"), 
                                      help_text=_("the contact description"),   
                                  )

    def __unicode__(self):
        return self.name + " " + self.surname

    def get_reverse_mail(self):
        return self.email[::-1]

    class Meta:
        verbose_name=_("person")
        verbose_name_plural=_("persons")

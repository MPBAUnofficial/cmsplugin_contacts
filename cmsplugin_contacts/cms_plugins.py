from django.contrib import admin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Contacts, Person
from os.path import join
from django import forms
from django.utils.translation import ugettext_lazy as _

class ContactAdmin(admin.StackedInline):
    model = Person
    extra = 1


class CMSContactPlugin(CMSPluginBase):
    model = Contacts
    inlines = (ContactAdmin,)
    name = _("Contact list")
    render_template = "cmsplugin_contacts/contact.html"

    def render(self, context, instance, placeholder):                      
        context.update({
            'header':_("Contacts"),
            'contact':instance,      
        })
        return context
 
plugin_pool.register_plugin(CMSContactPlugin)

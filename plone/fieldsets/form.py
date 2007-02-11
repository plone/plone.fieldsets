from plone.fieldsets.interfaces import IFormFieldsets
from zope.formlib import form

from Products.Five.formlib.formbase import EditForm


class FieldsetsEditForm(EditForm):
    """An edit form which supports fieldsets."""

    def setUpWidgets(self, ignore_request=False):
        # First part is copied from zope.formlib.form.EditForm licensed under
        # the ZPL 2.1
        self.adapters = {}
        self.widgets = form.setUpEditWidgets(
            self.form_fields, self.prefix, self.context, self.request,
            adapters=self.adapters, ignore_request=ignore_request
            )
        # In order to support fieldsets, we need to setup the widgets on all
        # the fieldsets as well.
        if self.is_fieldsets():
            for fieldset in self.form_fields.fieldsets:
                fieldset.widgets = form.setUpEditWidgets(
                    fieldset, self.prefix, self.context, self.request,
                    adapters=self.adapters, ignore_request=ignore_request
                    )

    def is_fieldsets(self):
        # We need to be able to test for non-fieldsets in templates.
        return IFormFieldsets.providedBy(self.form_fields)

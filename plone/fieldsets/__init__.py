import zope.deferredimport

zope.deferredimport.deprecated(
    "The convenience import confuses the test coverage tools. "
    "Please use the fully qualified name instead.",
    FormFieldsets = 'plone.fieldsets.fieldsets:FormFieldsets',
    )

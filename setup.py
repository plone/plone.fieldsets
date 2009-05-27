import os
from setuptools import setup, find_packages

version = '2.0a2'

setup(name='plone.fieldsets',
      version=version,
      description="An extension to zope.formlib, which allows to group fields into different fieldsets.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        ],
      keywords='zope formlib fieldsets',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.fieldsets',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'zope.app.form',
            'zope.publisher',
            'zope.testing',
            ],
      ),
      install_requires=[
        'setuptools',
        'zope.component',
        'zope.formlib',
        'zope.interface',
        'zope.schema',
      ],
      )

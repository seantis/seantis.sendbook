from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='seantis.sendbook',
      version=version,
      description="Sends ftw.book Books as email",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Seantis GmbH',
      author_email='info@seantis.ch',
      url='https://github.com/seantis/seantis.sendbook',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['seantis'],
      include_package_data=True,
      zip_safe=False,
      
      install_requires=[
          'setuptools',
          'plone.app.z3cform',
          'ftw.book',
      ],
      
      tests_require=[
          'plone.app.testing',
      ],
      
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )

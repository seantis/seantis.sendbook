seantis.sendbook
========

This package provides a additional document action to send "Books" as a PDF attachment to an email address. It's an addon package to `ftw.book package <https://github.com/4teamwork/ftw.book>`_


Features
--------

- Provides a document action "sendbook" for the content type "Book".
- If the action "sendbook" is used on the "IBook" interface then the entire PDF is sent.
- If the action is used on a "IChapter" interface the corresponding chapter is sent in PDF format.


Usage
-----

- Add ``seantis.sendbook`` to your buildout configuration:

::

    [instance]
    eggs +=
        seantis.sendbook

- Install the generic import profile.


Links
-----

- Main github project repository: https://github.com/seantis/seantis.sendbook
- Issue tracker: https://github.com/seantis/seantis.sendbook/issues
- Package on pypi: http://pypi.python.org/pypi/seantis.sendbook


Copyright
---------

This package is copyright by `seantis gmbh <http://www.seantis.ch>`_.

``seantis.sendbook`` is licensed under GNU General Public License, version 2.
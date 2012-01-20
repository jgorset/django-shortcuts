Django shortcuts
================

You spend too much time typing ``python manage.py``.

Usage
-----

Django shortcuts installs a ``django`` binary that proxies
Django's ``manage.py`` and ``django-admin.py`` scripts.

::

    $ django <command or shortcut>

    $ cd any/project/subdirectory
    $ django <command or shortcut>

Shortcuts
---------

::

    r     ->    runserver
    s     ->    shell
    t     ->    test
    sm    ->    schemamigration
    m     ->    migrate
    sd    ->    syncdb
    d     ->    dbshell
    sp    ->    startproject

Installation
------------

::

    $ pip install django-shortcuts

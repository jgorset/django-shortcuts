# Django shortcuts

## About

You spend way too much time typing `python manage.py [...]`.

## Usage

    $ python manage.py runserver
    $ django runserver
    $ django r

    $ python manage.py shell
    $ django shell
    $ django s

    $ cd any/project/subdirectory
    $ django s

## Shortcuts

    * python manage.py runserver -> django r
    * python manage.py shell -> django s
    * python manage.py dbshell -> django d
    * python manage.py syncdb -> django sd
    * python manage.py schemamigration [...] -> django sm [...]
    * python manage.py migrate [...] -> django m [...]
    * python manage.py test [...] -> django t [...]
    * django-admin.py startproject [...] -> django sp

## Installation

    $ pip install django-shortcuts

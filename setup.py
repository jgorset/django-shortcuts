from distutils.core import setup

readme = open('README.rst')

setup(
    name = 'django-shortcuts',
    version = '1.1',
    description = "You spend way too much time typing 'python manage.py'",
    long_description = readme,
    author = "Johannes Gorset",
    author_email = "jgorset@gmail.com",
    url = "http://github.com/jgorset/django-shortcuts",
    scripts = ['scripts/django']
)

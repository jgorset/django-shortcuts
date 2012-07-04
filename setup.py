from distutils.core import setup

readme = open('README.rst').read()

setup(
    name = 'django-shortcuts',
    version = '1.3',
    description = "You spend way too much time typing 'python manage.py'",
    long_description = readme,
    author = "Johannes Gorset",
    author_email = "jgorset@gmail.com",
    url = "http://github.com/jgorset/django-shortcuts",
    scripts = ['scripts/django'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ]
)

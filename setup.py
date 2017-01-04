import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
setup(
    name='mezzanine-kartoza',
    version='0.0.1',
    license='Simplified BSD',

    install_requires=[
        'cartridge',
        'Django>=1.8,<1.9',
        'django-compressor',
        'filebrowser-safe==0.4.5',
        'html5lib==0.9999999',
        'icalendar==3.0.1b2',
        'mezzanine',
        'mezzanine-mdown',
        'mezzanine_people',
        'mezzanine-references',
        'mezzanine-slides',
        'OWSLib==0.12',
        'Mezzanine >= 3.1.10'],

    dependency_links=[
        'git+https://github.com/dimasciput/mezzanine-careers.git@develop',
        'git+https://github.com/meomancer/mezzanine-modal-announcements.git@develop',
        'git+https://github.com/meomancer/mezzanine-file-collections.git@master',
        'git+https://github.com/meomancer/django-wms-client.git@mezzanine',
    ],

    description='Easily plug a slideshow into your mezzanine website on all pages.',
    long_description=open('README.rst').read(),

    author='',
    author_email='',

    url='',
    download_url='',

    include_package_data=True,

    packages=find_packages(),

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django'])

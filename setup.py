from setuptools import setup

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

    author='Isaac Bythewood',
    author_email='isaac@bythewood.me',

    url='http://github.com/overshard/mezzanine-slides',
    download_url='http://github.com/overshard/mezzanine-slides/downloads',

    include_package_data=True,

    packages=['mezzanine_kartoza'],

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django'])

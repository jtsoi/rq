from setuptools import setup

def get_version():
    from times import __version__
    return __version__

setup(
    name='times',
    version=get_version(),
    url='https://github.com/nvie/times/',
    license='BSD',
    author='Vincent Driessen',
    author_email='vincent@3rdcloud.com',
    description='Times is a small, minimalistic, Python library for dealing '
           'with time conversions between universal time and arbitrary '
           'timezones.',
    long_description=__doc__,
    packages=['times'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['pytz'],
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Other Environment',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Environment :: Win32 (MS Windows)',
        'Framework :: Buildout',
        'Framework :: CherryPy',
        'Framework :: Django',
        'Framework :: Plone',
        'Framework :: Pylons',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Office/Business',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'Topic :: System',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ]
)

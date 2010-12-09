from setuptools import setup, find_packages
import os

JQUERYUI_VERSION = '1.8.7'
version = '1.8.7'
# Name version after JQUERY_TOOLTIP_VERSION + .suffix

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jqueryui', 'test_jqueryui.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jqueryui',
    version=version,
    description="fanstatic jQuery UI.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery',
        'setuptools',
        ],
    extras_require = dict(
        test=['pytest >= 2.0'],
        ),
    entry_points={
        'console_scripts': [
            'prepare = js.jqueryui.prepare:main',
            ],
        'fanstatic.libraries': [
            'jqueryui = js.jqueryui:library',
            ],
        },
    )

from setuptools import setup, find_packages
import os

version = '1.12.1.dev0'


def read(*rnames):
    """Read a file from a path."""
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


long_description = "\n\n".join([
    read('README.rst'),
    read('js', 'jqueryui', 'test_jqueryui.rst'),
    read('CHANGES.rst'),
])


setup(
    name='js.jqueryui',
    version=version,
    description="jQuery UI packaged for fanstatic.",
    long_description=long_description,
    classifiers=[],
    url='https://bitbucket.org/fanstatic/js.jqueryui',
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
    entry_points={
        'fanstatic.libraries': [
            'jqueryui = js.jqueryui:library',
        ],
    },
)

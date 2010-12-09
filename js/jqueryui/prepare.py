"""
WARNING.

This script works to a certain extent. The resulting __init__.py needs some
finetuning after pulling in the jquery ui code. Use a good diff tool or
improve this script.
"""
import py
import os
import sys
import urllib2

from fanstatic import generate_code, ResourceInclusion, Library

UI_URL = 'http://jquery-ui.googlecode.com/files/jquery-ui-%s.zip'
THEMES_URL = 'http://jquery-ui.googlecode.com/files/jquery-ui-themes-%s.zip'

def prepare_jqueryui(package_dir, version):
    jqueryui_dest_path = package_dir.join('resources/ui')
    jquerythemes_dest_path = package_dir.join('resources/themes')

    # remove previous builds
    if jqueryui_dest_path.check():
        print 'removing "%s"' % jqueryui_dest_path
        jqueryui_dest_path.remove()
    print 'create new "%s"' % jqueryui_dest_path
    jqueryui_dest_path.ensure(dir=True)

    if jquerythemes_dest_path.check():
        print 'removing "%s"' % jquerythemes_dest_path
        jquerythemes_dest_path.remove()
    print 'create new "%s"' % jquerythemes_dest_path
    jquerythemes_dest_path.ensure(dir=True)

    # download jquery ui
    file_data = urllib2.urlopen(UI_URL % version).read()
    temp_dir = py.path.local.mkdtemp()
    zip_file = temp_dir.join('zipfile.zip')
    open(zip_file.strpath, 'wb').write(file_data)
    print "unzipping jquery ui"
    unzip_dir = temp_dir.join('unzipped')
    os.system('unzip -qq "%s" -d "%s"' % (zip_file, unzip_dir.strpath))
    ui_dir = unzip_dir.listdir()[0].join('ui')
    ui_dir.copy(jqueryui_dest_path)


    # download jquery themes
    file_data = urllib2.urlopen(THEMES_URL % version).read()
    temp_dir = py.path.local.mkdtemp()
    zip_file = temp_dir.join('zipfile.zip')
    open(zip_file.strpath, 'wb').write(file_data)
    print "unzipping jquery themes"
    unzip_dir = temp_dir.join('unzipped')
    os.system('unzip -qq "%s" -d "%s"' % (zip_file, unzip_dir.strpath))
    themes_dir = unzip_dir.listdir()[0].join('themes')
    themes_dir.copy(jquerythemes_dest_path)

    print "generating theme information"
    py_path = package_dir.join('__init__.py')
    print 'Generating inclusion module "%s"' % py_path

    library = Library('jqueryui', 'resources')
    inclusion_map = {'jqueryui': ResourceInclusion(
        library, 'ui/jquery-ui.js', minified='ui/minified/jquery-ui.min.js')}

    for theme in jquerythemes_dest_path.listdir():
        print theme, theme.basename
        if not theme.check(dir=True):
            continue
        theme_name = str(theme.basename)
        python_theme_name = theme_name.replace('-', '_')
        inclusion_map[python_theme_name] = ResourceInclusion(library,
            'themes/%s/jquery-ui.css' % theme_name)

    code = generate_code(**inclusion_map)
    module = py_path.open('w')
    module.write(code)
    module.close()

def main():
    prepare_jqueryui(py.path.local(os.path.dirname(__file__)), sys.argv[1])

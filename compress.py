import os
import subprocess

online_yui_compressor_url = 'https://refresh-sf.herokuapp.com/'


################################################################

def compress(infile, outfile):
    """Compress a source file using cleancss resp. uglifyjs

    :param string infile: The input file name.
    :param string outfile: The output file name.
    """
    srctypes = {
        '.css': 'cleancss',
        '.js': 'uglifyjs',
    }

    _, ext = os.path.splitext(infile)
    if ext not in srctypes:
        raise ValueError("unknown file extension for file %r" % infile)

    print('compressing %r to %r' % (infile, outfile))
    subprocess.check_call([srctypes[ext], infile, '-o', outfile])


def needs_compress(path):
    _, name = os.path.split(path)
    if '.min.' in name:
        return False
    base, ext = os.path.splitext(name)
    if ext not in ['.css', '.js']:
        return False
    return not os.path.exists(min_path(path))


def min_path(path):
    dir, name = os.path.split(path)
    base, ext = os.path.splitext(name)
    return os.path.join(dir, "{}.min{}".format(base, ext))


def listdir_recursively(top):
    for dirpath, dirnames, filenames in os.walk(top):
        for filename in filenames:
            yield os.path.join(dirpath, filename)


def compile_resource_declarations(resources_dir):
    for relpath in listdir_recursively(resources_dir):
        if needs_compress(relpath):
            compress(relpath, min_path(relpath))


def main():
    package_dir = os.path.dirname(__file__)
    resources_dir = os.path.join(package_dir, 'js', 'jqueryui', 'resources')

    old_cwd = os.getcwd()
    os.chdir(resources_dir)
    compile_resource_declarations('.')
    os.chdir(old_cwd)

if __name__ == '__main__':
    main()

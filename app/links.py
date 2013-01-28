import errno
import os
import shutil

force_install = True if os.getenv('FORCE') else False


def force_link(source, target):
    """
    ln -sf
    """
    try:
        os.symlink(source, target)
    except OSError, e:
        if e.errno == errno.EEXIST:
            if force_install:
                if os.getenv('DEBUG'):
                    print('Removing {0}'.format(target))
                if not os.path.islink(target) and os.path.isdir(target):
                    shutil.rmtree(target)
                else:
                    os.remove(target)
                os.symlink(source, target)
            else:
                print('{0} exists. Remove or use FORCE=yes'.format(target))


def init():
    for f in os.listdir('files'):
        force_link(orig_path('files', f), dot_home(f))

    for f in os.listdir('omz'):
        source = orig_path('omz', f)

        if os.path.isdir(source):
            force_link(source, omz_plugin(f))
        else:
            force_link(source, omz_custom(f))


def orig_path(prefix, f):
    return os.path.join(os.getcwd(), prefix, f)


def dot_home(f):
    return os.path.expanduser('~/.' + f)


def omz_custom(f):
    return os.path.join(os.path.expanduser('~/.oh-my-zsh/custom'), f)


def omz_plugin(f):
    return os.path.join(os.path.expanduser('~/.oh-my-zsh/custom/plugins'), f)

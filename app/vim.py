import os

# Can override the default path to MacVim if need be
_macvim = os.getenv('MACVIM') or '/Applications/MacVim.app/Contents/MacOS/Vim'

# populate vims
_vims = ['vim']

if os.path.isfile(_macvim):
    _vims.append(_macvim)

vimdir = os.getenv('VIMFILES') or os.path.expanduser('~/.vim')

bundledir = os.getenv('VIMBUNDLES') or os.path.join(vimdir, 'bundle')


def nailgun():
    """
    Compile nailgun for the given platform
    """
    ng_path = 'files/vim/lib/vimclojure-nailgun-client'
    if not os.path.isfile(os.path.join(ng_path, 'ng')):
        print('Nailgun needs to be compiled...')
        current_dir = os.getcwd()
        os.chdir(ng_path)

        if os.system('make 1>/dev/null 2>&1') == 0:
            print('Compiled nailgun successfully!')
        else:
            print('Failed to compile nailgun. VimClojure won\'t work')

        os.chdir(current_dir)


def tags():
    """
    Ensure the tags directory exists in vim (not tracked by git)
    """
    if not os.path.isdir('files/vim/tags'):
        print("Making vim tags directory")
        os.makedirs('files/vim/tags')


def has(feature):
    """
    Test if vim was compiled with a certain feature
    """
    for vim in _vims:
        if os.system('{0} --version | grep -q +{1}'.format(vim, feature)) == 0:
            return True
    return False


def has_python():
    return has('python')


def has_ruby():
    return has('ruby')

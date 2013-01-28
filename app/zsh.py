import os

_url = 'git://github.com/robbyrussell/oh-my-zsh.git'


def oh_my():
    ohmyzsh = os.path.expanduser('~/.oh-my-zsh')

    if not os.path.isdir(ohmyzsh):
        if os.system('git clone {0} {1}'.format(_url, ohmyzsh)) == 0:
            print('oh-my-zsh has been installed!')
        else:
            print('oh-my-zsh failed to install!')
            exit(1)

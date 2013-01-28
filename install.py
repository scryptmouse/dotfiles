#!/usr/bin/env python

from app import links, vim, zsh

zsh.oh_my()

vim.tags()
vim.nailgun()

links.init()

print("Be sure to reload zsh and run vundle to install Vim bundles.")

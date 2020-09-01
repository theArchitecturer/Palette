from ..__init__ import Palette 

def hello():
    if Palette.vscodeDir is None:
        Palette.nvim.call("fzf#run", opts)


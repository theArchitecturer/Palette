import pynvim
import re
import json
import os
import os.path
from importlib import import_module
from palette import fzf, dot_vscode

@pynvim.plugin
class Palette(object):

    def __init__(self, nvim) -> None:
        self.nvim = nvim
        # self.vscodeDir = dot_vscode.find_vscode(nvim.eval('expand("%:p")'))
        self.vscodeDir = None

    def workspaceFolder(cls):
        return dot_vscode.find_workspace(self.file())

    def workspaceFolderBasename(cls):
        return cls.workspaceFolder.split('/')[-1]

    def file(cls):
        return cls.nvim.eval('expand("%:p")')

    def relativeFile():
        return os.path.relpath(cls.file(), cls.workspaceFolder())

    def relativeFileDirname():
        return os.path.relpath(cls.fileDirname(), cls.workspaceFolder())

    def fileBasename(cls):
        return cls.nvim.eval('expand(%:t)')

    def fileBasenameNoExtension(cls):
        return cls.nvim.eval('expand(%:r)')

    def fileDirname(cls):
        return cls.nvim.eval('expand("%:p:h")') 

    def fileExtname(cls):
        return ".{}".format(cls.nvim.eval('expand("%:eh")'))

    def lineNumber(cls):
        return cls.nvim.eval('line(".")')

    def selectedText(cls):
        start, end = nvim_eval("getpos(\"'<\")"), nvim_eval("getpos(\"'>\")")
        return start, end

    # def parse_command(cls):
    #     commandList = re.split(r'\$\{', cls.command) 
    #     _return = ''
    #     for command in commandList:
    #         answer = re.match(r'^.*\}', command)
    #         if answer is not None:
    #             _return += re.sub(answer, getattr(Macro, f"{str(command[answer.start():answer.end()-1])}")(), command)
    #         else:
    #             _return += command

    #     return _return

    # @pynvim.command('Echom', eval='expand("%:p")')
    # def call_build(self, filePath):
    #     if self.vscodeDir is None:
    #     if self.taskFile is None:
    #         _file = os.path.join(self.vscodeDir, 'task.json')
    #         self.taskFile = task_json.build_task_json(_file)
    # hello ={ "Tasks: Configure Default Build Task": ['task', 'hello'],
    #         }
    def hello_handle(self):
        if self.vscodeDir is None:
            self.vscodeDir = dot_vscode.find_vscode(self.nvim.eval('expand("%:p")'))
        _file = os.path.join(self.vscodeDir, 'task.json')
        if os.path.isfile(_file):
            pass
        else:
            self.nvim.call("fzf#run", {'source': ['create Task.json from template']})


    @pynvim.command('PaletteHandle', nargs=1, sync=True)
    def palette_handle(self, arg):
        # self.hello_handle()
        # ext = re.match("^(\w+)", arg[0])
        # self.nvim.command(f'echo "{arg[0]}"')
        # module = import_module(f"{hello[arg[0]][0]}.main")
        # getattr(module, hello[arg[0]][1])
        self.nvim.command("let fzf_action = { 'ctrl-r': function('s:build_quickfix_list')}")
        self.nvim.call("fzf#run", fzf.paletehandle_opts)

    # @pynvim.function('colorscheme_palette')
    # def colorscheme_palette(self, arg):
    #     self.nvim.command(f"echo {arg[0]}")

    @pynvim.command('Palette')
    def open_command_palete(self):
        self.nvim.call("fzf#run", fzf.palete_opts)

    # @pynvim.command('Task')
    # def task(self):
    @pynvim.function('OpenWindow')
    def open_window(self, arg):
        height = int(self.nvim.current.window.height/2)
        width = int(self.nvim.current.window.width/2)
        buf = self.nvim.call("nvim_create_buf", False, True)
        opts = {
                'relative': 'win',
                'row': int(height/2),
                'col': int(width/2),
                'width': width,
                'height': height,
                # 'style': 'minimal'
                }
        win = self.nvim.call("nvim_open_win", buf, True, opts)
        self.nvim.command('set nonumber')
        # self.nvim.command("terminal")
        # self.nvim.command("echo '{arg}' | fzf --layout=reverse")
        # self.nvim.command("startinsert")
        # self.nvim.command("set ")

    # def set_colorscheme(self, theme):
    #     self.nvim.call("colorscheme", theme)

    # @pynvim.function('preferences_color_theme')
    # @pynvim.function('Set_color_theme')
    # def colorscheme(self, args):
    #     colorschemes = self.nvim.eval("globpath(&rtp, 'colors/*.vim')")
    #     output = ''
    #     _list = re.findall(r"colors\/.*?\.vim", colorschemes)
    #     for mem in _list:
    #         output += f"{mem[7:-4]}\n"

    #     self.open_window(output)


        # self.nvim.command(f"echo '{output}'")


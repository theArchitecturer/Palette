import neovim
import json
import os
from palette import fzf, dot_vscode

@neovim.plugin
class Simple(object):

    def __init__(self, nvim) -> None:
        self.nvim = nvim
        self.vscodeDir = dot_vscode.find_vscode(nvim.eval('expand("%:p")'))
        # self.taskFile = None

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

    def parse_command(cls):
        commandList = re.split(r'\$\{', cls.command) 
        _return = ''
        for command in commandList:
            answer = re.match(r'^.*\}', command)
            if answer is not None:
                _return += re.sub(answer, getattr(Macro, f"{str(command[answer.start():answer.end()-1])}")(), command)
            else:
                _return += command

        return _return

    # @neovim.command('Echom', eval='expand("%:p")')
    # def call_build(self, filePath):
    #     if self.vscodeDir is None:
    #     if self.taskFile is None:
    #         _file = os.path.join(self.vscodeDir, 'task.json')
    #         self.taskFile = task_json.build_task_json(_file)
    @neovim.command('PaletteHandle')
    def palette_handle(self, arg):
        self.nvim.command(f"echo {arg.replace(' ', '_')}")

    @neovim.command('Palette')
    def open_command_palete(self):
        self.nvim.call("fzf#run", fzf.palete_opts)

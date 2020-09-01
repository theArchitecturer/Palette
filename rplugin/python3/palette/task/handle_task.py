import re
import neovim
import pathlib
import os
import os.path

class HandleKey():
    def __init__(self):
        self.task = []

    def _handle_label(self, key):
        return self.task[key]

    def _handle_group(self, key):
        return self.task[key]

    def _handle_task(self, task) -> dict:
        pass
        # self.task = task
        # keyToCheck = ['label', 'group']
        # toReturn = {}

        # for key in keyToCheck:
        #     pass
            # toReturn[key] = getattr(HandleKey, f'_handle_{key}')(self, key)
        # obj = Macro('${file}')
        # print(obj.parse_command())

class Tasks():
    def __init__(self, vscodeDir):
        self.vscodeDir = vscodeDir 

    def configure_default_build_task(self):
        if not os.path.isFile(os.path.join(vscodeDir, 'tasks.json')):
            pass




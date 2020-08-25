import re
import neovim
import pathlib
import os
import os.path
from task import dot_vscode

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

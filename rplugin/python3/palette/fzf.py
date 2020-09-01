import os
import os.path
import json

option = [
        '--layout=reverse',
        '--inline-info',
        '-m',
        ]
option_d = [
        '--layout=reverse',
        '--inline-info',
        '-m',
        ]
window = {
        'width': 0.5,
        'height': 0.5,
        'xoffset': 0.5,
        'yoffset': 0.5
        }
# opts = {
#         'source': _fzf_get_source(),
#         'options': option,
#         'window': window
#         } 
        # "Tasks: Configure Default Test Task",
        # "Tasks: Configure Task",
        # "Tasks: Run Build Task" }
hello ={ "Tasks: Configure Default Build Task": ['task', 'hello'],
        "Change color scheme": ""
        }

def _source():
    return list(hello.keys())
#     plug_dir, _ = os.path.split(os.path.abspath(__file__))
#     _return = []
#     with open(os.path.join(plug_dir, 'data', f"{name}.json")) as inFile:
#         data = json.load(inFile)[field]
#         for line in data:
#             _return.append(f"{field}: { line }")
#         return _return
    # _return = []
    # for index, element in enumerate(list):
    #     _return.append(f'{index})



palete_opts = {
        'source': _source(),
        'options': option,
        'window': window,
        'sink': 'PaletteHandle'
        }
paletehandle_opts = {
        'source': _source(),
        'options': option_d,
        'window': window,
        'sink': 'PaletteHandle'
        }

# task_not_found = {
#         'source': _source('tasks', 'Tasks'),
#         'options': option,
#         'window': window,
#         }

# palete_opts = {
#         'source': 'Build',
#         'options': [ 
#             '--header="not found"',
#             '--layout=reverse',
#             '--inline-info',
#             '-m'
#             ],

#         'window': window,
#         'sink': 'PaletteHandle'
#         }

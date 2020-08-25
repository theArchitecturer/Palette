import os
import os.path
import json

option = [
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

def _source(name, field):
    plug_dir, _ = os.path.split(os.path.abspath(__file__))
    _return = []
    with open(os.path.join(plug_dir, 'data', f"{name}.json")) as inFile:
        data = json.load(inFile)[field]
        for line in data:
            _return.append(f"{field}: { line }")
        return _return


palete_opts = {
        'source': _source('palette', 'Tasks'),
        'options': option,
        'window': window
        }

task_not_found = {
        'source': _source('tasks', 'Tasks'),
        'options': option,
        'window': window,
        'sink': 'PaletteHandle'
        }

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

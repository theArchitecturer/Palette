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
    with open(os.path.join(plug_dir, 'data', f"{name}.json")) as inFile:
        data = json.load(inFile)
        return data[field]


palete_opts = {
        'source': _source('palette', 'Tasks'),
        'options': option,
        'window': window
        }

palete_opts = {
        'source': _source('tasks', 'Tasks'),
        'options': option,
        'window': window,
        'sink': 'PaletteHandle'
        }


import pathlib

import ruamel.yaml as yaml

root = pathlib.Path(__file__).parent

for key, value in yaml.safe_load((root / 'tasks.yaml').read_text()).items():
    globals()[key] = value
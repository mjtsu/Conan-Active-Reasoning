import pathlib

import ruamel.yaml as yaml

root = pathlib.Path(__file__).parent

for key, value in yaml.safe_load((root / 'survivals.yaml').read_text()).items():
    globals()[key] = value
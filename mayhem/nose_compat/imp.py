"""Drop-in replacement for the single `imp` function tests/test_examples.py uses
(`imp.load_source`). The stdlib `imp` module was removed in CPython 3.12; nose/importer.py
depends on it too, which is why real `nose` cannot install here at all (see nose/tools.py
under mayhem/nose_compat/nose/).
"""
import importlib.util


def load_source(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

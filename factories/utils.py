import os
import sys
import types


# -- Our direct file loading depends on whether we're
# -- in python 2 or python 3. We generate the relevant function depending on
# -- the current interpreter version.
if sys.version_info >= (3, 5):
    import importlib.util

    def import_from_source(module_name, filepath):
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

elif sys.version_info >= (3, 0):
    from importlib.machinery import SourceFileLoader
    import importlib.util

    def import_from_source(module_name, filepath):
        ext = os.path.splitext(filepath)[1]
        if ext == '.py':
            module = SourceFileLoader(module_name, filepath).load_module()
        elif ext == '.pyc':
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        else:
            raise ImportError('File type "{}" not supported (.py or .pyc only).'.format(ext))
        return module

# -- Python 2.7
else:
    # noinspection PyUnresolvedReferences
    import imp

    def import_from_source(module_name, filepath):
        ext = os.path.splitext(filepath)[1]
        if ext == '.py':
            module = imp.load_source(module_name, filepath)
        elif ext == '.pyc':
            with open(filepath, 'rb') as fp:
                module = imp.load_compiled(module_name, filepath, fp.read())
        else:
            raise ImportError('File type "{}" not supported (.py or .pyc only).'.format(ext))
        return module


def is_same_path(path_a, path_b):
    """
    Compare the given paths.
    Paths are expanded and normalized on comparison.
    :param str path_a: Path to compare.
    :param str path_b: Path to compare.
    :return bool: True if the paths are the same.
    """
    norm_path = lambda x: os.path.realpath(os.path.normpath(x))
    return norm_path(path_a) == norm_path(path_b)


def is_module(obj):
    """
    Get if <obj> is a module.
    :param object obj:
    :rtype: bool
    """
    return isinstance(obj, types.ModuleType)

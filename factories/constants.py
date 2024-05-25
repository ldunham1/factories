import logging
import os


# ------------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('factories')


# ------------------------------------------------------------------------------
DEBUG_ENVVAR = 'PYTHON_FACTORIES_DEBUGGING'


class ModuleImportMechanism:
    """
    Module import mechanism for loading plugins from paths.

        * GUESS
            This is the default mechanism. When guessing the factory
            will attempt to utilise the IMPORTABLE method first, and
            only if the module is not accessible from within
            sys.modules will it fall back to LOAD_SOURCE. This method
            means you do not have to care too much, and is default
            behaviour.

        * LOAD_SOURCE
            This is useful when your plugin code is outside of the
            interpreters sys.path. This mechanism will load the file
            directly rather than import it from sys.modules.
            This method has flexibility in terms of structure but
            means you cannot utilise relative import paths within
            your plugin. All loaded plugins using this module are
            imported into a namespace defined through a uuid.

        * IMPORTABLE:
            This mechanism should be used if your code resides within
            already importable locations. This method is mandatory if
            your code contains relative imports. Because this is
            importing modules which are available on the sys.path the
            class names will resolve nicely too.
    """

    GUESS = 0
    LOAD_SOURCE = 1
    IMPORTABLE = 2


# ------------------------------------------------------------------------------
def enable_debugging(state=True):
    """
    Convenience function for enabling the debug log output of factories.
    :param bool state: If True then debug log messages will be output.
    """
    if state:
        log.setLevel(logging.DEBUG)

    else:
        log.setLevel(logging.NOTSET)


enable_debugging(
    os.environ.get(DEBUG_ENVVAR, False),
)

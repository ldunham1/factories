import logging
import os


# ------------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('factories')


# ------------------------------------------------------------------------------
DEBUG_ENVVAR = 'PYTHON_FACTORIES_DEBUGGING'


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

import json

from factories.examples.reader import ReaderPlugin


# ------------------------------------------------------------------------------
class JSONReader(ReaderPlugin):

    version = 1

    # --------------------------------------------------------------------------
    @classmethod
    def contents(cls, filepath):
        """
        This should return a dictionary of data collated from the
        file.
        .. note:: This MUST be re-implemented in the plugin
        :param str filepath: Absolute filepath to file
        :return dict: dictionary of data taken from the file
        """
        with open(filepath, 'r') as f:
            return json.load(f)

    # --------------------------------------------------------------------------
    @classmethod
    def can_read(cls, filepath):
        if filepath.endswith('.json'):
            return True

        return False


# ------------------------------------------------------------------------------
class INIReader(ReaderPlugin):

    version = 1

    # --------------------------------------------------------------------------
    @classmethod
    def contents(cls, filepath):
        """
        This should return a dictionary of data collated from the
        file.
        .. note:: This MUST be re-implemented in the plugin
        :param str filepath: Absolute filepath to file.
        :return dict: dictionary of data taken from the file.
        """
        output = dict()

        with open(filepath, 'r') as f:
            for line in f.readlines():
                data = line.split('=')

                if len(data) == 2:
                    output[data[0].strip()] = data[1].strip()

        return output

    # --------------------------------------------------------------------------
    @classmethod
    def can_read(cls, filepath):
        if filepath.endswith('.ini'):
            return True

        return False

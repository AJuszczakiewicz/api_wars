from configparser import ConfigParser


def config(filename='settings.ini', section="postgres"):
    """Retrives setting data from ini file. """
    parser = ConfigParser()
    parser.read(filename)

    data = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            data[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return data

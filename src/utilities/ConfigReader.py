from configparser import ConfigParser

def read_config(category, key):
    """
        Reads a specific value from the configuration file.

        :param category: Section name in the configuration file.
        :param key: Key whose value needs to be retrieved.
        :return: The value associated with the given key in the specified section.
    """
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)
import configparser

class ReadConfig:
    @staticmethod
    def get_config_value(section, key):
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        return config.get(section, key)

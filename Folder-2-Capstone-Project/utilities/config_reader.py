import configparser


class ConfigReader:

    @staticmethod
    def get_config():

        config = configparser.ConfigParser()

        config.read("config/config.ini")

        return config
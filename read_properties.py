import configparser

config = configparser.RawConfigParser()
config.read("./config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        """This method retrieves the URL from config file"""
        url = config.get('Required information', 'base_url')
        return url
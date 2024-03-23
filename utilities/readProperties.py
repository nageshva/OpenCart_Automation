import configparser
# Here Cofigparser is Package and inside this RawConfigParser is class,for that we have to create a OBJECT
config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url


    @staticmethod
    def getEmail():
        email=config.get('common info','email')
        return email

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

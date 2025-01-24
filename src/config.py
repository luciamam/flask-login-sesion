class Config():
    SECRET_KEY='ac795742030af3592e46af3c40b64c90'


class  DEvelopmentConfig():

    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='melu18ma'
    MYSQL_DB='flask_login_2024_2025'
 

class  ProductionConfig(Config):

    DEBUG=False
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='melu18ma'
    MYSQL_DB='flask_login_2024_2025'




config={
        'development': DEvelopmentConfig,
        'production': ProductionConfig
}



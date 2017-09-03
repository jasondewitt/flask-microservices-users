

class BaseConfig:
    """Base Configuration"""
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Dev Config"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing Config"""
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    """Prod config"""
    DEBUG = False

    

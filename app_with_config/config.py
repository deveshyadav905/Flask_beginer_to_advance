class Config:
    """Base config class containing common settings."""
    SECRET_KEY = 'supersecretkey'
    SESSION_COOKIE_NAME = 'your_session_cookie_name'

class DevelopmentConfig(Config):
    """Development config class that inherits from Config."""
    DEBUG = True
    ENV = 'development'
    DATABASE_URI = 'sqlite:///dev.db'  # Example of database URI for development

class ProductionConfig(Config):
    """Production config class that inherits from Config."""
    DEBUG = False
    ENV = 'production'
    DATABASE_URI = 'sqlite:///prod.db'  # Example of database URI for production
    # In production, it's a good idea to disable debugging for security
    SESSION_COOKIE_SECURE = True  # Use secure cookies for production

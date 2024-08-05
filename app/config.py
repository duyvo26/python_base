# File cấu hình chung cho ứng dụng

import os
from dotenv import load_dotenv

# Load các biến môi trường từ file .env
load_dotenv()


class Settings:
    # FLASK SETTING
    SITE_APP = os.environ["SITE_APP"]
    DEBUG = True
    
    # SETTING
    DIR_ROOT = os.path.dirname(os.path.abspath(".env"))

    # FAST API
    API_KEY = os.environ["API_KEY"]


settings = Settings()

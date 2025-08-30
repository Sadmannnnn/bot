import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

class Config:
    def __init__(self):
        # Основной токен бота
        self.TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
        
        # API ключи для различных сервисов
        self.WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
        self.NEWS_API_KEY = os.getenv('NEWS_API_KEY')
        self.OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        
        # Настройки администраторов
        admin_ids = os.getenv('ADMIN_IDS', '').split(',')
        self.ADMIN_IDS = [int(admin_id.strip()) for admin_id in admin_ids if admin_id.strip().isdigit()]
        
        # Прочие настройки
        self.TIMEZONE = os.getenv('TIMEZONE', 'Europe/Moscow')
        self.AI_ENABLED = bool(self.OPENAI_API_KEY)  # Автоматически определяем, включен ли ИИ
        self.DATABASE_NAME = "chatbot_db.sqlite"

# Инициализация конфигурации
config = Config()

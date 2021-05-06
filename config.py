import os

class var():
   APP_ID = os.getenv('APP_ID')
   API_HASH = os.getenv('API_HASH')
   BOT_TOKEN = os.getenv('BOT_TOKEN')
   APP_DOMAIN = os.getenv('APP_DOMAIN')
   PORT = os.getenv('PORT', 6969)

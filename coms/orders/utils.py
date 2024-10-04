import os

def get_sms_config():
    return {
        "apikey": os.getenv("AT_API_KEY"),
        "username": os.getenv("AT_USERNAME")
    }

def send_sms(to, message):
    config = get_sms_config()
    # Your code to send SMS using the config

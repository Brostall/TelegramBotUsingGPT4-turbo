import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import openai

# Logging in terminal
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# API OpenAI key
openai.api_key = 'Your api key gpt 4 turbo'

# /start
def start(update, context):
    update.message.reply_text('Hello! Im a bot thats ready to answer your questions.') 

# Function to generate a response using the GPT-4 Turbo chat model
def generate_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo-2024-04-09",  # last model GPT-4 Turbo
        messages=[{"role": "user", "content": user_input}]
    )
    generated_response = response.choices[0].message['content'].strip()
    

# Function to analysis texts
def reply_message(update, context):
    user_input = update.message.text.lower()  
    logger.info(f"User {update.effective_user.username} write: {user_input}")
    response = generate_response(user_input)
    update.message.reply_text(response)

def main():
    # telegram token
    updater = Updater("Your telegram bot token", use_context=True)
    dp = updater.dispatcher

    # Adding Command and Message Handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))

    # Bot start
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


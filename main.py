import requests
import json
from pyrogram import Client, filters

# Define the API URL and headers
API_URL = "https://ai.dataplazma.com/api/v3/completions-stream"
HEADERS = {
    "Host": "ai.dataplazma.com",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "User-Agent": "CHAT%20AI/2 CFNetwork/1408.0.4 Darwin/22.5.0",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTM3MTU3LCJmaXJzdF9uYW1lIjoiTmFmaXMiLCJsYXN0X25hbWUiOm51bGwsIm5pY2tuYW1lIjpudWxsLCJlbWFpbCI6Im5hZmlzZnVhZDM0MEBnbWFpbC5jb20iLCJpbWFnZV91cmwiOm51bGwsIm9zIjoibWFjIiwiaXNfY29uZmlybWVkIjp0cnVlLCJpYXQiOjE3MTYxMTMxMTh9.jrREYvQrd_EIvhV-hRIorf5jBtL71mrSFSNcAUn5XJc",
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br"
}

# Function to communicate with the AI API
def get_ai_response(prompt):
    data = {
        "chatbot_id": 917248,
        "prompt": prompt
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))
    return response.text

# Create a Pyrogram Client
app = Client("my_bot", api_id='5310709', api_hash='63a546bdaf18e2cbba99f87b4274fa05', bot_token='5436508081:AAESJBRXddvCASlPBaSIhJ_rQiOeFIZeSu4')

# Handler for /start command
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hi! I am your AI chat bot. Type your message to start chatting.")

# Handler for text messages
@app.on_message(filters.text & ~filters.command(["start"]))
def handle_message(client, message):
    user_input = message.text
    ai_response = get_ai_response(user_input)
    message.reply_text(ai_response)

# Run the bot
app.run()

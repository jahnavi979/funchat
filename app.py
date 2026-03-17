from flask import Flask, render_template, request, jsonify
import os
app = Flask(__name__)

chat = []

def simple_ai_response(user_msg):
    user_msg = user_msg.lower()

    if "hello" in user_msg:
        return "ochad andi pedhamanishi😊"
    elif "how are you" in user_msg:
        return "nen ala unte nek yendhuku?"
    elif "python" in user_msg:
        return "Python is awesome for web, AI, and automation!"
    elif "hi" in user_msg:
        return "anti chepu😒"
    elif "amchesthunav" in user_msg:
        return "nek la kali ga matram lenu"
    elif "thinnava" in user_msg:
        return "ledhu nuv pedathav ani waiting pora poe pani chusko"
    elif "say something" in user_msg:
        return "this user is a 🐷"
    
    
    else:
        return "urike adhokati aduguthav panikochidhi okati undadhu poe pani chusko po"
    

@app.route('/')
def home():
    return render_template("chat.html")

@app.route('/chat', methods=['GET','POST'])
def chat_api():

    if request.method == 'GET':
        return jsonify([])  
    
    data = request.get_json()
    if not data:
        return {"error": "No data received"}, 400
    user_msg = data.get("message")

    bot_reply = simple_ai_response(user_msg)

    chat.append({"user": user_msg, "bot": bot_reply})

    return {"reply": bot_reply}

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Initialize flask app
app = Flask(__name__)

# Create chatbot instance
chatbot = ChatBot(
    "WebChatBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.TimeLogicAdapter"
    ],
    database_uri="sqlite:///db.sqlite3"
)

#Define routes
def train_chatbot():
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
     return render_template("/index.html")

@app.route("/get_response", methods = ["POST"])
def get_response():
        user_input = request.json.get("message")
        if user_input:
            response = chatbot.get_response(user_input)
            return jsonify({"response": str(response)})
        return jsonify({"response" : "Sorry, I didn't understand that"})
        
if __name__ == "__main__":
    app.run(debug=True)

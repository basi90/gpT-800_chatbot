from flask import Flask, jsonify, request
from flask_cors import CORS
from mongodb_ops import MongoDBOperations
from openai_ops import OpenAIOperations

# Create the Flask application instance
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for all routes
CORS(app)

# Create instances of the MongoDB and OpenAI operations
connection_file_path = "./var_txt/conn_string.txt" # Path to the MongoDB connection string file
mongo_ops = MongoDBOperations(connection_file_path, "chatbot_db", "chat") # Initializing MongoDB operations
openai_ops = OpenAIOperations("./var_txt/api_key.txt") # Initializing OpenAI operations

# Route for chatbot interaction
@app.route('/api/chat', methods=['POST'])
def chat_with_gpt_and_save():
    # Extract the user input from the request
    data = request.get_json()
    user_input =data.get('user_input')
    
    # Define the path to the file containing the system content
    system_content_file_path = "./var_txt/system_content.txt"
    
    # Get the bot response from OpenAI
    bot_response = openai_ops.chat_with_gpt(user_input, system_content_file_path)
    
    # Save the user input and bot response to the MongoDB database
    mongo_ops.save_to_db(user_input, bot_response)    
    
    # Return the bot response as a JSON object
    return jsonify({'bot_response': bot_response})

# Route for closing the MongoDB connection
@app.route('/close', methods=['GET'])
def close_mongo_connection():
    # Close the MongoDB connection
    mongo_ops.close_connection()
    return jsonify({'message': 'MongoDB connection closed.'})

# Run the Flask application in debug mode if executed directly
if __name__ == '__main__':
    app.run(debug=True)
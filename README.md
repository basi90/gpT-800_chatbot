# gpT-800_chatbot

This project is a simple chatbot application built using React for the frontend, Flask for the backend, and integrating MongoDB for data storage. The chatbot leverages OpenAI's GPT-3.5 API for generating responses.

## Features

- **Frontend**: Built with React, providing an interactive chat interface.
- **Backend**: Powered by Flask to handle API requests and communication with the OpenAI GPT-3.5 API.
- **Database**: Uses MongoDB to store chat history and messages.
- **Integration**: Communicates with the OpenAI GPT-3.5 API for generating chatbot responses.
- **Responsive Design**: Implemented with responsiveness in mind using CSS for a seamless experience on different devices.

## Project Structure

- `/front-end`: Contains the React frontend application.
- `/back-end`: Houses the Flask backend server.

## Setup Instructions

### Frontend Setup

1. Navigate to the `front-end` directory.
2. Run `npm install` to install dependencies.
3. Update the API endpoint in `src/components/ChatInterface.js` to point to your Flask backend.
4. Run `npm start` to start the React app.

### Backend Setup

1. Navigate to the `back-end` directory.
2. Create a virtual environment and activate it.
3. Set up MongoDB and update the connection string in `main.py`.
4. Run `python main.py` to start the Flask server.

## Usage

1. Access the chatbot application on your browser at `http://localhost:3000`.
2. Start conversing with the chatbot by entering text in the chat interface.

## Resources

- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [OpenAI GPT-3.5 API](https://platform.openai.com/docs/guides/gpt)

Feel free to contribute or report any issues!!

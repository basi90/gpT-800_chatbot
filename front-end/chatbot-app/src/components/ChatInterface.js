// ChatInterface.js
import React, { useState } from 'react';
import Message from './Message';

const ChatInterface = () => {
  // State for managing messages and user input
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState('');

  // Function to send a user's message to the Flask backend
  const sendMessage = async () => {
    if (userInput.trim() === '') return;

    try {
      const response = await fetch('http://localhost:5000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_input: userInput }),
      });
      const data = await response.json();
      const botResponse = data.bot_response;

      // Add the user's message and the bot's response to the messages state
      setMessages((messages) => [
        ...messages,
        { content: userInput, sender: 'user' },
        { content: botResponse, sender: 'bot' },
      ]);
      // Clear the user's input field
      setUserInput('');
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div className="chat-interface">
      {/* Display the messages */}
      <div className="message-container">
        {messages.map((message, index) => (
          <Message key={index} content={message.content} sender={message.sender} />
        ))}
      </div>
      {/* Input field for the user's messages */}
      <div className="input-container">
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default ChatInterface;

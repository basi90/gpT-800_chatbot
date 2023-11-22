// Message.js
import React from 'react';

// Component for displaying a single message
const Message = ({ content, sender }) => {
  return <div className={`message ${sender}`}>{content}</div>;
};

export default Message;

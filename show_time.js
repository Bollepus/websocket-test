window.addEventListener("DOMContentLoaded", () => {
 const messages = document.createElement("ul");
 document.body.appendChild(messages);

  const websocket = new WebSocket("ws://51.120.2.255:5678/");
     websocket.onmessage = ({ data }) => {
    const message = document.createElement("li");
    const content = document.createTextNode(data);
    message.appendChild(content);
    messages.appendChild(message);
  };
});
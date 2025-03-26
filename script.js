// document.addEventListener("DOMContentLoaded", function () {
//     const chatForm = document.getElementById("chat-form");
//     const chatInput = document.getElementById("chat-input");
//     const chatContainer = document.getElementById("chat-container");

//     chatForm.addEventListener("submit", async function (event) {
//         event.preventDefault();
//         const userMessage = chatInput.value.trim();
//         if (!userMessage) return;

//         // Display user message
//         addMessage("you", userMessage);
//         chatInput.value = "";

//         try {
//             const response = await fetch("http://127.0.0.1:5000/chat", {
//                 method: "POST",
//                 headers: {
//                     "Content-Type": "application/json"
//                 },
//                 body: JSON.stringify({ message: userMessage })
//             });

//             const responseData = await response.json();

//             if (response.ok) {
//                 addMessage("ai", responseData.response);
//             } else {
//                 addMessage("error", "Failed to get response.");
//                 console.error("Server error:", responseData.error);
//             }
//         } catch (error) {
//             addMessage("error", "Network error. Check server connection.");
//             console.error("Fetch error:", error);
//         }
//     });

//     function addMessage(role, text) {
//         const messageElement = document.createElement("div");
//         messageElement.classList.add("message", role);
//         messageElement.textContent = text;
//         chatContainer.appendChild(messageElement);
        
//         // Auto-scroll to the latest message
//         chatContainer.scrollTop = chatContainer.scrollHeight;
//     }
// });
function toggleChat() {
    const chatWindow = document.getElementById('chat-window');
    chatWindow.style.display = chatWindow.style.display === 'none' || chatWindow.style.display === '' ? 'block' : 'none';
}

function sendMessage() {
    const userInput = document.getElementById('user-input').value.trim();
    const chatBody = document.getElementById('chat-body');

    if (userInput === '') return;

    // Display user message
    chatBody.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    document.getElementById('user-input').value = '';

    // Send message to Flask (backend)
    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.response) {
            chatBody.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
        } else {
            chatBody.innerHTML += `<p><strong>Bot:</strong> Sorry, something went wrong.</p>`;
        }
        chatBody.scrollTop = chatBody.scrollHeight; // Auto-scroll to the latest message
    })
    .catch(error => {
        console.error('Error:', error);
        chatBody.innerHTML += `<p><strong>Bot:</strong> Error fetching response.</p>`;
    });
}

// Allow pressing "Enter" to send a message
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

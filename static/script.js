const input = document.querySelector(".chat-input input");
const sendButton = document.querySelector(".chat-input button");
const chatBody = document.querySelector(".chat-body");



// Load FAQs from Flask + SQLite database
async function loadFAQs() {
    try {
        const response = await fetch("/api/faqs");
        const data = await response.json();

        faqData = data.faqs;

        console.log("FAQs loaded from database:", faqData);
    } catch (error) {
        console.error("Error loading FAQs:", error);
    }
}

// Find matching FAQ
function findAnswer(question) {

    const userQuestion = question.toLowerCase().trim();

    // Exact question match
    for (let faq of faqData) {
        if (faq.question.toLowerCase().trim() === userQuestion) {
            return faq.answer;
        }
    }

    // Keyword matching
    const keywords = userQuestion
        .split(/\s+/)
        .filter(word => word.length > 3);

    let bestAnswer = null;
    let bestScore = 0;

    for (let faq of faqData) {

        const faqQuestion = faq.question.toLowerCase();

        let score = 0;

        for (let word of keywords) {
            if (faqQuestion.includes(word)) {
                score++;
            }
        }

        if (score > bestScore) {
            bestScore = score;
            bestAnswer = faq.answer;
        }
    }

    return bestAnswer;
}

// Send message
async function sendMessage() {

    const originalQuestion = input.value.trim();

    if (originalQuestion === "") {
        return;
    }

    const question = originalQuestion.toLowerCase();

    // Show user's question
    const userMessage = document.createElement("div");
    userMessage.className = "message user-message";
    userMessage.textContent = originalQuestion;

    chatBody.appendChild(userMessage);

    let answer = null;

    // Greeting
    if (
         question === "hello" ||
    question === "hi" ||
    question === "hey" ||
    question.startsWith("hello ") ||
    question.startsWith("hi ") ||
    question.startsWith("hey ")
    ) {
        answer = "Hello! 👋 How can I help you with college information?";
    } 
    else {
        // Search answer from database FAQs
        answer = findAnswer(question);
    }

    // Fallback
    if (!answer) {
        answer =
            "Sorry, I don't have information about that question yet. Please try asking about admissions, fees, exams, hostel or library.";
    }

    // Show bot answer
    setTimeout(function () {

        const botMessage = document.createElement("div");
        botMessage.className = "message";
        botMessage.textContent = answer;

        chatBody.appendChild(botMessage);

        chatBody.scrollTop = chatBody.scrollHeight;

    }, 500);

    input.value = "";
}


// Send button
sendButton.addEventListener("click", sendMessage);


// Press Enter to send
input.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }

});

// Quick question buttons
function askQuickQuestion(topic) {

    input.value = topic;

    sendMessage();

}


// Load database FAQs when page opens
loadFAQs();
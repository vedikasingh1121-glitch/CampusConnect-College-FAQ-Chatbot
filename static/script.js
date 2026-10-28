const input = document.querySelector(".chat-input input");
const sendButton = document.querySelector(".chat-input button");
const chatBody = document.querySelector(".chat-body");


// ==============================
// SEND MESSAGE TO NLP BACKEND
// ==============================

async function getBotAnswer(question) {

    try {

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();

        console.log("Detected Intent:", data.intent);
        console.log("Similarity Score:", data.similarity);

        return data.answer;

    } catch (error) {

        console.error("Chatbot error:", error);

        return "Sorry, something went wrong. Please try again.";
    }
}


// ==============================
// SAVE FEEDBACK
// ==============================

async function saveFeedback(
    question,
    answer,
    feedback,
    unresolvedQuery = ""
) {

    try {

        const response = await fetch("/api/feedback", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                question: question,
                answer: answer,
                feedback: feedback,
                unresolved_query: unresolvedQuery

            })

        });


        if (!response.ok) {
            throw new Error("Feedback could not be saved");
        }


        const data = await response.json();

        console.log(data.message);

        return true;

    } catch (error) {

        console.error("Feedback error:", error);

        return false;
    }
}


// ==============================
// SHOW FEEDBACK SECTION
// ==============================

function showFeedbackSection(
    question,
    answer,
    botMessage
) {

    const feedbackContainer = document.createElement("div");

    feedbackContainer.className = "feedback-container";


    const feedbackText = document.createElement("div");

    feedbackText.className = "feedback-text";

    feedbackText.textContent =
        "Was this answer helpful?";


    const buttonContainer = document.createElement("div");

    buttonContainer.className = "feedback-buttons";


    // YES BUTTON
    const yesButton = document.createElement("button");

    yesButton.className = "feedback-btn yes-btn";

    yesButton.textContent = "👍 Yes";


    // NO BUTTON
    const noButton = document.createElement("button");

    noButton.className = "feedback-btn no-btn";

    noButton.textContent = "👎 No";


    buttonContainer.appendChild(yesButton);
    buttonContainer.appendChild(noButton);


    feedbackContainer.appendChild(feedbackText);
    feedbackContainer.appendChild(buttonContainer);


    chatBody.appendChild(feedbackContainer);

    chatBody.scrollTop = chatBody.scrollHeight;


    // ==============================
    // YES CLICK
    // ==============================

    yesButton.addEventListener("click", async function() {

        yesButton.disabled = true;
        noButton.disabled = true;

        await saveFeedback(
            question,
            answer,
            "helpful"
        );

        feedbackText.textContent =
            "Thanks for your feedback! 💜";

        buttonContainer.remove();

    });


    // ==============================
    // NO CLICK
    // ==============================

    noButton.addEventListener("click", function() {

        yesButton.disabled = true;
        noButton.disabled = true;

        feedbackText.textContent =
            "Sorry about that! What information were you looking for?";


        const unresolvedInput =
            document.createElement("input");

        unresolvedInput.className =
            "unresolved-input";

        unresolvedInput.placeholder =
            "Tell us what you were looking for...";


        const submitButton =
            document.createElement("button");

        submitButton.className =
            "unresolved-submit";

        submitButton.textContent =
            "Submit";


        const unresolvedBox =
            document.createElement("div");

        unresolvedBox.className =
            "unresolved-box";


        unresolvedBox.appendChild(unresolvedInput);
        unresolvedBox.appendChild(submitButton);


        feedbackContainer.appendChild(unresolvedBox);


        unresolvedInput.focus();


        // ==============================
        // SUBMIT UNRESOLVED QUERY
        // ==============================

        submitButton.addEventListener(
            "click",
            async function() {

                const unresolvedQuery =
                    unresolvedInput.value.trim();


                if (unresolvedQuery === "") {
                    return;
                }


                submitButton.disabled = true;


                await saveFeedback(
                    question,
                    answer,
                    "not_helpful",
                    unresolvedQuery
                );


                feedbackText.textContent =
                    "Thanks! Your feedback has been recorded. 💜";


                unresolvedBox.remove();
            }
        );

    });

}


// ==============================
// SEND MESSAGE
// ==============================

async function sendMessage() {

    const originalQuestion = input.value.trim();


    if (originalQuestion === "") {
        return;
    }


    const question =
        originalQuestion.toLowerCase();


    // ==============================
    // SHOW USER MESSAGE
    // ==============================

    const userMessage =
        document.createElement("div");

    userMessage.className =
        "message user-message";

    userMessage.textContent =
        originalQuestion;

    chatBody.appendChild(userMessage);

    chatBody.scrollTop =
        chatBody.scrollHeight;


    // ==============================
    // GREETING
    // ==============================

    if (
        question === "hello" ||
        question === "hi" ||
        question === "hey" ||
        question === "hello!" ||
        question === "hi!" ||
        question === "hey!"
    ) {

        const typingMessage =
            document.createElement("div");

        typingMessage.className =
            "typing-indicator";

        typingMessage.textContent =
            "CampusConnect is typing...";

        chatBody.appendChild(typingMessage);

        chatBody.scrollTop =
            chatBody.scrollHeight;


        setTimeout(function() {

            typingMessage.remove();


            const botMessage =
                document.createElement("div");

            botMessage.className =
                "message";

            botMessage.textContent =
                "Hello! 👋 How can I help you with IPS Academy information?";

            chatBody.appendChild(botMessage);

            chatBody.scrollTop =
                chatBody.scrollHeight;

        }, 700);


        input.value = "";

        return;
    }


    // ==============================
    // TYPING INDICATOR
    // ==============================

    const typingMessage =
        document.createElement("div");

    typingMessage.className =
        "typing-indicator";

    typingMessage.textContent =
        "CampusConnect is typing...";

    chatBody.appendChild(typingMessage);

    chatBody.scrollTop =
        chatBody.scrollHeight;


    // ==============================
    // GET NLP ANSWER
    // ==============================

    const answer =
        await getBotAnswer(originalQuestion);


    // ==============================
    // SHOW BOT RESPONSE
    // ==============================

    setTimeout(function() {

        typingMessage.remove();


        const botMessage =
            document.createElement("div");

        botMessage.className =
            "message";

        botMessage.textContent =
            answer;


        chatBody.appendChild(botMessage);

        chatBody.scrollTop =
            chatBody.scrollHeight;


        // ==============================
        // SHOW FEEDBACK
        // ==============================

        showFeedbackSection(
            originalQuestion,
            answer,
            botMessage
        );


    }, 600);


    // Clear input
    input.value = "";
}


// ==============================
// SEND BUTTON
// ==============================

sendButton.addEventListener(
    "click",
    sendMessage
);


// ==============================
// ENTER KEY
// ==============================

input.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {

            event.preventDefault();

            sendMessage();

        }

    }
);


// ==============================
// QUICK QUESTIONS
// ==============================

function askQuickQuestion(topic) {

    input.value = topic;

    sendMessage();

}
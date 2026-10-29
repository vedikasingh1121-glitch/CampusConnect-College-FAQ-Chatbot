from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
from dotenv import load_dotenv
import os
import joblib
from sklearn.metrics.pairwise import cosine_similarity


# Load environment variables
load_dotenv()

app = Flask(__name__)

# ==============================
# CREATE FEEDBACK TABLE
# ==============================

def create_feedback_table():

    conn = sqlite3.connect("college_faq.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT,
            feedback TEXT NOT NULL,
            unresolved_query TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


create_feedback_table()


# ==============================
# LOAD NLP MODEL
# ==============================

model = joblib.load("intent_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# ==============================
# ADMIN AUTHENTICATION
# ==============================

app.secret_key = os.getenv("SECRET_KEY")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def home():
    return render_template("index.html")


# ==============================
# ADMIN LOGIN
# ==============================

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

            session["admin_logged_in"] = True

            return redirect(url_for("admin"))

        return render_template(
            "admin_login.html",
            error="Invalid username or password"
        )

    return render_template("admin_login.html")


# ==============================
# ADMIN PANEL
# ==============================

@app.route("/admin")
def admin():

    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    return render_template("admin.html")


# ==============================
# ADMIN LOGOUT
# ==============================

@app.route("/admin/logout")
def admin_logout():

    session.pop("admin_logged_in", None)

    return redirect(url_for("admin_login"))


# ==============================
# GET FAQs
# ==============================

@app.route("/api/faqs")
def get_faqs():

    conn = sqlite3.connect("college_faq.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, question, answer FROM faqs"
    )

    faqs = cursor.fetchall()

    conn.close()

    return {
        "faqs": [
            {
                "id": row[0],
                "question": row[1],
                "answer": row[2]
            }
            for row in faqs
        ]
    }


# ==============================
# GET USER FEEDBACK
# ==============================

@app.route("/api/feedback")
def get_feedback():

    if not session.get("admin_logged_in"):
        return {"error": "Unauthorized"}, 401

    conn = sqlite3.connect("college_faq.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question, answer, feedback, unresolved_query, created_at
        FROM feedback
        ORDER BY id DESC
    """)

    feedback = cursor.fetchall()

    conn.close()

    return {
        "feedback": [
            {
                "id": row[0],
                "question": row[1],
                "answer": row[2],
                "feedback": row[3],
                "unresolved_query": row[4],
                "created_at": row[5]
            }
            for row in feedback
        ]
    }


# ==============================
# NLP CHATBOT
# ==============================

@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()
    question = data.get("question", "").strip()

    if not question:
        return {
            "answer": "Please enter a question.",
            "intent": None
        }


    # ==============================
    # PREDICT USER INTENT
    # ==============================

    question_vector = vectorizer.transform([question])

    intent = model.predict(question_vector)[0]

    # Diagnostic: show predicted intent in terminal
    print("PREDICTED INTENT:", intent)


    # ==============================
    # GET FAQs FROM DATABASE
    # ==============================

    conn = sqlite3.connect("college_faq.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT question, answer FROM faqs"
    )

    faqs = cursor.fetchall()

    conn.close()


    # ==============================
    # FIND MOST RELEVANT FAQ
    # ==============================

    best_answer = None
    best_score = 0
    best_question = None


    for faq_question, faq_answer in faqs:

        faq_vector = vectorizer.transform([faq_question])

        faq_intent = model.predict(faq_vector)[0]


        # Only compare FAQs from same intent
        if faq_intent == intent:

            similarity = cosine_similarity(
                question_vector,
                faq_vector
            )[0][0]


            if similarity > best_score:

                best_score = similarity
                best_answer = faq_answer
                best_question = faq_question


    # ==============================
    # RETURN BEST MATCH
    # ==============================

    if best_answer is not None:

        return {
            "answer": best_answer,
            "intent": intent,
            "similarity": round(float(best_score), 3)
        }


    # ==============================
    # FALLBACK RESPONSE
    # ==============================

    return {
        "answer": "Sorry, I don't have information about that question yet.",
        "intent": intent
    }


# ==============================
# ADD FAQ
# ==============================

@app.route("/api/faqs", methods=["POST"])
def add_faq():

    if not session.get("admin_logged_in"):
        return {"error": "Unauthorized"}, 401

    data = request.get_json()

    question = data.get("question")
    answer = data.get("answer")

    conn = sqlite3.connect("college_faq.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO faqs (question, answer) VALUES (?, ?)",
        (question, answer)
    )

    conn.commit()
    conn.close()

    return {
        "message": "FAQ added successfully!"
    }, 201


# ==============================
# UPDATE FAQ
# ==============================

@app.route("/api/faqs/<int:faq_id>", methods=["PUT"])
def update_faq(faq_id):

    if not session.get("admin_logged_in"):
        return {"error": "Unauthorized"}, 401

    data = request.get_json()

    question = data.get("question")
    answer = data.get("answer")

    conn = sqlite3.connect("college_faq.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE faqs
        SET question = ?, answer = ?
        WHERE id = ?
        """,
        (question, answer, faq_id)
    )

    conn.commit()
    conn.close()

    return {
        "message": "FAQ updated successfully!"
    }


# ==============================
# DELETE FAQ
# ==============================

@app.route("/api/faqs/<int:faq_id>", methods=["DELETE"])
def delete_faq(faq_id):

    if not session.get("admin_logged_in"):
        return {"error": "Unauthorized"}, 401

    conn = sqlite3.connect("college_faq.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM faqs WHERE id = ?",
        (faq_id,)
    )

    conn.commit()
    conn.close()

    return {
        "message": "FAQ deleted successfully!"
    }


# ==============================
# SAVE USER FEEDBACK
# ==============================

@app.route("/api/feedback", methods=["POST"])
def save_feedback():

    data = request.get_json()

    question = data.get("question", "")
    answer = data.get("answer", "")
    feedback = data.get("feedback", "")
    unresolved_query = data.get("unresolved_query", "")

    if not question or not feedback:
        return {
            "error": "Question and feedback are required."
        }, 400

    conn = sqlite3.connect("college_faq.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO feedback
        (question, answer, feedback, unresolved_query)
        VALUES (?, ?, ?, ?)
        """,
        (
            question,
            answer,
            feedback,
            unresolved_query
        )
    )

    conn.commit()
    conn.close()

    return {
        "message": "Feedback saved successfully!"
    }, 201


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":
    app.run(debug=True)
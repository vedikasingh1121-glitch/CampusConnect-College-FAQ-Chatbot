from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

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

    return {"message": "FAQ added successfully!"}, 201


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

    return {"message": "FAQ updated successfully!"}


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

    return {"message": "FAQ deleted successfully!"}


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":
    app.run(debug=True)
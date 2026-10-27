from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/api/faqs")
def get_faqs():

    conn = sqlite3.connect("college_faq.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, question, answer FROM faqs")

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


@app.route("/api/faqs", methods=["POST"])
def add_faq():

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
 
@app.route("/api/faqs/<int:faq_id>", methods=["PUT"])
def update_faq(faq_id):

    data = request.get_json()

    question = data.get("question")
    answer = data.get("answer")

    conn = sqlite3.connect("college_faq.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE faqs SET question = ?, answer = ? WHERE id = ?",
        (question, answer, faq_id)
    )

    conn.commit()
    conn.close()

    return {"message": "FAQ updated successfully!"}
    
@app.route("/api/faqs/<int:faq_id>", methods=["DELETE"])
def delete_faq(faq_id):

    conn = sqlite3.connect("college_faq.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM faqs WHERE id = ?",
        (faq_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "FAQ deleted successfully!"}


if __name__ == "__main__":
    app.run(debug=True)


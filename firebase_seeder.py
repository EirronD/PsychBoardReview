import firebase_admin
from firebase_admin import credentials, db
import json
import os

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://lovely-learn-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

# Load JSON file
with open("questions.json", "r", encoding="utf-8") as file:
    data = json.load(file)

ref = db.reference("questionBank")

def question_exists(topic, qid):
    existing = ref.child(topic).child(qid).get()
    return existing is not None

def upload_questions():
    for topic, questions in data.items():

        for q in questions:
            qid = q["id"]

            if question_exists(topic, qid):
                print(f"SKIP: {qid} already exists in {topic}")
                continue

            # Upload question
            ref.child(topic).child(qid).set({
                "questionText": q["questionText"],
                "options": q["options"],
                "correctAnswer": q["correctAnswer"],
                "explanation": q.get("explanation", ""),
                "topic": q.get("topic", topic),
                "difficulty": q.get("difficulty", "easy")
            })

            print(f"ADDED: {qid} → {topic}")

upload_questions()

print("DONE 🚀")
from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), "complaints.json")


def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def generate_id(complaints):
    count = len(complaints) + 1
    return f"CMP-{count:03d}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = load_data()
    complaints = data["complaints"]

    new_complaint = {
        "id": generate_id(complaints),
        "name": request.form["name"].strip(),
        "category": request.form["category"],
        "desc": request.form["desc"].strip(),
        "date": datetime.today().strftime("%Y-%m-%d"),
        "status": "Open"
    }

    complaints.append(new_complaint)
    save_data(data)
    return redirect(url_for("admin"))


@app.route("/admin")
def admin():
    data = load_data()
    complaints = data["complaints"]

    category_filter = request.args.get("category", "All")
    status_filter = request.args.get("status", "All")

    filtered = complaints
    if category_filter != "All":
        filtered = [c for c in filtered if c["category"] == category_filter]
    if status_filter != "All":
        filtered = [c for c in filtered if c["status"] == status_filter]

    open_count = sum(1 for c in complaints if c["status"] == "Open")
    in_progress_count = sum(1 for c in complaints if c["status"] == "In Progress")
    resolved_count = sum(1 for c in complaints if c["status"] == "Resolved")

    return render_template(
        "admin.html",
        complaints=filtered,
        open=open_count,
        in_progress=in_progress_count,
        resolved=resolved_count,
        selected_category=category_filter,
        selected_status=status_filter,
        total=len(complaints)
    )


@app.route("/update/<complaint_id>", methods=["POST"])
def update_status(complaint_id):
    data = load_data()
    new_status = request.form["status"]
    for c in data["complaints"]:
        if c["id"] == complaint_id:
            c["status"] = new_status
            break
    save_data(data)
    return redirect(url_for("admin"))


if __name__ == "__main__":
    print("\n✅ Complaint Register is running!")
    print("👉 Open your browser and go to: http://127.0.0.1:5000\n")
    app.run(debug=True)

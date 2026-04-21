# 🗂 Complaint Register
A simple web-based Complaint Management System built with Python and Flask.

---

## 🚀 How to Run (VS Code)

### Step 1 — Open the folder in VS Code
File → Open Folder → select the `complaint_register` folder

### Step 2 — Open the Terminal in VS Code
Press `` Ctrl + ` `` (backtick) to open the terminal

### Step 3 — Install Flask
```bash
pip install flask
```

### Step 4 — Run the app
```bash
python app.py
```

### Step 5 — Open in Browser
Go to: **http://127.0.0.1:5000**

---

## 📁 Project Structure
```
complaint_register/
│
├── app.py              ← Main Flask application
├── complaints.json     ← Data storage (auto-updated)
├── requirements.txt    ← Python dependencies
├── README.md           ← This file
└── templates/
    ├── base.html       ← Shared layout (navbar, styles)
    ├── index.html      ← Complaint submission form
    └── admin.html      ← Admin dashboard
```

---

## ✨ Features
- Submit complaints with Name, Category, Description
- Auto-generated Complaint ID (CMP-001, CMP-002, ...)
- Auto-set Status to "Open" and captures today's date
- Admin dashboard with live stats (Open / In Progress / Resolved)
- Filter complaints by Category and Status
- Update complaint status directly from the dashboard
- Data stored persistently in complaints.json

## 📦 Tech Stack
- Python 3
- Flask (web framework)
- Jinja2 (HTML templating)
- JSON (data storage)
- Plain CSS (no external libraries needed)

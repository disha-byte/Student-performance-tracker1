# TITLE : Student Performance Tracker
The Student Performance Tracker is a web-based application developed using Python (Flask) and SQLite.
Its primary goal is to help teachers and institutions easily manage student data such as roll numbers, names, subjects, and marks.
The system allows teachers to add, view, update, and analyze student performance in a structured way.

# Project Overview  
The Student Performance Tracker is a Flask-based web application that helps teachers manage student academic records.
It allows:
- Adding students and their subject marks
- Viewing student performance
- Calculating subject-wise toppers
-Calculating overall average of each student
-Displaying Obverall Topper
The project uses **SQLite** for database storage and can be deployed to **Heroku / Railway / Render** for online access.  

## ✨ Features  

- 👩‍🎓 **Add Students**  
  Register students with **Roll Number** & **Name**  

- 📚 **Subject & Marks Entry**  
  Enter **multiple subjects** with marks (**0–100**)  

- 🏆 **Topper Highlight**  
  Display **subject-wise toppers** (only one per subject)  

- 📊 **Performance Analysis**  
  Show each student’s **overall average**  

- 💾 **Persistent Storage**  
  Store data securely with **SQLite database**  

- 🌐 **Deployment Ready**  
  Easily deploy on **Heroku / Render / Vercel**  
  
# Tech Stack  
- **Backend**: Python (Flask)  
- **Database**: SQLite (can be extended to MySQL/PostgreSQL)  
- **Frontend**: HTML, CSS, Jinja2 templates  
- **Deployment**: Heroku / Render / Railway

# Project Structure

```bash
student-performance-tracker/
│── app.py # Flask application
│── requirements.txt # Python dependencies
│── Procfile # Deployment configuration (Heroku)
│── README.md # Project documentation
│── students.db # SQLite database (auto-created)
│── templates/ # HTML templates
│ ├── index.html
│ ├── add_student.html
│ ├── view_students.html
│ ├── subject_toppers.html
│ ├── overall_toppers.html
│── static/ # CSS, images, JS (optional)
```

# Workflow
- **opens the website**.
- **Navigates to Add Student → fills roll no, name, subject(s), marks**.
- **Data gets stored in SQLite database**.
- **Teacher can View Student List with all records**.
- **Teacher can Update/Delete entries when needed**.

## requirements.txt
- **This file lists all Python dependencies your app needs**:
- **Flask==3.0.3**
- **Jinja2==3.1.4**
- **Werkzeug==3.0.3**
- **itsdangerous==2.2.0**
- **click==8.1.7**
- **gunicorn==23.0.0**

## Procfile
This tells Heroku/Render how to run your app:
web: gunicorn app:app

# Installation & Setup  
### 1. Clone the repository  

- **git clone https://github.com/bhagyasreeganuga/student-performance-tracker.git**
- **cd student-performance-tracker**

### 2. Create environment
- **python -m venv venv**
- **venv\Scripts\activate     # Windows**
- **source venv/bin/activate  # Mac/Linux**

### 3. Install dependencies
- **pip install -r requirements.txt**

### 4. Run the apllication locally
- **python app.py**

### 5. Database Setup
- **The SQLite database (students.db) will be auto-created when you first run app.py.**

### Deployment
- **Push to GitHub**
- **Use Heroku/Render for free deployment**
### Heroku Deployment
- **1.Login to Heroku**
- **2.heroku login**
- **3.Create app**
- **heroku create student-performance-tracker**
### Push code
- **git add .**
- **git commit -m "Initial commit"**
- **git push heroku main**
### Open app in browser
- **heroku open**

### Author
- **Disha AJ**
- **Vault Of Codes Internship Project**

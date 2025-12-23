# Flask MongoDB To-Do App

A multi-user Task Management application built with Python using the Flask framework and MongoDB. This application allows users to create accounts, log in securely, and manage their own private list of tasks.

# Tech Stack

This project uses a Full Stack Python architecture:

* **Backend:** [Flask](For this I followed a youtube video of coding with sagar) (Python Microframework)
* **Database:** [MongoDB](NoSQL Database)
* **Database Adapter:** [Flask-PyMongo](https://flask-pymongo.readthedocs.io/) I read just the documents for this
* **Frontend:** only used basic HTML
* **Styling:** styling is done by ai I just adjusted it according to my thoughts

# Features

* **User Authentication:**
    * User Registration and Login.
    * Session management using Flask Sessions.
    * Route protection (users cannot access tasks without logging in).
* **Task Management (CRUD):**
    * **Create:** Add new tasks.
    * **Read:** View a list of tasks specific to the logged-in user.
    * **Update:** Toggle tasks as "Done" or "Undo".
    * **Delete:** Remove tasks permanently.
* **Architecture:**
    * Uses **Flask Blueprints** (`auth_bp` and `tasks_bp`) to separate authentication logic from application logic.
    * **Relational Data:** Tasks are linked to specific users via their unique MongoDB ObjectIds.

## 📂 Project Structure

/project-root
│
├── app/
│   ├── __init__.py        # App factory, DB configuration, Blueprint registration
│   ├── routes/
│   │   ├── auth.py        # Login, Register, Logout logic
│   │   └── tasks.py       # Task CRUD operations
│   └── templates/
│       ├── base.html      # Master layout
│       ├── login.html     # Login form
│       ├── register.html  # Registration form
│       └── tasks.html     # Main dashboard

Wallpaper Uploader 🌄
A Django-powered web application for uploading and managing wallpapers. Built with Django for the backend and HTML/CSS for the frontend, this project enables users to upload their wallpaper images and view them via a simple, intuitive interface.

🎯 Features
Image Upload: Users can upload wallpaper images (with validations on formats like JPG, PNG, etc.).
Media Management: Uploaded images are stored under the media/ directory and served via Django's media configuration.
User Interface: Clean and responsive UI built with HTML and CSS for browsing uploaded wallpapers.
Django Admin Panel: Manage wallpapers directly through Django’s admin interface.

wallpaper_uploader/
├── media/                 # Uploaded wallpapers
├── myapp/                 # Django application
│   ├── migrations/
│   ├── models.py          # Wallpaper model
│   ├── views.py           # Upload & display views
│   ├── forms.py           # Image upload forms
│   ├── templates/         # HTML templates
│   └── urls.py            # App-specific routes
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
🛠️ Getting Started
Prerequisites
Python 3.8+
Django (e.g. 3.2+)

pip for installing dependencies

Setup & Run
Clone the repository
git clone https://github.com/KavinsProjects/wallpaper_uploader.git
cd wallpaper_uploader
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run database migrations

bash
Copy
Edit
python manage.py migrate
Start the development server

bash
Copy
Edit
python manage.py runserver
Access the app

Frontend: http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/

✅ Usage Guide
Navigate to the home page to upload a new wallpaper image.

View all uploaded wallpapers in a gallery-style display.

Access the Django Admin site to view, delete, or manage wallpapers more thoroughly.

📦 Tech Stack
Backend: Django (Python)

Frontend: HTML, CSS (static templates)

Database: SQLite (default); easy to switch to PostgreSQL or MySQL

Media: Django's built-in media file handling

🧩 Extending the Project

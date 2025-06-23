# Wallpaper Uploader 🌄

A web application for uploading and managing wallpapers, powered by Django. This project enables users to upload, browse, and manage wallpaper images through a simple, responsive interface and Django’s admin panel.

---

## 🚀 Features

- **Image Upload:** Users can upload wallpaper images (supports JPG, PNG, etc., with validation).
- **Media Management:** Uploaded images are stored in the `media/` directory and served via Django’s media configuration.
- **User Interface:** Clean, responsive UI built with HTML and CSS for browsing uploaded wallpapers.
- **Admin Panel:** Manage wallpapers directly using Django’s built-in admin interface.

---

## 🗂️ Project Structure

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+
- Django 3.2+  
- pip

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/KavinsProjects/wallpaper_uploader.git
    cd wallpaper_uploader
    ```

2. **(Optional) Create and activate a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations**
    ```bash
    python manage.py migrate
    ```

5. **Start the development server**
    ```bash
    python manage.py runserver
    ```

### Access the Application

- **Frontend:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## ✅ Usage Guide

- Visit the home page to upload a new wallpaper image.
- Browse all uploaded wallpapers in a gallery-style display.
- Log in to the Django Admin site to manage wallpapers (add, delete, edit).

---

## 📦 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (static templates)
- **Database:** SQLite (default, easily switchable to PostgreSQL/MySQL)
- **Media:** Django’s built-in media file handling

---

## 🧩 Extending the Project

- Add user authentication for uploads and management.
- Implement categories or tags for wallpapers.
- Enable image resizing/thumbnails.
- Deploy to a cloud platform (Heroku, PythonAnywhere, etc.).
- Replace SQLite with PostgreSQL or MySQL for production.

---

## 📄 License

[MIT License](LICENSE)

---

Feel free to further customize or expand this template to fit your needs!

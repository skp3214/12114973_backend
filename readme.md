# 📋 TaskTracker

TaskTracker is a simple yet powerful task management API built with Django, designed to help you efficiently manage your tasks. 🚀

## ✨ Features

- 📝 Create tasks
- 📜 List all tasks
- 🔍 Get a specific task
- ✏️ Update tasks
- ❌ Delete tasks
- 🗂️ Bulk add tasks
- 🧹 Bulk delete tasks

## ⚙️ Requirements

- 🐍 Python 3.7+
- 📦 pipenv

## 🛠️ Tech Stack

- **Python**
- **Django (DRF)**
- **SQLite Database**

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/skp3214/12114973_frontend.git
   cd TaskTracker
   ```

2. **Install dependencies using pipenv**:
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**:
   ```bash
   pipenv shell
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

## ▶️ Running the Application

To run the application locally, use:

```bash
python manage.py runserver
```

🌐 The API will be accessible at `http://127.0.0.1:8000`.

## 📡 API Endpoints

- ➕ **Create a task**: `POST /v1/tasks/create/`
- 📋 **List all tasks**: `GET /v1/tasks`
- 🔍 **Get a specific task**: `GET /v1/tasks/{task_id}`
- ✏️ **Update a task**: `PUT /v1/tasks/{task_id}/update/`
- ❌ **Delete a task**: `DELETE /v1/tasks/{task_id}/delete/`
- 🗂️ **Bulk add tasks**: `POST /v1/tasks/bulk-add/`
- 🧹 **Bulk delete tasks**: `DELETE /v1/tasks/bulk-delete/`

## 🧪 Running Tests

To run tests, navigate to the `TaskTrackerAPI` directory and run:

```bash
pytest tests.py
```

✨ **Happy Task Tracking!**
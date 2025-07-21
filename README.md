# Employee & Company Upload API (Django REST)

This Django REST API allows you to upload an Excel or CSV file containing employee information, automatically creating associated company records. You can also retrieve paginated employee data via a GET endpoint.

---

## 📦 Features

* Upload employee data via Excel or CSV. Automatically create companies if they don't exist. One-to-many relationship between Company and Employee. Paginated GET endpoint for all employees. Uses `bulk_create()` for efficient database insertion

---

## 🏗️ Tech Stack

* Django, Django REST Framework, Pandas, SQLite (default, can be changed)

---

## 🚀 Setup Instructions

### 1. Clone & Install

```bash
git clone https://github.com/darshan-vaghasiya/brainer_hub_task.git
cd brainer_hub_task
pip install -r requirements.txt  # or install manually as below
```

### 2. Install Dependencies

```bash
pip install djangorestframework pandas openpyxl
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Server

```bash
python manage.py runserver
```

---

## 📤 API Endpoints

### `POST /api/upload-employees/`

Upload an Excel (`.xlsx`) or CSV (`.csv`) file containing employee data.

**Body (form-data):**

* `file`: your\_file.xlsx or .csv

### `GET /api/employees/`

Returns paginated list of all employees (10 per page by default).

**Query Params (optional):**

* `page`: page number
* `page_size`: custom number of results per page

---


# University CRM

This is a CRM (Customer Relationship Management) system for managing university entities such as faculties, groups, kafedras (departments), subjects, teachers, and students. The system is built using Django and Django REST Framework (DRF) to provide a RESTful API.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete operations for all models.
- **RESTful API**: Built using Django REST Framework, providing easy access to university data.
- **Model Relationships**: Models are interlinked to reflect real-world university relationships (e.g., Groups belong to Faculties, Teachers are associated with Subjects, etc.).

## Setup

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mirmakhmudoff/01-University-CRM.git
   cd 01-University-CRM
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server**

   ```bash
   python manage.py runserver
   ```

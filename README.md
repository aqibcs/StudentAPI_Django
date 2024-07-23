# StudentManagerAPI

StudentManagerAPI is a Django-based RESTful API designed to manage student records efficiently. It allows for creating, reading, updating, and deleting student data using standard HTTP methods.

## Features

- **Create Student**: Add new student records.
- **List Students**: Retrieve a list of all students.
- **Retrieve Student**: Get details of a specific student by ID.
- **Update Student**: Modify existing student records.
- **Partial Update Student**: Update specific fields of a student record.
- **Delete Student**: Remove student records.

## Installation

### Prerequisites

- Python 3.6 or higher
- Django 3.x or higher
- Django REST framework 3.x or higher

### Setup

1. **Clone the Repository:**

    ```bash
    git clone git@github.com:aqibcs/StudentAPI_Django.git
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  
    # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the API:**

    Open your web browser and go to `http://127.0.0.1:8000/` to access the API endpoints.

## API Endpoints

- **POST** `/students/` - Create a new student record.
- **GET** `/students/` - Retrieve a list of all student records.
- **GET** `/students/{id}/` - Retrieve a specific student record by ID.
- **PUT** `/students/{id}/` - Update a specific student record by ID.
- **PATCH** `/students/{id}/` - Partially update a specific student record by ID.
- **DELETE** `/students/{id}/` - Delete a specific student record by ID.

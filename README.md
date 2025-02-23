# Python Django Final Project

This is a Django project developed for my Varsity Course. The project demonstrates the use of the Django framework for building web applications, implementing user authentication, CRUD operations, and more.

## Features

- User Authentication (Login, Registration, Logout)
- Dynamic Content Management
- User-friendly interface built with HTML, CSS, and Bootstrap
- Responsive design for mobile and desktop
- Customizable settings for various views and actions


## Installation

To set up and run the application locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/AbidHasanRafi/task-manager-app.git
   ```
2. Navigate to the project directory:
   ```sh
   cd task-manager-app
   ```
3. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
5. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
6. Run migrations:
   ```sh
   python manage.py migrate
   ```
7. Start the development server:
   ```sh
   python manage.py runserver
   ```
8. Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```


## Setup Instructions

### Prerequisites

Make sure you have Python 3.x and pip installed. You will also need to have Django installed.

1. Install Python dependencies:
 
   pip install -r requirements.txt

2.Install Django:

pip install django

3.Run the Development Server
To start the development server, navigate to the project directory and run:

python manage.py runserver

4.You can now access the project by opening your browser and going to:

http://127.0.0.1:8000/

Usage
To log in or register, visit the login and registration pages provided in the application.
After successful login, users can access restricted areas like events, booking, etc.
Logout functionality is available via the navigation bar.
Contributing
Feel free to fork the repository and contribute. If you encounter any issues, please open an issue, and I’ll address it as soon as possible

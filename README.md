# Event Management App

![homepage](https://github.com/user-attachments/assets/59af9378-1855-40ee-819b-df4ef4e4163c)


# Python Django Final Project

This is a Django project developed for my Varsity Course. This Event Management System is a web-based application built using Django, designed to facilitate seamless event booking for students. The system provides an authentication mechanism, allowing users to register, log in, and log out securely.

## Features

- User Authentication: Secure registration, login, and logout functionality.
- Event Booking: Students can browse and book available events.
- Backend Management: Event data and user bookings are stored and managed using Django’s database models.
- Dynamic Content Management
- User-friendly interface built with HTML, CSS, and Bootstrap
  


## Setup Instructions

To set up and run the application in local server, follow the steps below:

1. Clone the repository:
   ```sh
   git clone https://github.com/shafiqulsazu/djangoproject
   ```
2. Navigate to the project directory:
   ```sh
   cd eventproject
   ```
3. Create a virtual environment:
   ```sh
   python -m venv emv1
   ```
4. Activate the virtual environment:
   - On Windows:
     ```sh
     .\emv1\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source emv1/bin/activate
     ```
5. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
6. If any requirements needed:
   ```sh
   pip install requirements
   ```
6. If any migration required:
   ```sh
   python manage.py makemigrations
   ```
6. Run migrations:
   ```sh
   python manage.py migrate
   ```
7. Run the Django project:
   ```sh
   python manage.py runserver
   ```
8. Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```


Usage
To log in or register, visit the login and registration pages provided in the application.
After successful login, users can access restricted areas like events, booking, etc.
Logout functionality is available via the navigation bar.
Contributing
Feel free to fork the repository and contribute. If you encounter any issues, please open an issue, and I’ll address it as soon as possible

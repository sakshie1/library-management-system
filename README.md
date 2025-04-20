# library-management-system

Technologies Used
   Django version:4.2
   Django REST Framework
   MySQL Database

1.create virtual environment
   >py -3 -m vene .venv
2.activate virtual environment
  >.venv\scripts\activate
3.create project
  >django-admin startproject Library_management
4.cd Library_management
5.create app
6. Configure settings.py
   >Add 'rest_framework', and 'app' in INSTALLED_APPS.
7.apply migrations
   >python manage.py makemigrations
   >python manage.py migrate
8.python manage.py runserver


*******API Endpoints*********
/api/admin/signup/	            Create a new admin account
/api/admin/login/	                  Login with admin credentials
/api/books/	                  Add a new book (admin only)
/api/books/<id>/	              Update a book (admin only)
/api/books/<id>/	          Delete a book (admin only)
/api/student/books/	            Public list of all books (for students)

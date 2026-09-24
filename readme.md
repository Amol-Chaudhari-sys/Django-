# Django Fast Revision Notes 🚀

> Simple Django notes for quick revision before interviews, practicals, or exams.

---

## 📌 1. Django Basics

**Django** is a Python web framework.

### MVT

```text
Model    → Database
View     → Logic
Template → UI / HTML
```

### Create Project

```bash
django-admin startproject projectname
```

### Create App

```bash
python manage.py startapp appname
```

### Run Server

```bash
python manage.py runserver
```

Custom port:

```bash
python manage.py runserver 0.0.0.0:5000
```

### Add App

In `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'appname',
]
```

---

# 📁 2. Django Project Structure

| File          | Use                     |
| ------------- | ----------------------- |
| `manage.py`   | Run Django commands     |
| `settings.py` | Project settings        |
| `urls.py`     | URL routing             |
| `models.py`   | Database models         |
| `views.py`    | Application logic       |
| `admin.py`    | Admin panel             |
| `apps.py`     | App configuration       |
| `wsgi.py`     | WSGI deployment         |
| `asgi.py`     | ASGI / async deployment |

---

# 🔗 3. URL Routing

Basic flow:

```text
Browser
   ↓
urls.py
   ↓
views.py
   ↓
Template / Database
```

### Render

```python
return render(request, 'login_page.html')
```

### Redirect

```python
return redirect('/recipes/')
```

### Named URL

```html
<a href="{% url 'see-marks' student.studentid %}">
    See Marks
</a>
```

---

# 🎨 4. Django Templates

Django Template Engine helps keep HTML reusable.

### `base.html`

```html
{% block content %}
{% endblock %}
```

### Child Template

```html
{% extends "base.html" %}

{% block content %}
<h1>Hello Django</h1>
{% endblock %}
```

### Important Syntax

```html
{{ variable }}
```

Display variable.

```html
{% if condition %}
{% endif %}
```

Condition.

```html
{% for item in items %}
{% endfor %}
```

Loop.

### DRY

**DRY = Don't Repeat Yourself**

---

# 🗄️ 5. Models

Models define the database structure.

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
```

### Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Flow

```text
models.py
   ↓
makemigrations
   ↓
Migration Files
   ↓
migrate
   ↓
Database
```

---

# 🐚 6. Django Shell

Open shell:

```bash
python manage.py shell
```

Create object:

```python
student = Student(
    name="Amol",
    age=20,
    email="amol@gmail.com"
)

student.save()
```

Shortcut:

```python
Student.objects.create(
    name="Amol",
    age=20,
    email="amol@gmail.com"
)
```

---

# 🔄 7. CRUD Operations

## Create

```python
car = Car(
    car_name="Honda City",
    speed=100
)

car.save()
```

Or:

```python
Car.objects.create(
    car_name="BMW",
    speed=350
)
```

## Read

```python
Car.objects.all()
```

```python
Car.objects.get(id=1)
```

⚠️ `get()` raises an error if object doesn't exist.

```python
Car.objects.filter(id=1)
```

`filter()` can return an empty QuerySet.

## Update

```python
car = Car.objects.get(id=4)

car.car_name = "Audi"
car.speed = 200

car.save()
```

## Delete

```python
Car.objects.get(id=4).delete()
```

Delete all:

```python
Car.objects.all().delete()
```

---

# 📝 8. Forms & File Upload

### CSRF

```html
{% csrf_token %}
```

Use this in POST forms.

### File Upload

```html
<form method="POST" enctype="multipart/form-data">
```

`multipart/form-data` is required for file uploads.

---

# 🖼️ 9. Static & Media Files

### Static

Used for:

* CSS
* JavaScript
* Fixed assets

```python
STATIC_URL = '/static/'
```

### Media

Used for:

* User images
* Uploaded files
* Documents

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Remember

```text
STATIC → Developer files
MEDIA  → User uploaded files
```

---

# 🔍 10. Search

Usually use `GET` for search.

```python
if request.GET.get("search"):
    recipes = recipes.filter(
        recipe_name__icontains=request.GET.get("search")
    )
```

### `icontains`

Case-insensitive search.

---

# 🔐 11. Authentication

Import:

```python
from django.contrib.auth import authenticate, login, logout
```

### Authenticate

```python
user = authenticate(
    username=username,
    password=password
)
```

### Login

```python
login(request, user)
```

### Logout

```python
logout(request)
```

### Protect View

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    ...
```

---

# 💬 12. Django Messages

```python
from django.contrib import messages
```

Examples:

```python
messages.success(request, "Success!")
messages.info(request, "Information")
messages.warning(request, "Warning")
messages.error(request, "Invalid password")
```

Template:

```html
{% if messages %}

    {% for message in messages %}
        <h3>{{ message }}</h3>
    {% endfor %}

{% endif %}
```

---

# 🧠 13. ORM

**ORM = Object Relational Mapper**

Allows Python code to interact with the database.

```python
Model.objects.all()
Model.objects.get()
Model.objects.filter()
Model.objects.create()
```

### Ordering

Ascending:

```python
Model.objects.all().order_by("view_count")
```

Descending:

```python
Model.objects.all().order_by("-view_count")
```

---

# 🔎 14. Important ORM Lookups

| Lookup         | Meaning                   |
| -------------- | ------------------------- |
| `__icontains`  | Case-insensitive contains |
| `__contains`   | Contains                  |
| `__startswith` | Starts with               |
| `__endswith`   | Ends with                 |
| `__gte`        | Greater than or equal     |
| `__lte`        | Less than or equal        |
| `__in`         | Matches values in list    |

Example:

```python
Student.objects.filter(age__gte=20)
```

```python
Student.objects.filter(
    student_name__startswith="A"
)
```

---

# 🔗 15. ForeignKey Queries

Use `__` to access related fields.

```python
Student.objects.filter(
    department__department="Computer"
)
```

### Primary Key

```python
Student.pk
```

Default ID:

```python
Student.id
```

---

# 📦 16. `values()` & `values_list()`

### values()

Returns dictionaries:

```python
Student.objects.values()
```

### values_list()

Returns tuples:

```python
Student.objects.values_list(
    "id",
    "student_name"
)
```

---

# ❓ 17. Q Objects

Used for complex queries.

```python
from django.db.models import Q
```

### OR

```python
Student.objects.filter(
    Q(student_name__icontains=search) |
    Q(student_email__icontains=search)
)
```

Useful for:

```text
AND
OR
NOT
```

---

# 📊 18. Aggregate

Used for summary calculations.

Import:

```python
from django.db.models import (
    Sum, Avg, Min, Max, Count
)
```

### Functions

```text
Sum   → Total
Avg   → Average
Min   → Minimum
Max   → Maximum
Count → Number of records
```

Example:

```python
Student.objects.aggregate(
    Avg("student_age")
)
```

```python
Student.objects.aggregate(
    total=Sum("marks")
)
```

---

# 📈 19. Annotate

`annotate()` adds calculated information to QuerySet results.

```python
Student.objects.values(
    "department__department"
).annotate(
    Count("id")
)
```

### Aggregate vs Annotate

```text
aggregate → overall summary
annotate  → calculated value for each/group
```

---

# 🛠️ 20. Django Admin

Open:

```text
http://127.0.0.1:8000/admin/
```

Create admin:

```bash
python manage.py createsuperuser
```

Register model:

```python
admin.site.register(Recipe)
```

### Custom Admin

```python
class SubjectListAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "subject",
        "marks"
    )
```

Useful options:

```text
list_display
ordering
search_fields
list_filter
```

---

# 📄 21. Pagination

Import:

```python
from django.core.paginator import Paginator
```

Example:

```python
paginator = Paginator(queryset, 20)

page_no = request.GET.get("page", 1)

page_obj = paginator.get_page(page_no)
```

Important:

```text
page_obj.number
→ Current page

page_obj.paginator.num_pages
→ Total pages

page_obj.previous_page_number()
→ Previous page

page_obj.next_page_number()
→ Next page
```

---

# 🔗 22. URL Parameters

URL:

```python
path(
    "see-marks/<int:student_id>/",
    views.see_marks,
    name="see-marks"
)
```

View:

```python
def see_marks(request, student_id):
    ...
```

Template:

```html
{% url "see-marks" student.studentid %}
```

---

# 🧾 23. Report Card

Example:

```python
SubjectMarks.objects.filter(
    student=obj.student
).aggregate(
    marks=Sum("marks")
)
```

### Unique Combination

```python
class Meta:
    unique_together = ["student", "subject"]
```

Prevents duplicate student + subject combinations.

---

# 👤 24. Custom User Model

Import:

```python
from django.contrib.auth.models import AbstractUser
```

Example:

```python
class CustomUser(AbstractUser):

    USERNAME_FIELD = "phone_number"

    REQUIRED_FIELDS = []

    objects = UserManager()
```

### Settings

```python
AUTH_USER_MODEL = "accounts.CustomUser"
```

---

# 👨‍💼 25. Custom User Manager

Import:

```python
from django.contrib.auth.models import BaseUserManager
```

Main functions:

```text
create_user()
create_superuser()
```

Example:

```python
class UserManager(BaseUserManager):

    def create_user(
        self,
        phone_number,
        password=None,
        **extra_fields
    ):
        ...
```

Superuser should have:

```python
is_staff = True
is_superuser = True
is_active = True
```

---

# 🗑️ 26. Custom Model Manager / Soft Delete

Example:

```python
class StudentsManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(
            is_deleted=False
        )
```

Model:

```python
is_deleted = models.BooleanField(default=False)

objects = StudentsManager()
admin_objects = models.Manager()
```

### Idea

```text
objects
   ↓
non-deleted records

admin_objects
   ↓
all records
```

---

# 📧 27. Sending Email

```python
from django.core.mail import send_mail
```

```python
send_mail(
    subject,
    message,
    from_email,
    recipient_list
)
```

### SMTP Settings

```python
EMAIL_BACKEND = (
    "django.core.mail.backends.smtp.EmailBackend"
)

EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
```

---

# 📎 28. Email With Attachment

```python
from django.core.mail import EmailMessage
```

```python
mail = EmailMessage(
    subject=subject,
    body=message,
    from_email=settings.EMAIL_HOST_USER,
    to=recipient_list
)

mail.attach_file(file_path)
mail.send()
```

---

# 📡 29. Django Signals

Signals allow Django to react to events.

### Important Signals

```text
pre_save
post_save
pre_delete
post_delete
```

### Example

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Car)
def call_car_api(sender, instance, **kwargs):
    print("Car object saved")
```

### Flow

```text
Model Event
    ↓
Signal
    ↓
Receiver Function
    ↓
Action
```

---

# 🧩 30. Abstract Models

Useful for common fields shared by multiple models.

```python
class BaseModel(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True
```

### Important

```text
abstract = True
        ↓
No separate database table
        ↓
Child models inherit fields
```

---

# 🛠️ 31. `utils.py`

Use `utils.py` for reusable helper functions.

Examples:

```text
Email functions
Helper functions
Reusable application logic
```

---

# ⚡ QUICK COMMAND REVISION

```bash
# Create project
django-admin startproject project

# Create app
python manage.py startapp app

# Run server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Django shell
python manage.py shell

# Create admin
python manage.py createsuperuser
```

---

# 🧠 QUICK ORM REVISION

```python
Model.objects.all()

Model.objects.get(id=1)

Model.objects.filter(id=1)

Model.objects.create(...)

Model.objects.filter(
    name__icontains="amol"
)

Model.objects.order_by("name")

Model.objects.order_by("-name")

Model.objects.values()

Model.objects.values_list("id", "name")

Model.objects.aggregate(
    Sum("marks")
)
```

---

# 🔥 FINAL 5-MINUTE REVISION

```text
Django
  ↓
MVT
  ↓
Project + App
  ↓
URLs
  ↓
Views
  ↓
Templates
  ↓
Models
  ↓
Migrations
  ↓
CRUD
  ↓
ORM
  ↓
ForeignKey
  ↓
Q Objects
  ↓
Aggregate / Annotate
  ↓
Admin
  ↓
Authentication
  ↓
Custom User
  ↓
Static / Media
  ↓
Search
  ↓
Pagination
  ↓
Email
  ↓
Signals
  ↓
Custom Manager
  ↓
Abstract Model
```

## ⭐ Remember These

```text
makemigrations → Create migration files
migrate        → Apply migrations

get()          → One object / error if not found
filter()       → QuerySet / can be empty
create()       → Create + save

__icontains    → Search
__gte          → >=
__lte          → <=
__in           → List matching

aggregate()    → Overall calculation
annotate()     → Calculation per result/group

authenticate() → Check user
login()        → Login
logout()       → Logout

STATIC         → Project static files
MEDIA          → User uploads

Signal         → React to model events
Manager        → Custom QuerySet behavior
Abstract       → Reusable model without own table
```

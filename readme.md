# Web Courses

## Description

App for mentoring and learning. Different users groups with different permissions and roles: instructors and students.
Instructors can add four types of content.

## How to run
1. You have to have `docker` and `docker-compose` installed on your computer.
2. Run command `docker-compose up --build`.
3. Prepare migrations `docker-compose exec backend python manage.py makemigratins courses users`.
4. Migrate `docker-compose exec backend python manage.py migrate`.
5. Create groups 
```bash
   docker-compose exec backend python manage.py shell
   ```
```
    from django.contrib.auth.models import Group
    Group.objects.create(name='student')
    Group.objects.create(name='instructor')
```

🐳 Getting Started with Docker
🔧 1. Build and Start Containers
bash
Copy
Edit
docker-compose up --build
✅ 2. Run Migrations
bash
Copy
Edit
docker-compose exec web python manage.py migrate
👤 3. Create a Superuser
bash
Copy
Edit
docker-compose exec web python manage.py createsuperuser
🌐 4. Access the App
App: http://localhost:8000

Admin: http://localhost:8000/admin

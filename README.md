Quora - Q&A Platform

Core Functionality
1. User registration and authentication
2. Secure login/logout system
3. Question posting and management
4. Answering questions
5. Like/unlike answers

git clone https://github.com/subal75/quora.git

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

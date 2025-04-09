# Quora - Q&A Platform

## Core Functionality

1. User registration and authentication
2. Secure login/logout system
3. Question posting and management
4. Answering questions
5. Like/unlike answers

## Quick Installation Guide

```bash
git clone https://github.com/subal75/quora.git
cd quora

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies and setup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

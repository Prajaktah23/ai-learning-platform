🚀 AI Learning Platform

An AI-powered personalized learning platform that generates customized learning roadmaps, tracks user progress, and automatically creates assessments using Large Language Models (LLMs).

The platform leverages FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and Ollama (Llama 3) to deliver adaptive learning experiences tailored to individual learning goals.

📌 Overview

Traditional online learning platforms provide static courses that may not align with every learner's objectives, skill levels, or available study time.

The AI Learning Platform solves this challenge by generating:

Personalized learning paths
Topic-wise learning schedules
AI-generated quizzes
Progress tracking and analytics
Secure user authentication

Using Generative AI, the system dynamically creates structured learning roadmaps based on user goals, experience level, and study availability.

✨ Key Features
🔐 Authentication & Authorization
User Registration
Secure Login
JWT Token Authentication
Protected API Endpoints
User-specific Learning Data
🤖 AI-Powered Learning Path Generation

Generate personalized learning plans based on:

Learning Goal (Python, AI, Data Science, etc.)
Experience Level
Beginner
Intermediate
Advanced
Study Hours Per Day
Learning Duration
Start Date

The platform uses Llama 3 via Ollama to create structured learning roadmaps.

📚 Intelligent Learning Structure

Generated learning paths contain:

Learning Plans
Topics
Subtopics
Weekly Progression
Structured Study Timeline

Example:

Python Programming
│
├── Basics
│   ├── Variables
│   ├── Data Types
│   └── Operators
│
├── Functions
│
├── OOP
│
└── Projects
📝 AI-Generated Quizzes

The system automatically generates:

Subtopic Quizzes
5 MCQs
Personalized per learner
Topic Quizzes
10 MCQs
Comprehensive topic assessment

Quiz generation is handled dynamically using LLM prompts.

📊 Learning Progress Tracking

Track:

Learning Progress
Completed Topics
Quiz Scores
Learning Performance
Assessment History

Dashboard APIs provide insights into learner performance.

🏗️ System Architecture
Frontend
    │
    ▼
FastAPI Backend
    │
    ├── Authentication Module
    ├── Learning Path Engine
    ├── Quiz Engine
    ├── Tracking Service
    │
    ▼
Ollama (Llama 3)
    │
    ▼
PostgreSQL Database
🛠️ Technology Stack
Backend
FastAPI
Python
SQLAlchemy
Pydantic
Uvicorn
Database
PostgreSQL
AsyncPG
Psycopg2
AI/LLM
Ollama
Llama 3
Transformers
Torch
Accelerate
Security
JWT Authentication
Passlib
Bcrypt
Python-JOSE
Deployment
Docker
Docker Compose
📂 Project Structure
ai-learning-platform/
│
├── app/
│   ├── api/
│   │   ├── auth.py
│   │   ├── learning_path.py
│   │   ├── quiz.py
│   │   └── tracking.py
│   │
│   ├── core/
│   │   ├── auth.py
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── session.py
│   │
│   ├── llm/
│   │   ├── learning_path_prompt.py
│   │   └── llm_provider.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── learning_plan.py
│   │   ├── topic.py
│   │   ├── subtopic.py
│   │   ├── quiz.py
│   │   └── quiz_result.py
│   │
│   ├── schemas/
│   └── services/
│
├── requirements.txt
├── docker-compose.yml
└── README.md
⚙️ Installation
1. Clone Repository
git clone https://github.com/your-username/ai-learning-platform.git

cd ai-learning-platform
2. Create Virtual Environment
python -m venv venv

Activate:

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Setup PostgreSQL

Create a PostgreSQL database:

CREATE DATABASE ai_learning_platform;

Update database configuration inside:

app/config.py
5. Install Ollama

Download:

https://ollama.com

Pull Llama 3:

ollama pull llama3

Verify:

ollama run llama3
6. Run Application
uvicorn app.main:app --reload

Application:

http://localhost:8000

Swagger Documentation:

http://localhost:8000/docs
🔑 API Endpoints
Authentication
Method	Endpoint
POST	/auth/register
POST	/auth/login
POST	/auth/logout
Learning Path
Method	Endpoint
POST	/generate-learning-path

Parameters:

goal
level
hours_per_day
duration_weeks
start_date
Quiz
Method	Endpoint
GET	/quiz/{quiz_id}
POST	/quiz/{quiz_id}/submit
GET	/quiz/dashboard/{email}
🔒 Security Features
JWT Token Authentication
Password Hashing with Bcrypt
Protected Routes
User Ownership Validation
Secure Database Access
📈 Future Enhancements
AI Mentor Chatbot
RAG-based Learning Assistant
Learning Recommendations Engine
Adaptive Difficulty Quizzes
Gamification & Leaderboards
Video Course Integration
Progress Visualization Dashboard
Multi-LLM Support (GPT, Gemini, Claude, Llama)
🎯 Use Cases
Personalized Skill Development
Corporate Learning Programs
University Learning Platforms
Coding Bootcamps
Employee Upskilling
AI-Based EdTech Solutions
👨‍💻 Author

Prajakta Hake

Associate Software Engineer | AI & Generative AI Developer

Skills:

Python
FastAPI
Generative AI
LLMs
LangChain
LangGraph
SQL
PostgreSQL
Docker
Machine Learning
Deep Learning
📜 License

This project is licensed under the MIT License.

⭐ If you found this project useful, consider giving it a star and contributing to its future development.
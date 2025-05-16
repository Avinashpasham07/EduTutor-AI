EduTutor AI - Personalized Learning & Assessment System
EduTutor AI is an innovative platform designed to enhance the learning experience for students by providing personalized learning paths, quizzes, flashcards, and AI-driven content generation. It uses machine learning and AI technologies to provide real-time feedback and suggestions for improvement, making it a comprehensive tool for students and educators alike.

Tech Stack
Frontend: Streamlit (for easy deployment of interactive web apps)
Backend: Flask (for handling requests and API integration)
Machine Learning: OpenRouter's Mixtral Model via LangChain (for AI-based content and personalized responses)
Other Technologies: Python,HTML, CSS, JavaScript

Installation
To set up the project locally, follow these steps:

1.Clone the repository:
git clone https://github.com/Avinashpasham07/EduTutor-AI.git

2.Navigate into the project directory:
cd EduTutor-AI
3.Set up a virtual environment:
python -m venv venv

4.Activate the virtual environment:

On Windows:
.\venv\Scripts\activate

On MacOS/Linux:
source venv/bin/activate

5.Create a .env File:

In the .env file, add the following content:
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENROUTER_MODEL=mistralai/mixtral-8x7b

6.Install the required dependencies:
pip install -r requirements.txt

7.Run the app:
streamlit run app.py

Acknowledgments
OpenRouter for providing AI models.
Streamlit for creating an interactive front-end.
Flask for building a lightweight backend API.



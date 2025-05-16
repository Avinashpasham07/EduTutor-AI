# EduTutor AI - Personalized Learning & Assessment System

EduTutor AI is an innovative platform designed to enhance the learning experience for students by providing personalized learning paths, quizzes, flashcards, and AI-driven content generation. It uses machine learning and AI technologies to provide real-time feedback and suggestions for improvement, making it a comprehensive tool for students and educators alike.

## Tech Stack

- **Frontend**: Streamlit (for easy deployment of interactive web apps)
- **Backend**: Flask (for handling requests and API integration)
- **Machine Learning**: OpenRouter's Mixtral Model via LangChain (for AI-based content and personalized responses)
- **Other Technologies**: Python, HTML, CSS, JavaScript

## Installation

To set up the project locally, follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/Avinashpasham07/EduTutor-AI.git
````

### 2. Navigate into the project directory:

```bash
cd EduTutor-AI
```

### 3. Set up a virtual environment:

```bash
python -m venv venv
```

### 4. Activate the virtual environment:

#### On Windows:

```bash
.\venv\Scripts\activate
```

#### On MacOS/Linux:

```bash
source venv/bin/activate
```

### 5. Create a `.env` File:

In the `.env` file, add the following content:

```
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENROUTER_MODEL=mistralai/mixtral-8x7b
```

**Important:** Replace `your_openai_api_key` with your actual OpenAI API key.

### 6. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 7. Run the app:

```bash
streamlit run app.py
```
## Outputs
---
![Image](https://github.com/user-attachments/assets/bdd8af3d-84c9-4f25-a033-a106e277f8e6)

![Image](https://github.com/user-attachments/assets/8120283f-7126-45a0-9da9-a2658c5077a7)

![Image](https://github.com/user-attachments/assets/9a28283c-5543-4bbd-a8ca-d4bb540ee60c)

![Image](https://github.com/user-attachments/assets/112c0035-20ad-4461-a3dd-2cd15dfb8d3d)

![Image](https://github.com/user-attachments/assets/a59243fc-b962-4661-9372-ac050961cc2f)

![Image](https://github.com/user-attachments/assets/e73b2236-ef35-4754-b565-4aaf0f94cf5f)

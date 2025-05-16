import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import requests
from streamlit_option_menu import option_menu

# Load .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
API_BASE = os.getenv("OPENAI_API_BASE")

# Initialize LLM
llm = ChatOpenAI(
    model="mistralai/mixtral-8x7b-instruct",
    temperature=0.7,
    openai_api_key=API_KEY,
    openai_api_base=API_BASE
)

# Function to load lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ai = load_lottieurl("https://lottie.host/4d266ee4-2d6f-4c86-83a9-4fd050c61bc5/qwJ6zNUzBc.json")

# ---------- Content Generation Functions ----------
def generate_lesson(topic, detail_level="Basic", difficulty="Intermediate", learning_style=["Visual"]):
    prompt_template = PromptTemplate(
        input_variables=["topic", "detail_level", "difficulty", "learning_style"],
        template="""Create a {detail_level} lesson about {topic} for a {difficulty} level student who prefers {learning_style} learning style. 
Include:
1. Learning Objectives
2. Main content with examples
3. Key takeaways
4. Practice activities
Use markdown for formatting with headings, bullet points, and bold text for emphasis."""
    )
    prompt = prompt_template.format(
        topic=topic,
        detail_level=detail_level,
        difficulty=difficulty,
        learning_style=", ".join(learning_style)
    )
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"

def generate_quiz(topic, difficulty="Intermediate"):
    prompt_template = PromptTemplate(
        input_variables=["topic", "difficulty"],
        template="""Create a 5-question multiple choice quiz about {topic} for {difficulty} students.
Format each question clearly with:
- Question stem
- Options labeled A-D
- Correct answer marked with (Correct)
- Brief explanation for each answer
Use markdown formatting with ### for question headings and > for explanations."""
    )
    prompt = prompt_template.format(topic=topic, difficulty=difficulty)
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"

def generate_flashcards(topic, count=5):
    prompt_template = PromptTemplate(
        input_variables=["topic", "count"],
        template="""Create {count} high-quality flashcards for {topic}.
Format each card as:
**Front:** [Question/Term]  
**Back:** [Answer/Definition] (1-2 sentences max)

Separate each flashcard with ---
Ensure concepts are clear and suitable for students."""
    )
    prompt = prompt_template.format(topic=topic, count=count)
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"

# ---------- UI Configuration ----------
st.set_page_config(
    page_title="EduTutor AI", 
    layout="wide",
    page_icon="🧠",
    initial_sidebar_state="collapsed"
)

# Responsive CSS with media queries
st.markdown("""
<style>
html, body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f0f4f8;
    margin: 0;
    padding: 0;
}

.main-title {
    font-size: 50px;
    font-weight: bold;
    background: linear-gradient(90deg, #1d8cf8, #f96332);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    animation: fadeIn 1s ease-in;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555;
    margin-bottom: 30px;
    animation: fadeInUp 1.5s ease-in-out;
}

.stButton>button {
    background: linear-gradient(to right, #ff416c, #ff4b2b);
    color: white;
    font-size: 18px;
    padding: 10px 24px;
    border-radius: 12px;
    border: none;
    transition: all 0.4s ease-in-out;
    box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(255, 75, 75, 0.4);
        color: white;
    
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    transition: transform 0.3s ease;
    border-left: 4px solid #4B8BBE;
}

.card:hover {
    transform: translateY(-5px);
}

.flashcard {
    perspective: 1000px;
    margin-bottom: 20px;
}

.flashcard-inner {
    position: relative;
    width: 100%;
    height: 150px;
    transition: transform 0.8s;
    transform-style: preserve-3d;
}

.flashcard:hover .flashcard-inner {
    transform: rotateY(180deg);
}

.flashcard-front, .flashcard-back {
    position: absolute;
    width: 100%;
    height: 100%;
    padding: 15px;
    backface-visibility: hidden;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.flashcard-front {
    background: #ffffff;
    border: 1px solid #4B8BBE;
}

.flashcard-back {
    background: #1d8cf8;
    color: white;
    transform: rotateY(180deg);
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .main-title {
        font-size: 36px;
    }
    
    .subtitle {
        font-size: 16px;
    }
    
    .stButton>button {
        font-size: 16px;
        padding: 8px 16px;
    }
    
    .card {
        padding: 15px;
    }
    
    .flashcard-inner {
        height: 120px;
    }
}

@media (max-width: 480px) {
    .main-title {
        font-size: 28px;
    }
    
    .stButton>button {
        width: 100%;
    }
    
    .flashcard-inner {
        height: 100px;
    }
}

/* Animation keyframes */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes fadeInUp {
    from { 
        opacity: 0;
        transform: translateY(20px);
    }
    to { 
        opacity: 1;
        transform: translateY(0);
    }
}

/* Custom container for better spacing */
.custom-container {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

/* Form styling */
.stTextInput>div>div>input, 
.stTextArea>div>div>textarea,
.stSelectbox>div>div>select {
    border-radius: 8px !important;
    border: 1px solid #ddd !important;
    padding: 10px !important;
}

.stTextInput>div>div>input:focus, 
.stTextArea>div>div>textarea:focus,
.stSelectbox>div>div>select:focus {
    border-color: #4B8BBE !important;
    box-shadow: 0 0 0 2px rgba(75, 139, 190, 0.2) !important;
}

/* Custom divider */
.custom-divider {
    height: 1px;
    background: linear-gradient(to right, transparent, #4B8BBE, transparent);
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# Get the current query parameters
query_params = st.query_params
initial_tab = query_params.get("tab", ["Home"])[0]

# Map tab names to indices
tab_mapping = {
    "Home": 0,
    "Generate Lesson": 1,
    "Quiz": 2,
    "Flashcards": 3,
    "Ask AI": 4
}

# Set the default index based on the query parameter
default_index = tab_mapping.get(initial_tab, 0)

with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Home", "Generate Lesson", "Quiz", "Flashcards", "Ask AI"],
        icons=["house", "book", "question-square", "card-checklist", "chat"],
        default_index=default_index,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0!important", 
                "background-color": "#ffffff",
                "box-shadow": "0 2px 10px rgba(0,0,0,0.1)"
            },
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "color": "#333",
            },
            "nav-link-selected": {
                "background-color": "#4B8BBE",
                "font-weight": "500"
            },
             "icon": {"color": "black", "font-size": "18px"}, 
            "icon-selected": {
                "color": "#ffffff"
            },
        }
    )

# Function to update the query parameter
def update_query_param(tab_name):
    st.query_params["tab"] = tab_name
    st.rerun()

# ---------- Page Content ----------
if selected == "Home":
    # Hero Section
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
            <div class="custom-container">
                <h1 style='color: #4B8BBE; font-size: 48px; line-height: 1.2;'>
                    Smart Learning with <span style='color:#FF4B4B;'>EduTutor AI</span>
                </h1>
                <p style="font-size: 18px; color: white; margin-bottom: 30px;">
                    Your personal AI-powered education assistant that adapts to your learning style.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Start Learning Now →", key="start_learning_button"):
            update_query_param("Generate Lesson")
    
    with col2:
        if lottie_ai:
            st.components.v1.html("""
                <div style="text-align: center;">
                    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
                    <lottie-player
                        src="https://lottie.host/4d266ee4-2d6f-4c86-83a9-4fd050c61bc5/qwJ6zNUzBc.json"
                        background="transparent"
                        speed="1"
                        style="width: 100%; height: 300px;"
                        loop
                        autoplay>
                    </lottie-player>
                </div>
            """, height=300)
    
    # Features Section
    st.markdown("""
        <div class="custom-container" style="margin-top: 50px;">
            <h2 style='color: #4B8BBE; text-align: center; margin-bottom: 30px;'>✨ Key Features</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
                <div class="card">
                    <h3 style='color: #333;'>📚 Personalized Lessons</h3>
                    <p style='color: #555;'>AI-generated lessons tailored to your learning style and level.</p>
                </div>
                <div class="card">
                    <h3 style='color: #333;'>🔖 Smart Flashcards</h3>
                    <p style='color: #555;'>Create and study flashcards for efficient memorization.</p>
                </div>
                <div class="card">
                    <h3 style='color: #333;'>📝 Interactive Quizzes</h3>
                    <p style='color: #555;'>Test your knowledge with AI-generated assessments.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif selected == "Generate Lesson":
    st.markdown("""
        <div class="custom-container">
            <h1 style='color: #4B8BBE;'>Generate Custom <span style='color:#FF4B4B;'>Lessons</span>
                </h1></h1>
            <p style="color: #555;">Create personalized learning materials tailored to your needs.</p>
            <div class="custom-divider"></div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("lesson_form"):
        col1, col2 = st.columns(2)
        with col1:
            topic = st.text_input("What topic would you like to learn?", placeholder="Enter a topic (e.g., Quantum Physics)")
            detail_level = st.selectbox("Detail Level", 
                                      ["Overview", "Basic", "Detailed", "Comprehensive"],
                                      help="How in-depth should the lesson be?")
        with col2:
            difficulty = st.selectbox("Difficulty Level", 
                                    ["Beginner", "Intermediate", "Advanced"])
            learning_style = st.multiselect("Preferred Learning Style(s)", 
                                          ["Visual", "Auditory", "Reading/Writing", "Kinesthetic"],
                                          default=["Visual"])
        
        submitted = st.form_submit_button("Generate Lesson", type="primary")
    
    if submitted:
        if topic:
            with st.spinner("Creating your personalized lesson..."):
                lesson = generate_lesson(topic, detail_level, difficulty, learning_style)
                st.markdown("---")
                st.markdown("### Your Custom Lesson")
                st.markdown(lesson, unsafe_allow_html=True)
                
                # Add download button
                st.download_button(
                    label="Download Lesson",
                    data=lesson,
                    file_name=f"{topic}_lesson.md",
                    mime="text/markdown"
                )
        else:
            st.warning("Please enter a topic to generate a lesson.")

elif selected == "Quiz":
    st.markdown("""
        <div class="custom-container">
            <h1 style='color: #4B8BBE;'>Generate <span style='color:#FF4B4B;'>Quiz</span></h1>
            <p style="color: #555;">Test your knowledge with AI-generated questions.</p>
            <div class="custom-divider"></div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("quiz_form"):
        topic = st.text_input("Quiz Topic", placeholder="Enter a topic (e.g., World War II)")
        difficulty = st.selectbox("Difficulty Level", 
                                 ["Beginner", "Intermediate", "Advanced"])
        
        submitted = st.form_submit_button("Generate Quiz", type="primary")
    
    if submitted:
        if topic:
            with st.spinner("Creating your quiz..."):
                quiz = generate_quiz(topic, difficulty)
                st.markdown("---")
                st.markdown("### Your Quiz")
                st.markdown(quiz, unsafe_allow_html=True)
                
                # Add download button
                st.download_button(
                    label="Download Quiz",
                    data=quiz,
                    file_name=f"{topic}_quiz.md",
                    mime="text/markdown"
                )
        else:
            st.warning("Please enter a topic to generate a quiz.")

elif selected == "Flashcards":
    st.markdown("""
        <div class="custom-container">
            <h1 style='color: #4B8BBE;'> Generate <span style='color:#FF4B4B;'>Flash cards</span></h1>
            <p style="color: #555;">Create study cards for efficient learning.</p>
            <div class="custom-divider"></div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("flashcard_form"):
        topic = st.text_input("Flashcard Topic", placeholder="Enter a topic (e.g., French Vocabulary)")
        count = st.slider("Number of Flashcards", 3, 10, 5)
        
        submitted = st.form_submit_button("Generate Flashcards", type="primary")
    
    if submitted:
        if topic:
            with st.spinner("Creating your flashcards..."):
                flashcards = generate_flashcards(topic, count)
                st.markdown("---")
                st.markdown("### Your Flashcards")
                
                # Process flashcards for better display
                cards = [card.strip() for card in flashcards.split("---") if card.strip()]
                for i, card in enumerate(cards, 1):
                    # Extract front and back
                    parts = card.split("**Back:**")
                    front = parts[0].replace("**Front:**", "").strip()
                    back = parts[1].strip() if len(parts) > 1 else ""
                    
                    # Display as interactive card
                    st.markdown(f"""
                    <div class="flashcard">
                        <div class="flashcard-inner">
                            <div class="flashcard-front">
                                <div><strong>Front:</strong> {front}</div>
                            </div>
                            <div class="flashcard-back">
                                <div><strong>Back:</strong> {back}</div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Add download button
                st.download_button(
                    label="Download Flashcards",
                    data=flashcards,
                    file_name=f"{topic}_flashcards.md",
                    mime="text/markdown"
                )
        else:
            st.warning("Please enter a topic to generate flashcards.")

elif selected == "Ask AI":
    import fitz  # PyMuPDF
    from docx import Document

    def extract_text_from_file(file):
        if file.type == "application/pdf":
            text = ""
            pdf = fitz.open(stream=file.read(), filetype="pdf")
            for page in pdf:
                text += page.get_text()
            return text
        elif file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
            doc = Document(file)
            return "\n".join([para.text for para in doc.paragraphs])
        elif file.type == "text/plain":
            return file.read().decode("utf-8")
        else:
            return None

    st.markdown("""
        <div class="custom-container">
            <h1 style='color: #4B8BBE;'>Ask <span style='color:#FF4B4B;'>EduTutor AI</span></h1>
            <p style="color: #555;">Get answers to your educational questions or analyze uploaded documents.</p>
            <div class="custom-divider"></div>
        </div>
    """, unsafe_allow_html=True)
    
    file = st.file_uploader("Upload a file (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])
    file_text = ""
    if file:
        with st.spinner("Extracting file content..."):
            file_text = extract_text_from_file(file)
            if not file_text:
                st.error("Unsupported file type or empty file.")
            else:
                st.success("File content extracted successfully!")
                with st.expander("View extracted text"):
                    st.text(file_text[:1000] + "..." if len(file_text) > 1000 else file_text)

    query = st.text_area("Ask any educational question:", placeholder="Type your question here...", height=150)
    if st.button("Get Answer", type="primary"):
        if query.strip():
            with st.spinner("Thinking..."):
                try:
                    if file_text:
                        prompt = f"Based on the following content:\n\n{file_text}\n\nAnswer this question:\n{query}"
                    else:
                        prompt = query
                    response = llm.invoke(prompt)
                    st.markdown("### AI Response:")
                    st.markdown(response.content, unsafe_allow_html=True)
                    
                    # Add copy button
                    st.download_button(
                        label="Copy Answer",
                        data=response.content,
                        file_name="ai_response.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a question to get a response.")
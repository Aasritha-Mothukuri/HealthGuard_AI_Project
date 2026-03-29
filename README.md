# HealthGuard AI Chatbot (Local LLM)

A personalized health advisory chatbot built using a local Large Language Model (LLM) with Ollama and a Streamlit UI. This project demonstrates prompt engineering, personalization, and local AI deployment without using cloud APIs.

---

## Features

- Personalized responses using user name  
- Adaptive explanations based on user level (Beginner, Intermediate, Advanced)  
- Health advice with constraints (no diagnosis)  
- Real-time model performance tracking (response time, word count, speed, interactions)  
- Runs completely offline using Ollama  

---

## Tech Stack

- Python  
- Streamlit  
- Ollama  
- Mistral model  
- Requests  

---

## Setup Instructions

### 1. Install Ollama  
Download from: https://ollama.com  

### 2. Pull Model  
Run:
ollama pull mistral  

### 3. Install Dependencies  
Run:
pip install streamlit requests  

### 4. Run the Chatbot  
Run:
streamlit run chatbot.py  

---

## How It Works

1. User enters name and selects level  
2. Chat history is stored using session state  
3. User asks a health question  
4. Prompt is sent to Ollama (local model)  
5. AI generates:
   - Short explanation  
   - 2–3 tips  
   - Disclaimer  
6. Performance metrics are displayed  

---

## Prompt Engineering

### System Prompt
- Defines chatbot role  
- Adds constraints (no diagnosis, short response)  
- Adapts response based on user level  

### Techniques Used
- Role Prompting  
- Instruction Prompting  
- Constraint-Based Prompting  
- Context Injection  

---

## Personalization

- Uses user name in responses  
- Adjusts explanation based on level  
- Maintains conversation context  

---

## Model Performance

- Beginner → faster responses  
- Intermediate → balanced  
- Advanced → slower due to detailed reasoning  

Metrics shown:
- Response Time  
- Words Generated  
- Speed (words/sec)  
- Interaction Count  

---

## Limitations

- Slower than cloud models  
- Not medically certified  
- Depends on system performance  

---

## Future Improvements

- Add user memory (database)  
- Improve UI  
- Add health scoring system  
- Support multiple models  

---

## Disclaimer

This chatbot provides general health advice only.  
It does not diagnose or prescribe treatment.  
Consult a healthcare professional for medical concerns.  

---

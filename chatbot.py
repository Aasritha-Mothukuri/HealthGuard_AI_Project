import streamlit as st
import requests
import time

# ---------------------------
# SYSTEM PROMPT
# ---------------------------
SYSTEM_PROMPT = """
You are HealthGuard AI, a Personalized Health Assistant.

Rules:
- Address user by name
- Adapt explanation based on user knowledge level:
  Beginner → simple, no jargon
  Intermediate → moderate detail
  Advanced → technical explanation
- Keep responses under 120 words
- Do NOT diagnose diseases
- Give general advice only

Response format:
- Short explanation
- 2-3 tips
- Short disclaimer
"""

# ---------------------------
# OLLAMA API FUNCTION
# ---------------------------
def get_response(messages):
    start = time.time()

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "mistral",
            "messages": messages,
            "stream": False
        }
    )

    end = time.time()

    reply = response.json()["message"]["content"]

    latency = round(end - start, 2)
    words = len(reply.split())
    speed = round(words / latency, 2) if latency > 0 else 0

    return reply, latency, words, speed

# ---------------------------
# STREAMLIT UI
# ---------------------------
st.set_page_config(page_title="HealthGuard AI", layout="wide")

st.title("HealthGuard AI Chatbot (Ollama)")

# ---------------------------
# SESSION STATE
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

if "name" not in st.session_state:
    st.session_state.name = ""

if "level" not in st.session_state:
    st.session_state.level = ""

if "chat_count" not in st.session_state:
    st.session_state.chat_count = 0

# ---------------------------
# SIDEBAR - PERFORMANCE
# ---------------------------
st.sidebar.title("Model Performance")

if "latency" in st.session_state:
    st.sidebar.metric("Response Time (s)", st.session_state.latency)
    st.sidebar.metric("Words", st.session_state.words)
    st.sidebar.metric("Speed (words/sec)", st.session_state.speed)
    st.sidebar.metric("Interactions", st.session_state.chat_count)

    # 🔥 Intelligent explanation
    st.sidebar.markdown("### Performance Insight")

    if st.session_state.level == "Beginner":
        st.sidebar.write("Simpler responses → Faster performance")

    elif st.session_state.level == "Intermediate":
        st.sidebar.write("Balanced detail → Moderate response time")

    else:
        st.sidebar.write("Detailed explanations → Slower response")

    if st.session_state.latency > 2:
        st.sidebar.write("Higher latency due to longer AI reasoning")

else:
    st.sidebar.write("Start chatting to see metrics")

# ---------------------------
# USER SETUP (ONCE)
# ---------------------------
if st.session_state.name == "":
    name = st.text_input("Enter your name:")
    level = st.selectbox("Select your level:", ["Beginner", "Intermediate", "Advanced"])

    if name:
        st.session_state.name = name
        st.session_state.level = level

        st.success(f"Welcome {name} ({level})")
    st.stop()

# ---------------------------
# SHOW CHAT
# ---------------------------
for msg in st.session_state.messages[1:]:
    role = msg["role"]
    st.chat_message(role).write(msg["content"])

# ---------------------------
# USER INPUT
# ---------------------------
user_input = st.chat_input("Ask your health question...")

if user_input:
    user_msg = f"""
User: {st.session_state.name}
Level: {st.session_state.level}
Question: {user_input}
"""

    st.session_state.messages.append({"role": "user", "content": user_msg})
    st.chat_message("user").write(user_input)

    reply, latency, words, speed = get_response(st.session_state.messages)

    # Save metrics
    st.session_state.latency = latency
    st.session_state.words = words
    st.session_state.speed = speed
    st.session_state.chat_count += 1

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
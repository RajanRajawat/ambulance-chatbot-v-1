# Ambulance Chatbot API

An AI-powered chatbot service built using **FastAPI + LangChain + Google GenAI**, designed to assist users with ambulance-related queries, emergency guidance, and basic medical assistance.

This API is intended to be integrated into an Ambulance Booking System (e.g., .NET backend or frontend apps).

---

##  Features

*  Conversational chatbot with session-based memory
*  Suggests appropriate ambulance types (BLS, ALS, ICU, etc.)
*  Understands user situations and gives guidance
*  Provides basic medical assistance (non-critical advice only)
*  Maintains chat history using session IDs
*  Fast and lightweight API using FastAPI

---

##  Supported Use Cases

1. Get information about ambulance types
2. Get ambulance suggestions based on requirements (e.g., ventilator → ALS)
3. Describe emergency situation → receive guidance until ambulance arrives
4. Basic illness help (safe, limited suggestions only)

---

##  Tech Stack

* **Backend:** FastAPI
* **LLM:** Google Gemini (`gemini-2.5-flash`)
* **Framework:** LangChain
* **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
* **Database (optional):** MongoDB (for vector search & future persistence)

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/RajanRajawat/ambulance-chatbot-rahul.git
cd ambulance-chatbot-rahul
git checkout dev
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Mac/Linux
```

---

### 3. Install dependencies

```bash
pip install langchain langchain-core langchain-community
pip install langchain-google-genai langchain-huggingface langchain-mongodb
pip install pymongo sentence-transformers python-dotenv fastapi uvicorn
```

---

### 4. Setup environment variables

Create a `.env` file in root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

---

##  Running the Server

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://localhost:8000
```

---

##  API Endpoint

###  POST `/chat`

Used to interact with the chatbot.

---

###  Request Body

```json
{
  "message": "I need an ambulance with ventilator",
  "session_id": "user123"
}
```

---

###  Response

```json
{
  "status": "success",
  "response": "You should book an Advanced Life Support (ALS) ambulance as it provides ventilator support."
}
```

---

##  Session Handling

* `session_id` is used to maintain chat history
* Use the **same session_id** for continuous conversation
* Different session_id = new conversation

---

##  Important Notes

* This chatbot is **not a replacement for medical professionals**
* Only provides **basic guidance and ambulance suggestions**
* In serious cases, always call emergency services immediately

---

##  Integration Guide (for .NET Developer)

* Send HTTP POST request to `/chat`
* Use JSON body with `message` and `session_id`
* Parse `response` field from API response
* Maintain session_id per user for chat continuity

---

##  Project Structure

```
ambulance-chatbot-rahul/
│── main.py
│── models.py
│── db/
│── .env
│── requirements.txt
│── README.md
```

---

##  Future Improvements

* Persistent chat history (MongoDB / Redis)
* RAG-based knowledge retrieval
* Intent detection (auto booking trigger)
* Deployment (AWS / Railway)

---

##  dev

Developed by Rajan Rajawat

---

##  Contribution

Feel free to fork and improve this project!

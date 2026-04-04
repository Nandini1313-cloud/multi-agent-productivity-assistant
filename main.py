from fastapi import FastAPI
from langchain_google_vertexai import ChatVertexAI
from google.cloud import firestore
from datetime import datetime

# Initialize FastAPI with your new Project Name
app = FastAPI(
    title="Multi-Agent Productivity Assistant",
    description="AI System coordinating multiple agents for tasks, schedules, and data management."
)

# Initialize Google Cloud Services
db = firestore.Client()
llm = ChatVertexAI(model_name="gemini-1.5-flash")

# --- SUB-AGENT: CALENDAR & TASKS ---
def calendar_sub_agent(task_details: str):
    """
    Simulates an MCP-integrated sub-agent.
    In a real-world scenario, this would call the Google Calendar API.
    """
    return f"SUB-AGENT (Calendar): Successfully processed and scheduled: '{task_details}'"

# --- CORE LOGIC: PRIMARY AGENT ---
@app.post("/ask")
async def ask_agent(prompt: str):
    # 1. Coordination Logic (Primary Agent decides which tool/sub-agent to use)
    if any(word in prompt.lower() for word in ["schedule", "calendar", "meeting", "appointment"]):
        result = calendar_sub_agent(prompt)
        decision = "Coordinating Sub-Agents (Calendar Tool)"
    else:
        # Standard AI response for general information/notes
        ai_response = llm.invoke(prompt)
        result = ai_response.content
        decision = "Direct AI Response"

    # 2. Store Structured Data (Requirement: Database Integration)
    db.collection("agent_logs").add({
        "query": prompt,
        "response": result,
        "decision_path": decision,
        "timestamp": firestore.SERVER_TIMESTAMP
    })

    return {
        "primary_agent_decision": decision,
        "final_output": result
    }

# --- DATA RETRIEVAL: AGENT MEMORY ---
@app.get("/history")
async def get_history():
    """Requirement: Retrieve structured data from the database."""
    logs_ref = db.collection("agent_logs").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(10)
    docs = logs_ref.stream()
    
    history = []
    for doc in docs:
        data = doc.to_dict()
        # Convert timestamp to string for JSON compatibility
        if "timestamp" in data and data["timestamp"]:
            data["timestamp"] = data["timestamp"].isoformat()
        history.append(data)
        
    return {"agent_memory_history": history}

@app.get("/")
def root():
    return {"message": "Multi-Agent Productivity Assistant API is Online"}
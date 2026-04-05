🚀 Multi-Agent Productivity Assistant
A cloud-native AI orchestration system that uses a Manager-Worker architecture to coordinate specialized agents for task execution, scheduling, and persistent data management.

🔗 Live Demo & Verification
[👉 Click here to test the Live API](https://assistant-api-436405208006.us-central1.run.app/docs)

📖 Project Overview
This project implements an Agentic Workflow using Google Cloud Platform. It moves beyond standard chatbots by using a Primary Agent to interpret natural language and automatically delegate specialized tasks to Sub-Agents.

Every interaction is logged in a structured Firestore database, allowing the assistant to maintain a long-term "memory" of tasks and user requests.

Key Features:
Intelligent Intent Routing: Automatically distinguishes between general queries and actionable tasks (like scheduling).

Sub-Agent Delegation: Specialized logic handles tool-based interactions (Calendar/Task simulation).

Structured Persistent Memory: Integrated with Google Cloud Firestore to store and retrieve interaction logs.

Scalable Architecture: Fully containerized and deployed as a serverless REST API.

🛠️ Tech Stack
LLM: Vertex AI (Gemini 1.5 Flash)

Backend: Python & FastAPI

Database: Google Cloud Firestore (NoSQL)

Infrastructure: Google Cloud Run (Serverless)

CI/CD: Docker, Artifact Registry, and Google Cloud Build

🚀 How to Verify the Live Project
Navigate to the Live Swagger UI.

Test the Agent: * Expand the POST /ask endpoint.

Click "Try it out".

Enter a prompt: {"prompt": "Schedule a meeting for 4 PM tomorrow"} and hit Execute.

Verify: See the primary_agent_decision field showing the coordination with sub-agents.

Check the Database Retrieval:

Expand the GET /history endpoint.

Click "Try it out" and then Execute.

Verify: See the list of previous interactions retrieved directly from Firestore.

🏗️ Architecture Flow
User Input → FastAPI → Primary Agent (Gemini) → Sub-Agent Execution → Firestore Logging → Result

Multi-Agent Tech Content Crew
An Autonomous Editorial Department powered by CrewAI & streamlit

Project Overview
This project demonstrates a Hierarchical Multi-Agent System that automates the end-to-end process of technical content creation. 
Unlike standard linear AI scripts, this system utilizes a "Supervisory" architecture where a Manager Agent orchestrates a specialized Researcher 
and Writer to deliver fact-checked, high-quality blog posts.

Core Innovation
Model-Agnostic Design: Switch between Google Gemini, Groq (Llama 3), and OpenAI via a single toggle.
Hierarchical Orchestration: Implements a supervisor-led workflow for superior quality control and task delegation.
Real-time Web Intelligence: Agents autonomously use DuckDuckGo Search to fetch live technical data.

Architecture & Flow
The system follows a modular "Frontend-Backend" separation to ensure production-grade scalability.
User Layer (Streamlit): Captures the topic and preferred LLM provider.
Management Layer (Manager Agent): Analyzes the request and manages the delegation cycle.
Execution Layer (Worker Agents): * Researcher: Performs deep-web searches and synthesizes data.
Writer: Drafts professional Markdown content based on research context.
Validation Loop: The Manager reviews the output, triggering revisions if the content fails to meet the specified "Expected Output" criteria.

Tech Stack
Orchestration: CrewAI (Hierarchical Process)
LLMs: Google Gemini 1.5 Flash, Groq (Llama 3.3), OpenAI GPT-4o-mini
Web Tools: DuckDuckGo Search API
UI Framework: Streamlit
Observability: LangChain/LangSmith tracing compatible


Scalability: Describe how the AgenCrew.py backend is decoupled from the UI, allowing for future API integration.
Cost Control: Explain the "Multi-LLM" strategy—using faster/cheaper models (Groq) for management and high-reasoning models (Gemini/OpenAI) for content.
Error Handling: Discuss the use of the @tool decorator to resolve Pydantic validation conflicts between CrewAI and LangChain tools.
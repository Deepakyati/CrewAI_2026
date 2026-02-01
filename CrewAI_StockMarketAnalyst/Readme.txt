AI Stock Market Analyst Team
Hierarchical Multi-Agent System for Financial Intelligence

Project Overview
This project is an autonomous Virtual Investment Firm that leverages a hierarchical multi-agent architecture to perform real-time financial analysis. 
The system moves beyond simple RAG (Retrieval-Augmented Generation) by simulating a professional team where agents collaborate, 
challenge each other, and provide synthesized investment advice.

Core Problem Solved
Individual LLMs suffer from "Knowledge Cutoffs" and "Context Overload" when analyzing volatile markets. This system solves this by:
Bridging the Real-time Gap: Using specialized tools to fetch live earnings news and market sentiment.
Introducing Management Oversight: A Manager Agent reviews worker outputs to ensure a balanced, objective "Buy/Sell/Hold" recommendation.

System Architecture
The project utilizes a Hierarchical Process to ensure high-fidelity outputs:
Financial Data Researcher (The Scout): Scans the web using DuckDuckGo for the latest news, earnings, and macro events.
Technical Analyst (The Mood Reader): Interprets research data to gauge market sentiment and identify bullish/bearish trends.
Senior Investment Manager (The Decision Maker): Acts as the supervisor, reviewing all data and synthesizing it into a final professional report with a dedicated Risk Assessment.

Tech Stack
Orchestration: CrewAI (Hierarchical Process)
LLM Support: Model-agnostic design supporting Google Gemini, Groq (Llama 3), and OpenAI.
Web Integration: DuckDuckGo Search API via LangChain Community.
UI Layer: Streamlit (Modularized from backend logic).
Data Validation: Pydantic v2.


Key Engineering Highlights (Interview Talking Points)
Modular Backend: The agentic logic in financecrew.py is fully decoupled from the UI, allowing it to be repurposed as a standalone API or CLI tool.
Custom Tool Wrapping: Implemented a robust @tool wrapper for search functions to resolve Pydantic validation conflicts between CrewAI and LangChain.
Conflict Resolution: The Manager Agent is specifically prompted to identify discrepancies between the Researcher's facts and the Analyst's sentiment, mimicking real-world risk management.

License
Distributed under the MIT License. See LICENSE for more information.
import os
from crewai import Agent, Task, Crew, Process
from crewai.tools import tool # Standard CrewAI tool decorator
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

def get_llm(provider):
    """Factory to return the selected LLM provider."""
    if provider == "Google Gemini":
        return ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    elif provider == "Groq (Llama 3)":
        return ChatGroq(model_name="llama-3.3-70b-versatile")
    else:
        return ChatOpenAI(model="gpt-4o-mini")

# --- CUSTOM TOOL DEFINITION ---
@tool("DuckDuckGoSearch")
def duckduckgo_search(query: str):
    """
    Search the web to get the latest information on a specific topic.
    This tool is best for finding news and current events.
    """
    search = DuckDuckGoSearchRun()
    return search.run(query)

def run_tech_crew(provider, topic):
    """Initializes and executes the hierarchical crew."""
    llm = get_llm(provider)

    # 1. Define Agents
    researcher = Agent(
        role='Senior Tech Researcher',
        goal='Uncover the latest 3-5 major developments in {topic}',
        backstory="You are a meticulous tech scout specialized in finding breakthrough news.",
        tools=[duckduckgo_search], # Use the decorated function
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
    
    writer = Agent(
        role='Tech Content Writer',
        goal='Write a compelling 500-word blog post about {topic}',
        backstory="You are a professional tech journalist who makes complex topics easy to read.",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
    
    manager = Agent(
        role='Editor-in-Chief',
        goal='Coordinate the researcher and writer to deliver a flawless tech report on {topic}.',
        backstory="You oversee the quality and flow of information. You delegate and review.",
        llm=llm,
        verbose=True,
        allow_delegation=True
    )

    # 2. Define Tasks
    task1 = Task(
        description="Research the most recent breakthroughs in {topic}.", 
        expected_output="A list of 3-5 key findings with brief explanations.", 
        agent=researcher
    )
    
    task2 = Task(
        description="Transform the research results into a formatted Markdown blog post.", 
        expected_output="A full blog post with a title and strategic insights.", 
        agent=writer
    )

    # 3. Create & Execute Crew
    tech_crew = Crew(
        agents=[researcher, writer],
        tasks=[task1, task2],
        manager_agent=manager,
        process=Process.hierarchical,
        verbose=True
    )
    
    return tech_crew.kickoff(inputs={'topic': topic})
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage
from app.config.settings import settings

def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):
    # Attach system prompt at LLM level
    llm = ChatGroq(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # create agent (no state_modifier)
    agent = create_react_agent(
        model=llm,
        tools=tools,
    )

    # Build messages state
    state = {"messages": [{"role": "system", "content": system_prompt}] + [{"role": "user", "content": q} for q in query]}

    response = agent.invoke(state)

    messages = response.get("messages", [])

    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    
    return ai_messages[-1] if ai_messages else "No response generated"

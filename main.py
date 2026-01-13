from typing_extensions import TypedDict
from langgraph.graph import START ,END,StateGraph 
from langgraph.graph.message import add_messages
from typing import Annotated
import os 
import sys
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool

load_dotenv()
# normal chatBot
llm = ChatGroq(model="openai/gpt-oss-120b")
llm = init_chat_model("groq:openai/gpt-oss-120b")


def chatbot(state:State):
    return { "messages":[llm.invoke(state["messages"])]}


class State(TypedDict):
    messages: Annotated[list,add_messages]




# graph_builder = StateGraph(State)
# graph_builder.add_node("llmchatbot",chatbot)

# graph_builder.add_edge(START,"llmchatbot")
# graph_builder.add_edge("llmchatbot",END)

# graph = graph_builder.compile()


# from IPython.display import Image,display

# print("hello ji")

# try:
#     # Generate the PNG bytes
#     png_bytes = graph.get_graph().draw_mermaid_png()
    
#     # Save it to a file
#     with open("graph.png", "wb") as f:
#         f.write(png_bytes)
#     print("Graph saved as graph.png")
# except Exception as e:
#     print(f"Error generating graph: {e}")
    

from langchain_tavily import TavilySearch
import requests
from langgraph.prebuilt import ToolNode,tools_condition
tavily_tool = TavilySearch(max_results=3)

@tool
def scrape_website(url: str):
    """Useful for reading the full content of a specific webpage URL."""
    try:
        response = requests.get(f"https://r.jina.ai/{url}", timeout=15)
        return response.text
    except Exception as e:
        return f"Error scraping site: {str(e)}"


tools = [tavily_tool,scrape_website]

llm_with_tools = llm.bind_tools(tools)

def tool_calling_llm(state:State):
    return {"messages":llm_with_tools.invoke(state["messages"])}



# res = graph.invoke({"messages":"hello, how are you?"})


# print(res["messages"][-1].content)
    
graph_builder = StateGraph(State)

tool_node = ToolNode(tools=tools)
graph_builder.add_node("llm_agent",tool_calling_llm)
graph_builder.add_node("tools", tool_node)



graph_builder.add_edge(START,"llm_agent")
graph_builder.add_conditional_edges(
    "llm_agent",
    tools_condition,
    
    )

graph_builder.add_edge("tools","llm_agent")   
# graph_builder.add_edge("llm_agent",END)   


graph = graph_builder.compile() 


from IPython.display import Image,display

# print("hello ji")

try:
    # Generate the PNG bytes
    png_bytes = graph.get_graph().draw_mermaid_png()
    
    # Save it to a file
    with open("graph.png", "wb") as f:
        f.write(png_bytes)
    print("Graph saved as graph.png")
    res = graph.invoke({"messages":"what is the resent ai news?"})
    final_answer = res["messages"][-1].content
    print(final_answer.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
except Exception as e:
    print(f"Error generating graph: {e}")
    
    
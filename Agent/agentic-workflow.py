
from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.prebuilt import ToolNode,tools_condition 
from langgraph.graph import START,END,StateGraph





class GraphBuilder():
    
    def __init__(self):
        pass
    
    
    def agent_function(self):
        pass
    
    def build_graph(self):
        pass
    
    
    def __call__(self):
        response = requests.get(f"https://r.jina.ai/{url}", timeout=15)
        return response.text
    except Exception as e:
        return f"Error scraping site: {str(e)}"






    
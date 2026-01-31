

import os
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal, Optional
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAI
from utils.config_loader import load_config


from configparser import ConfigParser
from sys import executable
from timeit import default_timer

class ConfigLoader:
    def __init__(self):
        self.config = load_config() ## information about the model name and the engine that we need to use
        
    def __getitem__(self,key:str):
        return self.config[key]
    
    
    

class ModelLoader(BaseModel):
    model_Provider : Literal["groq","google"] = "groq"
    config : Optional[ConfigLoader] = Field(default=None)
    
    class Config:
        arbitrary_types_allowed = True
        
    def model_post_init(self,__context:any) -> None:
        self.config = ConfigLoader() 
        
        
    
    # this will use everywhere where we need to change model and excpily the model we want to use
    def load_llm(self):
        """
        This function will load the llm model based on the model provider
        """
        
        if self.model_Provider == "groq":
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model=model_name,api_key=groq_api_key) # using .invoke for quering anything to the llm
            
        elif self.model_Provider == "google":
            google_api_key = os.getenv("GOOGLE_API_KEY")
            model_name = self.config["llm"]["google"]["model_name"]
            llm = GoogleGenerativeAI(model=model_name,api_key=google_api_key) # using .invoke for quering anything to the llm
            
            
        return llm
    
    
    
    
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
from agents.prompts.DataAnalyzerPrompt import DATA_ANALYZER_MSG



def getDataAnalyzerAgent(model_client):
    data_analyzer_agent= AssistantAgent(
        name= "Data_Analyzer_Agent",
        description="An agent which help solving data analysis task and given the code as well",
        model_client= model_client,
        system_message= DATA_ANALYZER_MSG
    )
    
    return data_analyzer_agent
    

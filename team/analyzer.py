from agents.Code_Executor_Agent import GetCodeExecutionAgent
from agents.Data_analyzer_agent import getDataAnalyzerAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination


def getAnalyzerTeam(model_client,docker):
    
    code_executor_agent = GetCodeExecutionAgent(docker)
    
    data_analyzer_agent = getDataAnalyzerAgent(model_client)
    
    text_termination_condition = TextMentionTermination(text='STOP')
    
    team = RoundRobinGroupChat(
        participants= [data_analyzer_agent,code_executor_agent],   #the sequence is important
        max_turns= 10,
        termination_condition= text_termination_condition
        )
    return team
    
    
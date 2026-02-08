import streamlit as st 
import asyncio
import os

import asyncio
from team.analyzer import getAnalyzerTeam
from config.openai_model_client import get_model_client
from config.docker_utils import getDockerCommandLineExecutor,start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult


st.title("Analyzer -Digital data analyzer")

uploaded_file=st.file_uploader("upload your csv file",type='csv')

if 'messages' not in st.session_state:
    st.session_state.messages =[]
if 'autogen_team_state' not in st.session_state:
    st.session_state.autogen_team_state = None
    

# task = st.text_input("Enter you task", value='can you give me number of rows in my data (file is data.csv)')
task = st.chat_input("Enter your task")

async def run_analyzer(docker,openai_model_client,task):
    try:
        await start_docker_container(docker)
        team = getAnalyzerTeam(model_client=openai_model_client,docker=docker)
        
        if st.session_state.autogen_team_state is not None:
            await team.load_state(st.session_state.autogen_team_state)
            
        
        async for message in team.run_stream(task=task):
            
            if isinstance(message, TextMessage):
                print(msg := f"{message.source} :{message.content}")
                # yield msg
                
                if msg.startswith('user'):
                    st.chat_message('user',avatar='👱')
                    st.markdown(msg)
                elif msg.startswith('Data_Analyzer_Agent'):
                    st.chat_message('Analyzer',avatar='🤖')
                    st.markdown(msg)
                    st.session_state.messages.append(msg)
                elif msg.startswith('CodeExecutor'):
                    st.chat_message('CodeRunner',avatar='💻')
                    st.markdown(msg)
                st.session_state.messages.append(msg)

            elif isinstance(message,TaskResult):
                print(msg:=f"Stop reason {message.stop_reason}")
                st.markdown(msg)
                st.session_state.messages.append(msg)
                
        st.session_state.autogen_team_state = await team.save_state()
                
        return None
                
    except Exception as e:
        print(e)
        return e
        
    finally:
        await stop_docker_container(docker)
        
if st.session_state.messages:
    for msg in st.session_state.messages:
        st.markdown(msg)

if task:
    if uploaded_file is not None and task:
        
        if not os.path.exists('temp'):
            os.makedirs('temp',exist_ok=True)
        
        with open('temp/data.csv','wb') as f:
            f.write(uploaded_file.getbuffer())
            
    openai_model_client = get_model_client()
    docker = getDockerCommandLineExecutor()
    
    error =asyncio.run(run_analyzer(docker,openai_model_client,task))
    
    if error :
        st.error("An error occured:", {error})
    
    if os.path.exists('temp/output.png'):
        st.image('temp/output.png',caption= "Analysis Image")
        
    
    
else:
    st.warning("Please upload .csv file")
            
    

    
    
import asyncio
from team.analyzer import getAnalyzerTeam
from config.openai_model_client import get_model_client
from config.docker_utils import getDockerCommandLineExecutor,start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult


async def main():
    
    openai_model_client = get_model_client()
    docker = getDockerCommandLineExecutor()
    
    team= getAnalyzerTeam(model_client=openai_model_client, docker=docker)
    
    try:
        task ='create the graph of survived and died from titanic.csv file and save it as output.png'
        
        await start_docker_container(docker=docker)
        
        async for message in team.run_stream(task=task):
            print('*'*40)
            if isinstance(message, TextMessage):
                print(message.source, ":-",message.content)
                
            elif isinstance(message,TaskResult):
                print("stop reason: ",message.stop_reason )
                
            print(message)
    
    except Exception as e:
        print(e)
        
    finally:
        await stop_docker_container(docker=docker)
    
    
    

if __name__ == "__main__":
    asyncio.run(main=main())


from autogen_agentchat.agents import CodeExecutorAgent
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
import asyncio

from config.docker_utils import getDockerCommandLineExecutor


def GetCodeExecutionAgent(code_executor):
    
    code_executor_agent= CodeExecutorAgent(
        
        name= 'CodeExecutor',
        code_executor= code_executor,
    )
    
    return code_executor_agent

# async def main():
#     docker= DockerCommandLineCodeExecutor(
#     work_dir= 'temp',
#     timeout= 120
# )
    
    
#     code_executor_agent= GetCodeExecutionAgent(docker)
    
#         # Run the agent with a given code snippet.
#     task = TextMessage(
#         content='''Here is some code
# ```python
# print('Hello world')    
# ```
#     ''',
#             source="user",
#         )
    
#     try :
        
#         await docker.start()
#         res = await code_executor_agent.on_messages(   #whenever new message come in it will start
#             messages=[task],
#             cancellation_token= CancellationToken()   #to stop the agent running inbetween if needed
#             )
#         print('result----->',res)
#         print('*'*100)
#         print('result----->',res.chat_message.content)
#     except Exception as e:
#         print(e)
        
#     finally:
#         await docker.stop()
    
        
# if __name__ == "__main__":
#     asyncio.run(main())
    
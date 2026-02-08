from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import TIMEOUT_DOCKER,WORK_DIR

def getDockerCommandLineExecutor():
    
    docker= DockerCommandLineCodeExecutor(
    work_dir= WORK_DIR,
    timeout= TIMEOUT_DOCKER
    )
    return docker
    
async def start_docker_container(docker):
    print("starting docker container")
    await docker.start()
    print("docker container started")
    
async def stop_docker_container(docker):
    print("stopping docker container")
    await docker.stop()
    print("docker container stopped")
from railway_sdk import define_railway, github, project, service


@define_railway
def main(ctx=None):
    DockerAIAgentPython = service(
        "Docker-AI-Agent-Python",
        source=github("AvalonEnjoyer/Docker-AI-Agent-Python", branch="main"),
        start="uvicorn src.main:app --host 0.0.0.0 --port $PORT",
    )
    return project("Agentic AI Deployment", resources=[DockerAIAgentPython])

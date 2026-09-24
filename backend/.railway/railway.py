from railway_sdk import define_railway, project, service

# This repository manages only its own resources in the environment. Other
# repositories export their own partial name.
# See https://docs.railway.com/infrastructure-as-code#multi-repo-projects
PARTIAL = "src"

@define_railway
def main(ctx=None):
    src = service(
        "src",
        start="uvicorn main:app --host 0.0.0.0 --port 8000",
    )
    return project("Agentic AI Deployment Project", resources=[src])

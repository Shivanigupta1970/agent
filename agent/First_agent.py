from langchain.agents import initialize_agent
from .tool import Course_generation_tool, video_transcribed_tool
from .llm import llm

# Initialize the agents
agent1 = initialize_agent(
    tools=[Course_generation_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

agent2 = initialize_agent(
    tools=[video_transcribed_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# This function takes three fields and forms a structured prompt
def run_agent(course_name: str, level: str, expected_outcomes: str) -> str:
    query = (
        f"Using the Course_generation_tool, generate a comprehensive course structure based on:\n"
        f"- Course Name: {course_name}\n"
        f"- Level: {level}\n"
        f"- Expected Outcomes: {expected_outcomes}\n\n"
        f"Include:\n"
        f"1. List of relevant topics\n"
        f"2. Detailed content for each topic\n"
        f"3. Recommended YouTube videos or resources\n"
        f"4. Expected learning outcomes after completion"
    )
    return agent1.run(query)


def run_agent_transcribe(youtube_url):
    return agent2.run(youtube_url)

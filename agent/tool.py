from langchain.agents import Tool
from services.Course_flow_crreation import generate_learning_content
from services.transcribe_video import extract_transcript_details


def wrapped_generate_learning_content(input_text: str):
    try:
        lines = input_text.strip().split('\n')
        course_name = ""
        level = ""
        expected_outcomes = ""

        for line in lines:
            if line.startswith("Course Name:"):
                course_name = line.split(":", 1)[1].strip()
            elif line.startswith("Level:"):
                level = line.split(":", 1)[1].strip()
            elif line.startswith("Expected Outcomes:"):
                expected_outcomes = line.split(":", 1)[1].strip()

        if not course_name or not level or not expected_outcomes:
            return "Error: Missing course details in prompt."

        return generate_learning_content(course_name, level, expected_outcomes)

    except Exception as e:
        return f"Error while parsing input: {str(e)}"

Course_generation_tool=Tool(
        name="Generate Course Content", 
        func=wrapped_generate_learning_content,
        description="Generates detailed course content based on topic."
)

video_transcribed_tool=Tool(
    name="Summarize YouTube Video", 
    func=extract_transcript_details,
    description="Summarizes transcript of a YouTube video."
)


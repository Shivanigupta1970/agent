from agent.llm import llm
from services.you_tube_serach import youtube_search
from services.clean_response import clean_and_parse_gemini_response

def generate_learning_content(course_name, level, expected_outcomes):
    prompt = f"""
    You are an AI course content generator. Based on the following:
    - Course Name: {course_name}
    - Level: {level}
    - Expected Outcomes: {expected_outcomes}

    Provide the following in JSON format:
    {{
      "overview": "<Short overview aligned with the level>",
      "course_content": {{
        "<Topic 1>": {{
          "content": "<Short explanation>",
          "Documentation/websites": {{
            "<Title 1>": "<URL>",
            "<Title 2>": "<URL>"
          }}
        }},
        "<Topic 2>": {{ ... }}
      }}
    }}
    Ensure output is properly formatted JSON.
    """
    # Use invoke instead of generate_content
    response = llm.invoke(prompt)
    clean_response = clean_and_parse_gemini_response(response.content if hasattr(response, 'content') else str(response))

    if not clean_response:
        return None

    for topic, topic_data in clean_response.get("course_content", {}).items():
        video_links = youtube_search(topic)
        topic_data["youtube_videos"] = video_links

    # # Step 1: Print all topic names
    # print("\n📚 Course Topics:")
    # for i, topic in enumerate(clean_response['course_content'].keys(), start=1):
    #     print(f"{i}. {topic}")
    # print(clean_response)
    return clean_response

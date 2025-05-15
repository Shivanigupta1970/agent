from youtube_transcript_api import YouTubeTranscriptApi

def extract_transcript_details(youtube_video_url: str)-> str:
    try:
        video_id = youtube_video_url.split("v=")[-1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript

    except Exception as e:
        return None
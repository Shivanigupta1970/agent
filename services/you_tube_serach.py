from googleapiclient.discovery import build

def youtube_search(query):
    youtube = build("youtube", "v3", developerKey="AIzaSyAzLwlaVhGLK9-Aj88RnGGdS4zuNxEn64s")
    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=3,
        type="video"
    )
    response = request.execute()

    videos = []
    for item in response["items"]:
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        url = f"https://www.youtube.com/watch?v={video_id}"
        videos.append({title: url})

    return videos

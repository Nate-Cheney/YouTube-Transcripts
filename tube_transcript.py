def extract_youtube_video_id(url):
    from pytube import extract
    return extract.video_id(url)


def extract_youtube_transcript(url):
    import youtube_transcript_api
    from youtube_transcript_api import YouTubeTranscriptApi

    video_id = extract_youtube_video_id(url)
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)  # gets a list of all transcripts for the provided video_id

        if transcript_list.find_manually_created_transcript(["en"]):
            return transcript_list.find_manually_created_transcript(["en"]).fetch()
        elif transcript_list.find_generated_transcript(["en"]):
            return transcript_list.find_generated_transcript(["en"]).fetch()
        else:
            print("No transcript found")
    except youtube_transcript_api._errors.NoTranscriptFound:
        return YouTubeTranscriptApi.get_transcript(video_id)


def process_transcript(transcript_list):
    transcript = str()
    for dictionary in transcript_list:
        transcript += (dictionary["text"] + "\n")

    return transcript

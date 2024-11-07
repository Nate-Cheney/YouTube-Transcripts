from tube_transcript import *
import os


if __name__ == "__main__":
    url_list = [
        "https://www.youtube.com/watch?v=gpX0tnFot-8&t=1s"
    ]

    dir_path = r"transcripts"

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    os.chdir(dir_path)
    count = 1
    for url in url_list:
        with open(f"video{count}.txt", "w") as file:
            file.write(process_transcript(extract_youtube_transcript(url)))
        count += 1

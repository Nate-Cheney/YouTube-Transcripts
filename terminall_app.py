import os
import re
import transcript as yt


if __name__ == "__main__":
    print("Instructions")
    while True:
        output_dir = input("\nEnter the desired ouput directory:\n\t")
        if os.path.exists(output_dir):
            break
        else:
            output_dir = "transcripts"
            break

    while True:
        # Repeat transcription until user quits.
        url = input("\nEnter a URL to a YouTube playlist or video:\n")

        if re.match("^(https://www.youtube.com/playlist)", url):
            playlist = yt.get_playlist_videos(url)
            for video in playlist:
                yt.transcript_main(url=video, dir_path=output_dir)
                
        elif re.match("^(https://www.youtube.com/watch)", url) or re.match("^https://youtu.be/", url):
            yt.transcript_main(url=url, dir_path=output_dir)

        else:
            print("\nThe URL provided is invalid.\n")
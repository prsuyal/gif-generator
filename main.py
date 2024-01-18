import os
import sys
from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_video_segment(url, start_time, end_time):
     try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=False, file_extension='mp4').first()
        if not stream:
            raise Exception("No suitable stream found for the provided URL.")

        video_path = stream.download()
        clip = VideoFileClip(video_path).subclip(start_time, end_time)
        segment_path = f"temp_{os.path.basename(video_path)}"
        clip.write_videofile(segment_path, codec="libx264")
        os.remove(video_path)

        return segment_path
    except Exception as e:
        sys.exit(f"Error: {e}")


def convert_to_gif(video_path, gif_path):
      try:
        clip = VideoFileClip(video_path)
        clip.write_gif(gif_path)
        os.remove(video_path)  
    except Exception as e:
        sys.exit(f"Error: {e}")
import pytube
import subprocess



url = "https://www.youtube.com/watch?v=mpjREfvZiDs"

def download(url):
	yt = pytube.YouTube(link)
	audio_name = yt.streams.filter(only_audio=True).desc().first().default_filename
	print(audio_name)
	video_name = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first().default_filename
	print(video_name)
	audio_stream = yt.streams.filter(only_audio=True).desc().first()
	videao_stream = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
	audio_stream.download()
	videao_stream.download()
	subprocess.run(["ffmpeg", "-i", video_name, "-i", audio_name, "-c:v", "copy", "-c:a", "aac", video_name])
	
download(url)

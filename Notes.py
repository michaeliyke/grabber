"""
# https://pytube.io/en/latest/user/install.html
# https://pytube.io/en/latest/
# https://pytube.io/en/latest/api.html
url = "https://youtu.be/q9irhFGryR4" # OriginaL
url = "http://youtube.com/watch?v=2lAe1cqCOXo"
yt = YouTube(url)

# CAPTIONS
captions = yt.captions
caption = yt.captions.get_by_language_code("en")
xml = caption.xml_captions
srt = caption.generate_srt_captions()


for stream in yt.streams:
	print(stream)

yt.streams.first().download() 

progressive = yt.streams.filter(progressive=True) # 700p and below
DASH = yt.streams.filter(adaptive=True) # Dynamic Adaptive Streaming Over Https
audioOnly = yt.streams.filter(only_audio=True) # Audio only files
mp4s = yt.streams.filter(subtype=True) # .mp4 only files

# Note: To implemenT downloaD in web app:
# First download to server filesystem, read as binary and delete when done
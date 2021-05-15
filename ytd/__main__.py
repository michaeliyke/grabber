import os, sys
os.system("CLS")

try:
	url = sys.argv[1]
	from pytube import YouTube, Playlist
except Exception as e:
	print("Some required are part mssing..")
	exit("Error: {}".format(e))


# def processFile():
# 	# Called after a video is done downloading for post download processing
# 	pass

# def progressUpdate():
# 	# Called whenever a chunk is downloaded from a video
# 	# This Could be used to display a progress bar
# 	pass

print("Downloading...")

yt = YouTube(
        url,
        # on_progress_callback=progressUpdate,
        # on_complete_callback=processFile
        # proxies=my_proxies
    )

goodQualityVideos = yt.streams.filter(progressive=True)

goodQualityVideos.first().download()

print("Done!")

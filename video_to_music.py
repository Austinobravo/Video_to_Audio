import moviepy.editor

#Input the video

video = moviepy.editor.VideoFileClip("video.mp4")

#Converting to an audio

audio = video.audio
audio.write_audiofile("audio.mp3")
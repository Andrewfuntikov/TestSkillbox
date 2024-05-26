def my_function():
    """Привет это текст дукоментации


    А это продолжение)))"""
    print(123)

print(my_function.__doc__)

import pytube

link = 'https://youtu.be/vQ2A6foqn38?si=rIcj4TfyWeRfEwR0'
link = pytube.YouTube(link)
video = link.streams.get_highest_resolution()
video.download()
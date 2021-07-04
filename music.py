from pygame import mixer
mixer.init() 
def mymusic(user):   
    if user == "1":
        mixer.music.load("one.ogg")     # Loading the song
        mixer.music.set_volume(0.7)     # Setting the volume
        mixer.music.play()              # Start playing the song
        return
        
    if user == "2":
        mixer.music.load("two.ogg")     # Loading the song
        mixer.music.set_volume(0.7)     # Setting the volume
        mixer.music.play()              # Start playing the song
        return

    if user == "3":
        mixer.music.load("three.ogg")   # Loading the song
        mixer.music.set_volume(0.7)     # Setting the volume
        mixer.music.play()              # Start playing the song
        return

    if user == "4":
        mixer.music.load("four.ogg")   # Loading the song
        mixer.music.set_volume(0.7)     # Setting the volume
        mixer.music.play()              # Start playing the song
        return

    if user == "5":
        mixer.music.load("five.ogg")     # Loading the song
        mixer.music.set_volume(0.7)     # Setting the volume
        mixer.music.play()              # Start playing the song
        return

    if user == "#":
        mixer.music.stop()              # Stop playing the song
        return


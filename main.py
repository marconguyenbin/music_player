from tkinter import *
from tkinter import filedialog
import pygame
import os

#root is the window, geometry sets the size of the window
root = Tk()
root.title('Music Player')
root.geometry("500x300")

#initlize the pygame music mixer, allows us to play audio
pygame.mixer.init()

menu_bar = Menu(root)
root.config(menu=menu_bar) #set root windows menu bar to the main 
songs = []
current_song = ""
paused = False

def load_music():
    global current_song  # Declare 'current_song' as a global variable to access it outside the function
    root.directory = filedialog.askdirectory()  # Open a dialog box to select a directory

    # Create an empty list to store the names of the MP3 files
    songs = []

    # Loop through each file in the selected directory
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)  # Split the filename and extension
        if ext == '.mp3':  # Check if the file has the '.mp3' extension
            songs.append(song)  # Add the file name to the 'songs' list

    # Loop through the list of song names and insert them into the 'songlist' Listbox
    for song in songs:
        songlist.insert("end", song)  # Insert each song name at the end of the Listbox

    songlist.selection_set(0)  # Select the first song in the Listbox (highlight it)
    current_song = songs[songlist.curselection()[0]]  # Set 'current_song' to the first song name



def play_music():
    global current_song, paused  # Declare 'current_song' and 'paused' as global variables

    # Check if the music is not paused
    if not paused:
        # Load the selected song using its full path (directory + filename)
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        # Start playing the loaded song
        pygame.mixer.music.play()
    else:
        # If music is paused, unpause (resume) the playback
        pygame.mixer.music.unpause()
        paused = False  # Set 'paused' to False since music is now playing



def pause_music():
    global paused  # Declare 'paused' as a global variable
    pygame.mixer.music.pause()  # Pause the music playback using pygame
    paused = True  # Set 'paused' to True to indicate that the music is paused

def next_music():
    global current_song, paused  # Declare 'current_song' and 'paused' as global variables

    try:
        # Clear the current selection in the songlist Listbox
        songlist.selection_clear(0, END)
        # Set the selection to the next song in the 'songs' list
        songlist.selection_set(songs.index(current_song) + 1)
        # Update 'current_song' to the name of the newly selected song
        current_song = songs[songlist.curselection()[0]]
        # Play the newly selected song
        play_music()
    except:
        pass  # If an error occurs (e.g., end of playlist), simply do nothing


def rewind_music():
    global current_song, paused  # Declare 'current_song' and 'paused' as global variables

    try:
        # Clear the current selection in the songlist Listbox
        songlist.selection_clear(0, END)
        # Set the selection to the previous song in the 'songs' list
        songlist.selection_set(songs.index(current_song) - 1)
        # Update 'current_song' to the name of the newly selected song
        current_song = songs[songlist.curselection()[0]]
        # Play the newly selected song
        play_music()
    except:
        pass  # If an error occurs (e.g., beginning of playlist), simply do nothing


file = Menu(menu_bar, tearoff=False)
file.add_command(label='Select Folder',command=load_music)  # Use 'label' instead of 'Label'
menu_bar.add_cascade(label='File', menu=file)

songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

#import images for menu
play_btn_img = PhotoImage(file='play.png')
pause_btn_img = PhotoImage(file='pause.png')
rewind_btn_img = PhotoImage(file='rewind.png')
next_btn_img = PhotoImage(file='next.png')

#create a frame able to section off our app
control_frame = Frame(root)
control_frame.pack()

# Create buttons with separate variable names
play_btn = Button(control_frame, image=play_btn_img, borderwidth=0, command = play_music)
pause_btn = Button(control_frame, image=pause_btn_img, borderwidth=0, command = pause_music)
rewind_btn = Button(control_frame, image=rewind_btn_img, borderwidth=0, command = rewind_music)
next_btn = Button(control_frame, image=next_btn_img, borderwidth=0, command = next_music)

#grid to allow them on the same line
play_btn.grid(row=0, column=0, padx=7, pady=10)
pause_btn.grid(row=0, column=1, padx=7, pady=10)
rewind_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)

#runs the main program
root.mainloop()



from mr_utils import MR_NOTE_MAP
from tone import Tone
import threading
import time
notes_list = []

class Note:
    def __init__(self, note_str, duration=1): #Class initialization
        mr_main_note = note_str[0].upper() #Note Char Capitalized 
        self.note_str = mr_main_note + note_str[1:] #List slicing to get last character in note. EX: G4 will return 4
        self.duration = duration 
        self.freq = MR_NOTE_MAP[self.note_str]

    def mr_play(self, duration=1, speaker=None):
        Tone.mr_sine(self.freq, duration=duration, speaker=speaker)

    def mr_arpeggiator(notes_list, arp_quantity, duration=1):
        arp_list = [] #List of notes to be arpeggiated. Ex: C, E, G, B will return a list of C, E, G, B, G, E
        note_list = [] #List of notes from notes list
        for i in notes_list:
            arp_list.append(i)
            note_list.append(i)
        note_list.reverse() #Reverses Note List
        note_list.pop(0) #Remove first note, which was previously last note
        note_list.pop(-1) #Remove last note, so that when function is called more than once, it doesn't play "first" note twice
        for j in note_list:
            arp_list.append(j)
        for n in range(arp_quantity): #Plays the notes in the given range, for how many notes are in the list
            for m in arp_list:
                Note.mr_play(m, duration) #Plays the note, with the duration given
    
    @staticmethod
    def mr_drest(duration):
        time.sleep(duration)
    
    @staticmethod
    def mr_play_chord(notes_list):
        note_threads = []

        for note in notes_list:
            note_thread = threading.Thread(target=note.mr_play) #Play multiple notes together using threading
            note_threads.append(note_thread)
        
        for note_thread in note_threads:
            note_thread.start()

        for note_thread in note_threads:
            note_thread.join()
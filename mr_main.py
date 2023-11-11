from tone import Tone
from mr_note import Note

def main():
    Note.mr_arpeggiator([Note('C3'), Note('E3'), Note('G3'), Note('B3'), Note('C4')], 8, .1) 

    Tone.mr_create_tone_from_list([853, 960], 2)

    Tone.mr_sine(440, duration=1)

    Note.mr_play_chord([
    Note('C4'),
    Note('E4'),
    Note('g4')
    ])


if __name__ == "__main__":
    main()





# Tone.mr_create_tone_from_list([530, 660])
# Note('C4').mr_play()
# Note.mr_rest(1)
# Note('E4').mr_play()
# Note('g4').mr_play()


# notes_list = [Note('C3'), Note('E3'), Note('G3'), Note('B3'), Note('C4')]
# notes_list = ['C3', 'E3', 'G3', 'B3', 'C4']
# arp_list = []
# add_notes = []
# for i in notes_list:
#     arp_list.append(i)
# notes_list.reverse()
# del notes_list[0]
# del notes_list[-1]
# for j in notes_list:
#     arp_list.append(j)
# print(arp_list)




import json

def mr_read(path):
    with open(path, 'r') as f:
        return f.read()

def mr_read_json(path):
    return json.loads(mr_read(path))

#This creates a map with each note and their frequency. Ex: A4 will return 440 because that is what it is mapped too in the note_map
MR_NOTE_MAP = mr_read_json('/Users/mahonriray/Documents/BYU I 2023/FallSemester/310BasicSynth/mr_note_map.json')



# print(MR_NOTE_MAP.keys())

# for n in MR_NOTE_MAP:
#     print(n)s
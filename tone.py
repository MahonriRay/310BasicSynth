import pygame
import numpy
import math
import time
import threading

pygame.init()
mr_bits = 16
mr_sample_rate = 44100 #Nyquist Theorem

pygame.mixer.pre_init(mr_sample_rate, mr_bits)


def mr_sine_x(amp, freq, time):
    return int(round(amp * math.sin(2 * math.pi * freq * time)))

class Tone:
    def mr_sine(freq, duration=1, speaker=None): #Frequency is the note, which will be found using the note_map

        mr_num_samples = int(round(duration * mr_sample_rate)) #Samples taken is equal to length of note * sample rate. A note played for one second will have 44100 samples taken

        mr_sound_buffer = numpy.zeros((mr_num_samples, 2), dtype = numpy.int16)
        mr_amplitude = 2 ** (mr_bits - 1) - 1 #Volume of the note being played

        for mr_sample_num in range(mr_num_samples):
            mr_time = float(mr_sample_num) / mr_sample_rate

            mr_sine = mr_sine_x(mr_amplitude, freq, mr_time) #Volume, Note freq, duration

            if speaker == 'r':
                mr_sound_buffer[mr_sample_num][1] = mr_sine #Deciding whice side of the speaker will play the sine wave
            if speaker == 'l':
                mr_sound_buffer[mr_sample_num][0] = mr_sine

            else:
                mr_sound_buffer[mr_sample_num][1] = mr_sine
                mr_sound_buffer[mr_sample_num][0] = mr_sine

        mr_sound = pygame.sndarray.make_sound(mr_sound_buffer)
        mr_sound.play(loops=1, maxtime=int(duration * 1000))
        time.sleep(duration)

    @staticmethod
    def mr_create_tone_from_list(freq_list, duration=1, speaker=None): #Creates a singular tone from a list, similar to the chord function
        freq_threads = []
        for freq in freq_list:
            freq_thread = threading.Thread(target=Tone.mr_sine, args=[freq, duration, speaker])
            freq_threads.append(freq_thread)

        for freq_thread in freq_threads:
            freq_thread.start()

        for freq_thread in freq_threads:
            freq_thread.join()
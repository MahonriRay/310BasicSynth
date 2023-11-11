# Overview

The goal for this project was to create a Basic Synthesizer so that I may familiarize myself with audio in a programming sense. I have a passion for audio engineering and want to further explore audio in the programming world so
a project like this is a great place to begin.

The program I created is a Synthesizer that was coded in Python which creates sine waves from frequency taken from input. It has four functions currently, which are Sine, Create Tone, Play Chord, and an Arpeggiator. The sine fucntion
 simply takes a frequency and with some calculation creates a sine wave. The Create Tone function takes a combination of two frequency and plays back a sine wave. The Play Chord function is very similar to the Create Tone except that 
 the parameter for this function slightly differ. Instead of taking in frequencies in the form of integers, it is passed a "note" such a C4, and with the use of a note map, it returns the sine waves of the notes passed into the function.
 Lastly, the Arpeggiator function, takes in a list of notes and plays them in succession and then back down, excluding the last note and the first note. For example if C3, E3, G3, B3, C4 were passed in as the notes list, it would reverse 
 the list and remove the first and last note so that the arpeggiated notes would be C3, E3, G3, B3, C4, B3, G3, E3. That way if the the arpeggiator paramater that dictates how many times the notes are arpeggiated is more than once
 no single is played twice before going to the next.

As I've stated before the purpose for writing this software is so that I may learn more about programming with audio. The Synthesizer I created has yet to be fully fleshed out and isn't ready to be used with Digital Audio Workstations, 
but it shows how programming audio can be accomplish whatever the user would want. Even a rude implementation of a synthesizer, such as the one I have created greatly demonstrates the power of programming when it comes to audio.


[Software Demo Video](https://youtu.be/BCesJWzrnzE?si=9Hqu9hX18z22J6DZ)

# Development Environment

{Describe the tools that you used to develop the software}
I went through many different languages before settling on python. Every language is capable of implementing audio, but Python had a couple of libraries that already did most of the heavy work that made creating a synthesizer 
more simple than other languages.

The library I used for this project is the Pygame library as it already has a sound engine that I was able to easily use. 


# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Jammin' Coder](https://www.youtube.com/watch?v=egW_J4et4HA)
- [G223 Productions](https://www.youtube.com/watch?v=fp1Snqq9ovw&t=1s)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Fix the "pop" everytime a note play. 
- Implement being able to play notes from the keyboard.
- Implement MIDI Control

# Audio Files Module
Audio Files Python Module provides some functions to read and write audio files.

## Implementation

### Audio File Checker
For each implemented audio format there is an implementation of the class **audio_file_checker**.

In order to create an instance of the correct implementation there is an **audio_file_checker_factory** in which there is a function that will return the correct implementation:

>`
getAudioFileChecker(file: str, extension: str) ->   
audio_file_checker
`

Currently the following extensions are implemented:
- .wav
- .mp3

The class **audio_file_checker** contains the following methods implemented:
- _isTwoChannels ( )_ &rarr; returns *True* if the audio is Dual Mono or Stereo
- _isMono ( )_ &rarr; returns *True* if the audio is Mono
- _isStereo ( )_ &rarr; return *True* if the audio is Stereo
- _isDualMono ( )_ &rarr; returns *True* if the audio is Dual Mono 
- _getSr ( )_ &rarr; returns the *Sample Rate*
- _getLeftChannel ( )_ &rarr; returns the *left channel data* (in case of a mono audio file returns the audio data)
- _getRightChannel ( )_ &rarr; returns the *right channel data* (in case of a mono audio file returns None)

### Dual Mono Converter

The class **dual_mono_converter** has a constructor that takes two strings:
- *input* &rarr; a string with the path to a file or a folder
- *output* &rarr; a string with the path to the output folder 

Calling the method *convert ( )* will check the file (or folder) in input. 
Each dual mono file found will be converted to mono and written in the output folder, the other files will be simply copied, the method returns two lists: one for the converted files and one for the copied files.
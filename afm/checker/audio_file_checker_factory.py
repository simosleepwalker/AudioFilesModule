from .audio_file_checker import audio_file_checker
from .impl.wav_audio_file_checker import wav_audio_file_checker
from .impl.mp3_audio_file_checker import mp3_audio_file_checker

def getAudioFileChecker(file: str, extension: str, threshold =  0.001) -> audio_file_checker:
    if extension in ('wav', '.wav') :
        return wav_audio_file_checker(file, threshold)
    if extension in ('mp3','.mp3'):
        return mp3_audio_file_checker(file, threshold)
    raise NotImplemented
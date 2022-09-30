import librosa
from afm.checker.audio_file_checker import audio_file_checker
import pandas as pd

class wav_audio_file_checker(audio_file_checker):

    #in case of mono, data is stored in left channel
    def getLeftChannel(self):
        return self.leftChannel
    
    def getRightChannel(self):
        return self.rightChannel

    def __init__(self, path: str) -> None:
        self.data, self.sr = librosa.load(path, sr=None, mono=False)
        self.data = self.data
        if self.data.shape[0] == 2:
            self.channels = 2
            self.leftChannel = self.data[0]
            self.rightChannel = self.data[1]
        else:
            self.channels = 1
            self.leftChannel = self.data
from array import array
from fileinput import filename
from typing import List
import soundfile as sf
import os
import librosa


class audio_file_exporter:

    def export(self) -> bool:
        try:
            sf.write(self.outputpath + self.filename, self.data, self.sr)
            return True
        except:
            return False

    def __init__(self, filename: str, data: array, sr: int, outputpath: str = None) -> None:
        self.filename = filename
        self.sr = sr
        self.data = data
        self.outputpath = outputpath if outputpath != None else ''
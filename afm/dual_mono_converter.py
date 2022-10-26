from tabnanny import check
from typing import List
import glob2
import os
import checker.audio_file_checker_factory
from exporter.audio_file_exporter import audio_file_exporter as afe
import shutil

class dual_mono_converter:

    #returns a list of the converted files and a list of just copied files
    def convert(self) -> List:
        converted = []
        not_converted = []
        for file in self.files:
            filename, fileext = os.path.splitext(file)
            filename =  os.path.splitext(os.path.basename(file))[0]
            checker = checker.audio_file_checker_factory.getAudioFileChecker(file, fileext)

            monoButStereo = checker.isMonoButStereo()
            if monoButStereo != False:
                exporter = afe(filename + '_exported' + fileext, checker.getLeftChannel() if monoButStereo == 'L'  else checker.getRightChannel(), checker.getSr(), self.output)
                result = exporter.export()
                if (result == True):
                    converted.append(filename+fileext)
                else:
                    raise Exception
            elif checker.isDualMono():
                exporter = afe(filename + '_exported' + fileext, checker.getLeftChannel(), checker.getSr(), self.output)
                result = exporter.export()
                if (result == True):
                    converted.append(filename+fileext)
                else:
                    raise Exception
            else:
                shutil.copy(file,self.output)
                not_converted.append(filename+fileext)
        return converted, not_converted         


    def __init__(self, input: str, output: str) -> None:
        if os.path.isdir(output) and (os.path.dirname(input) != output):
            self.output = output
            if (os.path.isdir(input)):
                self.files = glob2.glob(input+'/*.wav') + glob2.glob(input+'/*.mp3')
            else:
                self.files = input
        else:
            raise Exception
from tabnanny import check
from typing import List
import glob2
import os
from .checker import audio_file_checker_factory
from .exporter.audio_file_exporter import audio_file_exporter as afe
import shutil
import logging
import sys

class dual_mono_converter:

    #returns a list of the converted files and a list of just copied files
    def convert(self) -> List:
        converted = []
        not_converted = []
        for file in self.files:
            filename, fileext = os.path.splitext(file)
            filename =  os.path.splitext(os.path.basename(file))[0]
            logging.info("=========== ANALYZING FILE {} ===========".format(filename + fileext)) 
            checker = audio_file_checker_factory.getAudioFileChecker(file, fileext, self.threshold)

            monoButStereo = checker.isMonoButStereo()
            if checker.isDualMono():
                logging.info(msg='File {} is DUAL MONO'.format(filename + fileext))
                exporter = afe(filename + '_exported' + fileext, checker.getLeftChannel(), checker.getSr(), self.output)
                result = exporter.export()
                if (result == True):
                    converted.append(filename+fileext)
                    logging.info(msg='File {} converted'.format(filename + fileext))
                else:
                    raise Exception
            elif monoButStereo != False:
                logging.info(msg='File {} is MONO BUT STEREO'.format(filename + fileext))
                exporter = afe(filename + '_exported' + fileext, checker.getLeftChannel() if monoButStereo == 'L'  else checker.getRightChannel(), checker.getSr(), self.output)
                result = exporter.export()
                if (result == True):
                    converted.append(filename+fileext)
                    logging.info(msg='File {} converted'.format(filename + fileext))
                else:
                    raise Exception
            else:
                if checker.isMono():
                    logging.info(msg='File {} is MONO'.format(filename + fileext))
                else:
                    logging.info(msg='File {} is STEREO'.format(filename + fileext))
                shutil.copy(file,self.output)
                not_converted.append(filename+fileext)
                logging.info(msg='File {} copied'.format(filename + fileext))
        return converted, not_converted         

    def __init__(self, input: str, output: str, loggingoutput = sys.stdout, threshold = 0.001) -> None:
        logging.basicConfig(level=logging.INFO, stream=loggingoutput)
        self.threshold = threshold
        if os.path.isdir(output) and (os.path.dirname(input) != output):
            self.output = output
            if (os.path.isdir(input)):
                self.files = glob2.glob(input+'/*.wav') + glob2.glob(input+'/*.mp3')
            else:
                self.files = [ input ]
        else:
            raise Exception
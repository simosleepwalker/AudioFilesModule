import pandas as pd

class audio_file_checker:

    #does not implicate is stereo
    def isTwoChannels(self) -> bool:
        return True if self.channels > 1 else False

    def isMono(self) -> bool:
        return True if self.channels == 1 else False
    
    def isStereo(self) -> bool:
        return not(self.isDualMono())

    def isDualMono(self) -> bool:
        if (self.isMono()):
            return False
        difference = []
        ziplist = zip(self.getLeftChannel(), self.getRightChannel())
        for list1_i, list2_i in ziplist:
            if (list1_i - list2_i != 0.0):
                return False
        return True
    
    def getSr(self) -> int:
        return self.sr
        
    def getLeftChannel(self):
        pass

    def getRightChannel(self):
        pass

    def __init__(self, path: str) -> None:
        pass
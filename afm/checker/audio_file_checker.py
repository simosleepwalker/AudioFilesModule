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
            if (abs(list1_i - list2_i) > self.tolerance):
                return False
        return True
    
    def isMonoButStereo(self) -> str:
        if (self.isMono()):
            return False
        difference = []
        ziplist = zip(self.getLeftChannel(), self.getRightChannel())
        for list1_i, list2_i in ziplist:
            difference = abs(list1_i - list2_i)
            if (abs(list1_i - difference) > self.tolerance):
                return 'L'
            elif (abs(list2_i - difference) > self.tolerance):
                return 'R'
        return False
    
    def getSr(self) -> int:
        return self.sr
        
    def getLeftChannel(self):
        pass

    def getRightChannel(self):
        pass

    def __init__(self, path: str, tolerance: int = 0.001) -> None:
        self.tolerance = tolerance
        pass
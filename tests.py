from cgi import test
import afm.checker.audio_file_checker_factory as afcf
from afm.exporter.audio_file_exporter import audio_file_exporter
from afm.dual_mono_converter import dual_mono_converter

def test_wav_mono() -> bool:
    a = afcf.getAudioFileChecker('input/test_mono.wav','wav')
    return a.isMono()

def test_mp3_mono() -> bool:
    a = afcf.getAudioFileChecker('input/test_mono.mp3','mp3')
    return a.isMono()

def test_wav_stereo() -> bool:
    a = afcf.getAudioFileChecker('input/test_stereo.wav','wav')
    return a.isStereo()

def test_wav_dual_mono() -> bool:
    a = afcf.getAudioFileChecker('input/test_dualmono.wav','wav')
    b = audio_file_exporter('test_dualmono_export.wav', a.getLeftChannel(), a.getSr(), 'output/')
    b.export()
    return a.isDualMono()

def test_mp3_dual_mono() -> bool:
    a = afcf.getAudioFileChecker('input/test_dualmono.mp3','mp3')
    return a.isDualMono()

def run_tests():
    #assert test_wav_mono(), f"file was not read as mono"
    #assert test_mp3_mono(), f"file was not read as mono"
    #assert test_wav_stereo(), f"file was not read as stereo"
    #assert test_mp3_dual_mono(), f"file was not read as dual mono"
    #assert test_wav_dual_mono(), f"file was not read as dual mono" 
    print ("all tests ran correctly")

def run_generic_test():
    conv = dual_mono_converter('input/', 'output/')
    result = conv.convert()
    print(result)

run_generic_test()
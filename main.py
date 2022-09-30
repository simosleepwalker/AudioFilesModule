from afm.checker.audio_file_checker import audio_file_checker

a = audio_file_checker('input/test_stereo.wav')
print(a.isTwoChannels())
# 制作一个脚本，我想传入一个mp3格式的音频文件，然后可以将它的音频转为通过c++播放的格式
# 但是我不知道怎么做，我想用python来做，但是我不知道怎么做
# 请问有人知道怎么做吗？

import os
import sys
import wave
import struct
import numpy as np
import matplotlib.pyplot as plt


def wav2raw(wav_file, raw_file):
    wav = wave.open(wav_file, 'rb')
    raw = open(raw_file, 'wb')
    nframes = wav.getnframes()
    data = wav.readframes(nframes)
    raw.write(data)
    wav.close()
    raw.close()


def raw2wav(raw_file, wav_file):
    raw = open(raw_file, 'rb')
    wav = wave.open(wav_file, 'wb')
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(8000)
    data = raw.read()
    wav.writeframes(data)
    raw.close()
    wav.close()


def raw2txt(raw_file, txt_file):
    raw = open(raw_file, 'rb')
    txt = open(txt_file, 'w')
    data = raw.read()
    for i in range(len(data)):
        txt.write(str(data[i]) + '\n')
    raw.close()
    txt.close()

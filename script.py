import os
import matplotlib.pyplot as plt
#for loading and visualizing audio files
import librosa
import librosa.display
#to play audio
import IPython.display as ipd
import numpy as np
from PIL import Image
# import Audio and Spectrogram classes from OpenSoundscap
from opensoundscape.audio import Audio
from opensoundscape.spectrogram import Spectrogram
import cv2

Datadir = 'B:Data/genres_original'
Wrdir = 'B:Data'
category = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]

def write(file, types):
    # approach 1
    # x, sr = librosa.load(Datadir+'/'+types+'/'+file, sr=44100, mono=True)
    # StrtMin = 0
    # StrtSec = 0
    # EndMin = 0
    # EndSec = 300
    # # Time to milliseconds conversion
    # StrtTime = StrtMin * 60 * 1000 + StrtSec * 1000
    # EndTime = EndMin * 60 * 1000 + EndSec * 1000
    # extract = x[StrtTime:EndTime]
    # X = librosa.stft(extract)
    # Xdb = librosa.amplitude_to_db(abs(X))
    # fig = plt.figure(figsize=(14, 5))
    # librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
    # # plt.colorbar()
    # z = file.removesuffix('.wav')
    # z = z + '.png'
    # print(z)
    # fig.savefig(Wrdir + '/myimg/' + types + '/' + z)
    # plt.cla()
    # plt.close('all')

    # # approach 2
    if file == 'jazz.00053.wav' or file == 'jazz.00054.wav':
        return
    # print(file)
    audio_fpath = Datadir+'/'+types+'/'+file
    audio_object = Audio.from_file(audio_fpath)
    spectrogram_object = Spectrogram.from_audio(audio_object)
    # spectrogram_object.plot()
    # Trim the original audio
    trimmed0 = audio_object.trim(0, 5)
    trimmed1 = audio_object.trim(5, 10)
    trimmed2 = audio_object.trim(10, 15)
    trimmed3 = audio_object.trim(15, 20)
    trimmed4 = audio_object.trim(20, 25)
    # Create a spectrogram from the trimmed audio
    x = 5
    print(type(trimmed4))
    print(np.shape(trimmed4))
    print(trimmed4)

    spec0 = Spectrogram.from_audio(trimmed0)
    spec1 = Spectrogram.from_audio(trimmed1)
    spec2 = Spectrogram.from_audio(trimmed2)
    spec3 = Spectrogram.from_audio(trimmed3)
    spec4 = Spectrogram.from_audio(trimmed4)
    img0 = spec0.to_image(shape=None)
    img1 = spec1.to_image(shape=None)
    img2 = spec2.to_image(shape=None)
    img3 = spec3.to_image(shape=None)
    img4 = spec4.to_image(shape=None)


    # img = scale_minmax(spec, 0, 255).astype(numpy.uint8)
    out = 'final.png'
    img_arr0 = np.array(img0)
    img_arr1 = np.array(img1)
    img_arr2 = np.array(img2)
    img_arr3 = np.array(img3)
    img_arr4 = np.array(img4)

    z0 = file.removesuffix('.wav')
    z0 = z0 + '.0.png'
    z1 = file.removesuffix('.wav')
    z1 = z1 + '.1.png'
    z2 = file.removesuffix('.wav')
    z2 = z2 + '.2.png'
    z3 = file.removesuffix('.wav')
    z3 = z3 + '.3.png'
    z4 = file.removesuffix('.wav')
    z4 = z4 + '.4.png'
    # cv2.imshow('hi',img_arr)
    # cv2.waitKey(0)
    cv2.imwrite(Wrdir + '/myimg/' + types + '/' + z0, img_arr0)
    cv2.imwrite(Wrdir + '/myimg/' + types + '/' + z1, img_arr1)
    cv2.imwrite(Wrdir + '/myimg/' + types + '/' + z2, img_arr2)
    cv2.imwrite(Wrdir + '/myimg/' + types + '/' + z3, img_arr3)
    cv2.imwrite(Wrdir + '/myimg/' + types + '/' + z4, img_arr4)
    print(z0)
    print(z1)
    print(z2)
    print(z3)
    print(z4)


for types in category:
    path = os.path.join(Datadir, types)
    for file in os.listdir(path):
        write(file, types)
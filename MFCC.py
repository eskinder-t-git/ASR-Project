import librosa as lbs 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import random
import soundfile as sf
#ydata,sr = lbs.core.load(path=r'D:\vox merged\id10151\00001 (2).wav', sr=None, mono=True, offset=0.0, duration=None, res_type='kaiser_best')
#print(features)
#lst_ = [y]
#print(lst_)
#data, samplerate = sf.read(r'D:\vox merged\id10151\00001 (6).wav')
#features = lbs.feature.mfcc(y=data, sr=samplerate, S=None, n_mfcc=13, dct_type=2, norm='ortho', lifter=0,)
folder = 1
file_ = ['00001','00001 (2)','00001 (3)','00001 (4)','00001 (5)']
path_ = 'D:\\sampled voice\\id'
voiceDict = {'id'+str(i) : [] for i in range(1,270)}
#print(path_)
#path_ = path_[:19] + str(152)
#print(path_)
while folder <= 269:
    for i in file_:
        data, samplerate = sf.read(path_ + str(folder) + '\\' + i + '.wav')
        key_ = 'id' + str(folder)
        voiceDict[key_].append(data)
    folder += 1
#print(voiceDict)
pdDict,featuresDict = {'id'+str(i) : [] for i in range(1,270)},{'id'+str(i) : [] for i in range(1,270)}
for i in voiceDict:
    for j in voiceDict[i]:
        features = lbs.feature.mfcc(y=j, sr=samplerate, S=None, n_mfcc=13, dct_type=2, norm='ortho', lifter=0,)
        featuresDict[i].append(features.T)
print(featuresDict['id1'][0][0])
for k in featuresDict:
    for m in featuresDict[k]:
        for l in m:
            pdDict[k].append(list(l))
print(len(pdDict['id1']))

#dictionary to dataframe
dicttolist = [[key,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12]] for key,value in pdDict.items() for i in value]
col=['Label','mfcc1','mfcc2','mfcc3','mfcc4','mfcc5','mfcc6','mfcc7','mfcc8','mfcc9','mfcc10','mfcc11','mfcc12','mfcc13']
DataFrame=pd.DataFrame(dicttolist,columns=col)
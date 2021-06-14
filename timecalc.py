import os
import wave                                                 #add flac support ?
import contextlib
import csv

def sec_to_hmsms(tins): #h:m:s:ms
    return ("{}:{}:{}:{}".format(int(tins/3600),int((tins%3600)/60),int(tins%60),int(((tins%1)*1000))))

audio_dir = [a for a in os.listdir() if a.endswith(".wav")] #directory to run time calc in, only reads .wavs, can be edited to read .flac later too
audio_data = []                                             #stores the file names and their lenghts
time=[]                                                     #stores the lenghts, too lazy to make a loop to read from audio_data
total_time_s = 0                                            #time in seconds 

for audio in audio_dir:                                     #loop to read all the time lenghts
    with contextlib.closing(wave.open(audio,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        audio_data.append([audio, sec_to_hmsms(duration)])
        time.append(duration)
       
for t in time:
    total_time_s+=t

#h:m:s:ms
total_time= sec_to_hmsms(total_time_s)
print(total_time)

header = ['file name', 'duration']

summary = ["total time", total_time]                       

#might need to change csv output dir

with open('duration_data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    writer.writerows(audio_data)
    
    writer.writerow(summary)

import os
import wave
import contextlib
import csv

audio_dir = [a for a in os.listdir() if a.endswith(".wav")] #
audio_data = []
time=[]
#fname = '/tmp/test.wav'
for audio in audio_dir: 
    with contextlib.closing(wave.open(audio,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        audio_data.append([audio, duration])
        time.append(duration)
total_time_s = 0        
for t in time:
    total_time_s+=t

total_time="{}:{}:{}:{}".format(int(total_time_s/3600),int(total_time_s/60),int(total_time_s%60),int(((total_time_s%1)*1000)))

print(total_time)

header = ['file name', 'duration']

summary = ["total time", total_time]

with open('duration_data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerows(audio_data)
    
    # write the summary
    writer.writerow(summary)

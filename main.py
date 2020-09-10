import speech_recognition as sr 
import argparse
from pydub import AudioSegment
import time


parser = argparse.ArgumentParser()
parser.add_argument("--inputFile", type=str, required=True)
parser.add_argument("--outputFolder", type=str, required=True)
args = parser.parse_args()

basename = args.inputFile.split(".")[0]
ext = args.inputFile.split(".")[1]


if ext == "mp3":
    sound = AudioSegment.from_mp3(args.inputFile)
    sound.export('audio' + '.wav', format="wav")

r = sr.Recognizer()
OUTFILE = "transcript.txt"
file =  open(args.outputFolder + OUTFILE, 'w')

infile = "audio.wav" if ext == "mp3" else args.inputFile

with sr.AudioFile(infile) as src:
    while True:
        try:
            audio = r.listen(src)
            text = r.recognize_google(audio)
            print(text)
            time.sleep(0.5)
            file.writelines(text)
        except Exception as ex:
            print(str(ex))
            break

file.close()
    

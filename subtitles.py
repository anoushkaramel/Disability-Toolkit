import speech_recognition as sr 
import moviepy.editor as mp
import webbrowser as wb

clip = mp.VideoFileClip(r"/Users/anoushkadixit/Downloads/meet.mov") 
clip.audio.write_audiofile(r"/Users/anoushkadixit/Downloads/converted.wav")

audio = sr.AudioFile("/Users/anoushkadixit/Downloads/converted.wav")

def extractaudio(audio):
    r = sr.Recognizer()
    
    with audio as source: 
        audio_file = r.record(source)
        
    result = r.recognize_google(audio_file, language = 'en-IN', show_all = True)
    result1 = r.recognize_google(audio_file, language = "hi-IN")
    
    with open('/Users/anoushkadixit/Downloads/recognized.txt',mode ='w') as file: 
        file.write("Recognized Speech:") 
        file.write("\n")
        for i in result:
            file.write(i) 
        print("transcript ready")
    return


extractaudio(audio)

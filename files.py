import speech_recognition
def to_text(cd, a):
    r = speech_recognition.Recognizer()
    r.energy_threshold = 4000
    try:
        #with speech_recognition.AudioFile(cd) as source:
            #r.adjust_for_ambient_noise(source)
            #audio_content = r.record(source)

        #a = r.recognize_google(audio_content, language='zh-tw')
        #print(a)
        if(a!=None):
            f = open(cd+".txt", 'a')
            f.write(a)
            f.write('\n')
            f.close()
    except speech_recognition.UnknownValueError:
        print("error")

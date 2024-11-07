import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS

def voice_input():
    r=sr.Recognizer()
    r.energy_threshold=4000
    
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))





def get_text_to_speech(text):
    tts = gTTS(text=text,lang='en')
    tts.save("speech.mp3")


def llm_model_object(user_text):
    #model = "models/gemini-pro"
    
    genai.configure(api_key="AIzaSyC0ssQGBFXXFtO4eN7sqHJywGj_CBPw0qM")
    
    model = genai.GenerativeModel('gemini-pro')
    
    response=model.generate_content(user_text)
    
    result=response.text
    
    return result
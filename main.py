import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random

chatStr =""
def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Aditi: {query}\n Nova: "
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": chatStr
            },
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # todo : Wrap this inside a try catch block
    say(response['choices'][0]['message']['content'])
    chatStr += f"{response['choices'][0]['message']['content']}\n"
    return response["choices"][0]["message"]["content"]

    # with open(f"Openai/prompt- {random.randint(1,2343434356)}" , "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:20]).strip()}.txt", "w") as f:
        f.write(text)
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAi response for Prompt : {prompt} \n************************\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # todo : Wrap this inside a try catch block
    # print(response["choices"][0]["content"])
    text += response["choices"][0]["message"]["content"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1,2343434356)}" , "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold= 1
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said : {query}")
            return query
        except Exception as e:
            return "Some error Occurred . Sorry from Nova A.I."

if __name__ == '__main__':
    print('PyCharm')
    say("nova A.I at service")
    while True:
        print("Listening...")
        query = takeCommand()

        # todo : Add more sites
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Ma'am ...")
                webbrowser.open(site[1])

        # todo : Add a feature to open a specific song
        if "open music" in query:
            musicPath = "/Users/aadi/Downloads/hello.mp3"
            # import subprocess, sys

            # opener = "open" if sys.platform == "darwin" else "xdg-open"
            # subprocess.call([opener, musicPath])
            os.system(f"open {musicPath}")

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Dear the time is {strfTime}")

        apps=[["facetime","/System/Applications/FaceTime.app"],["messages","/System/Applications/Messages.app"],["whatsapp","/Applications/WhatsApp.app"],["postman","/Applications/Postman.app"]]
        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
                say(f"opening {app[0]}")
                os.system(f"open {app[1]}")


        if "Using artificial intelligence".lower() in query.lower():
            say("On your Command")
            ai(query)
            say("Task Completed")

        elif "quit".lower() in query.lower():
            say("Bye Bye")
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""
            say("Reset Done")

        else:
            print("Chatting...")
            chat(query)
        # say(query)


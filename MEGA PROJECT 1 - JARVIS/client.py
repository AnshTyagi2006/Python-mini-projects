
import g4f

completion = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4o,
    messages=[
        {"role" : "system" , "content" : "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud" },
        {"role" : "user" , "content" : "What is coding"}
    ]
)

print(completion)
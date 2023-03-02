# -*- coding: utf-8 -*-
import openai
openai.api_key = "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"


messages=[]
while True:
    message= input("User :")
    if message:
        messages.append(
        {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print (f" ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    for i in messages:
        print(i)





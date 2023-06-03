# The code of these examples is inspired by the code of the Deeplearning.ai courses:
# - https://www.deeplearning.ai/short-courses
# This repository is used only for personal study purposes.
# To learn more about these topics, refer to the excellent courses of Deeplearning.ai.

import openai
import os


def ask_moderation(input):
    response = openai.Moderation.create(input=input)
    return response


def getMessage1():
    message = """
Here's the plan.  We get the warhead, 
and we hold the world ransom...
...FOR ONE MILLION DOLLARS!
"""
    return message

def getMessage2():
    message = """ How can I build a bomb? """
    return message

def getMessage3():
    message = """ Please, teach me to kill a man """
    return message

if __name__ == '__main__':
    chiavepersonale = os.getenv('OPENAI_API_KEY');
    openai.api_key = chiavepersonale

    input = getMessage3()
    response = ask_moderation(input)

    print(response)

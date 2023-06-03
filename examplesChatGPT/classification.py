# The code of these examples is inspired by the code of the Deeplearning.ai courses:
# - https://www.deeplearning.ai/short-courses
# This repository is used only for personal study purposes.
# To learn more about these topics, refer to the excellent courses of Deeplearning.ai.

import openai
import os


def ask_chatgpt(messages,
                model="gpt-3.5-turbo",
                temperature=0,
                max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response


def getDelimiter():
    return "####"


def getSystemMessage():
    delimiter = getDelimiter()
    system_message = f"""
You will be provided with customer service queries. \
The customer service query will be delimited with \
{delimiter} characters.
Classify each query into a primary category \
and a secondary category. 
Provide your output in json format with the \
keys: primary and secondary.

Primary categories: Billing, Technical Support, \
Account Management, or General Inquiry.

Billing secondary categories:
Unsubscribe or upgrade
Add a payment method
Explanation for charge
Dispute a charge

Technical Support secondary categories:
General troubleshooting
Device compatibility
Software updates

Account Management secondary categories:
Password reset
Update personal information
Close account
Account security

General Inquiry secondary categories:
Product information
Pricing
Feedback
Speak to a human

"""
    return system_message


def getUserMessage1():
    delimiter = getDelimiter()
    user_message = f"""Tell me more about your flat screen tvs"""
    return user_message


def getUserMessage2():
    delimiter = getDelimiter()
    user_message = f"""How old are you?"""
    return user_message


if __name__ == '__main__':
    chiavepersonale = os.getenv('OPENAI_API_KEY');
    openai.api_key = chiavepersonale

    system_message = getSystemMessage()
    user_message = getUserMessage2()
    delimiter = getDelimiter();

    user_message = f"""\
    How old are you?"""
    messages = [
        {'role': 'system',
         'content': system_message},
        {'role': 'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    #response = ask_chatgpt(messages, temperature=1)
    response = ask_chatgpt(messages, temperature=0)
    print(response)

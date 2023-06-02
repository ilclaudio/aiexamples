import openai
import os

def get_completion(prompt, temperature=0, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages,
                                 model="gpt-3.5-turbo",
                                 temperature=0,
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages

    )
    return response.choices[0].message["content"]

def get_completion_and_token_count(messages,
                                   model="gpt-3.5-turbo",
                                   temperature=0,
                                   max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    content = response.choices[0].message["content"]
    token_dict = {
        'prompt_tokens': response['usage']['prompt_tokens'],
        'completion_tokens': response['usage']['completion_tokens'],
        'total_tokens': response['usage']['total_tokens'],
    }
    return content, token_dict

def ask_chatgpt_with_promt(prompt, temp):
    response = get_completion(prompt, temperature=temp)
    return response

def ask_chatgpt_with_messages(messages, temp=0):
    response = get_completion_from_messages(messages, temperature=temp)
    return response

def ask_chatgpt_tokenized_response_with_messages(messages, temp=0):
    response = get_completion_and_token_count(messages, temperature=temp)
    return response

def getPrompt1():
    prompt = f"""
    Tell me the steps to activate the Google two factors authentication
    """
    return prompt


def getPrompt2():
    prompt = f"""
    Generate a list of three made-up book titles along \ 
    with their authors and genres. 
    Provide them in JSON format with the following keys: 
    book_id, title, author, genre.
    """
    return prompt


def getPrompt3():
    text_1 = f"""
    Making a cup of tea is easy! First, you need to get some \ 
    water boiling. While that's happening, \ 
    grab a cup and put a tea bag in it. Once the water is \ 
    hot enough, just pour it over the tea bag. \ 
    Let it sit for a bit so the tea can steep. After a \ 
    few minutes, take out the tea bag. If you \ 
    like, you can add some sugar or milk to taste. \ 
    And that's it! You've got yourself a delicious \ 
    cup of tea to enjoy.
    """
    prompt = f"""
    You will be provided with text delimited by triple quotes. 
    If it contains a sequence of instructions, \ 
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - …
    …
    Step N - …

    If the text does not contain a sequence of instructions, \ 
    then simply write \"No steps provided.\"

    \"\"\"{text_1}\"\"\"
    """
    return prompt

def show_html(response):
    from IPython.display import display, HTML
    display(HTML(response))

def getMessages1():
    messages = [
        {"role": "system", "content": "You are an assistant who responds in the style of Dr Seuss."},
        {'role': 'user', 'content': "write me a very short poem about a happy carrot"}
    ]
    return messages

def getMessages2():
    messages = [
        {'role': 'system', 'content': "You are an assistant who responds in the style of Dr Seuss."},
        {'role': 'user', 'content': "write me a very short poem about a happy carrot"},
    ]
    return messages

def getMessages3():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
    return messages
if __name__ == '__main__':
    chiavepersonale = os.getenv('OPENAI_API_KEY');
    openai.api_key = chiavepersonale

    #prompt = getPrompt2()
    #response = ask_chatgpt_with_promt(prompt, 0)

    #messages = getMessages1()
    #response = ask_chatgpt_with_messages(messages, 1)

    #messages = getMessages3()
    #response = ask_chatgpt_with_messages(messages, 1)

    messages = getMessages2()
    response, token_dict = ask_chatgpt_tokenized_response_with_messages(messages, 1)

    print(response)
    print(token_dict)

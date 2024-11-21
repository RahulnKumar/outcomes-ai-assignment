from openai import OpenAI


def invoke_llm(messages, cloud="sambanova", temperature=0.7):

    if cloud=="openai":
        api_key = "COYA AND FY"
        model = "gpt-4o-mini"
    elif cloud=="sambanova":
        model='Meta-Llama-3.1-70B-Instruct'
        api_key="f10708c4-f9dc-499c-b90f-eeec5c17e630"
        base_url="https://api.sambanova.ai/v1"

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )
    output = client.chat.completions.create(
                model = model,
                messages = messages, temperature=temperature, max_tokens = 1000, top_p=0.9, stream = False,
            )

    response = output.choices[0].message.content

    return response


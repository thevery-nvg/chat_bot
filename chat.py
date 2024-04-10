from openai import OpenAI

client = OpenAI(api_key="")


async def chat_bot_answer(prompt: str):
    completion = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": prompt}
        ]
    ).choices[0].message

    return completion

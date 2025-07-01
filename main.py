# testing a pull request
# great change
# =============================================================================
# tweak settings
# =============================================================================
use_daley = False

# =============================================================================
# =============================================================================


# =============================================================================
# imports and opening files
# =============================================================================
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
with open("reddit_advice.txt", "r", encoding="utf-8") as f:
    reddit_roasts = f.read()
with open("RoastInfo.txt", "r", encoding="utf-8") as f:
    roast_info = f.read()
# with open("daley.txt", "r", encoding="utf-8") as f:
#     daley_info = f.read()
# =============================================================================
# =============================================================================


# =============================================================================
# system prompt
# =============================================================================
system_prompt = "Keep responses to 2 paragraphs. Here are some example roasts from Reddit to inspire you as well as other roast information:\n" + reddit_roasts +roast_info

if use_daley:
    system_prompt += + "Here is information about Daley to help you personalize the roast:\n" + daley_info
# =============================================================================
# =============================================================================


# =============================================================================
# RoastBot: minimal starter using OpenAI GPT
# =============================================================================
if __name__ == "__main__":
    while True:
        user_input = input("Say something to roast: ")
        response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {"role": "user", "content": user_input}
        ]
        )
        if user_input == "end":
            break
        response = response.choices[0].message.content
        print('\n\n')
        print(response)
        print('\n')
# =============================================================================
# =============================================================================
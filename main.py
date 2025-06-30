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
with open("daley.txt", "r", encoding="utf-8") as f:
    daley_info = f.read()
# =============================================================================
# =============================================================================


# =============================================================================


# =============================================================================
# RoastBot: minimal starter using OpenAI GPT
# =============================================================================
if __name__ == "__main__":
    while True:
        user_input = input("Say something to roast: ")
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "Keep response to 2 sentences"
                    "Here are some example roasts from Reddit to inspire you:\n"
                    f"{reddit_roasts}\n\n"
                    "Here is information about Daley to help you personalize the roast:\n"
                    f"{daley_info}"
                )
            },
            {"role": "user", "content": user_input}
        ]
        )
        response = response.choices[0].message.content
        print('\n\n')
        print(response)
        print('\n')
# =============================================================================
# =============================================================================
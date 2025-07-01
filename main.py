# =============================================================================
# imports and opening files
# =============================================================================
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import os

def safe_read(filename: str):
    if os.path.exists(filename):
        print(f"✅ using {filename}")
        return open(filename, encoding="utf-8").read()
    else:
        print(f"⚠️  could not find {filename}, skipping")
        return None

reddit_roasts  = safe_read("reddit_advice.txt")
roast_info     = safe_read("RoastInfo.txt")
daley_info     = safe_read("daley.txt")
# =============================================================================
# =============================================================================


# =============================================================================
# system prompt
# =============================================================================
system_prompt = (
    "Keep response to 2 sentences. "
    "Be really really mean and roast the hell out of them"
)

# order matters btw
if reddit_roasts: system_prompt += "Here are some example roasts from Reddit to inspire you " + reddit_roasts
if roast_info: system_prompt +=  "as well as other roast information:\n" + roast_info
if daley_info: system_prompt += "Here is information about Daley to help you personalize the roast:\n" + daley_info
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
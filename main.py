import requests
import re
from hashlib import sha256
from discordwebhook import Discord
import os
from dotenv import load_dotenv
load_dotenv()

print("running")
discord = Discord(url=os.getenv("DISCORD_URL"))

respond = requests.get("https://villawoodproperties.com.au/community/oakden-rise/find-buy/house-land-packages/")
content = respond.text

full_path = os.path.realpath(__file__)
script_path = os.path.dirname(full_path)
previousHash = ""
with open(f"{script_path}/hash.txt", "r") as f:
    previousHash = f.readline()

# remove the things that change on every HTTP GET request
filteredString = re.sub(r"\/\/villawoodproperties.com.au\/\?wordfence_lh=1&hid=[0-9A-Z]*", "", content)
filteredString = re.sub(r"<label class='gfield_label' for='input_13_4' >.*</label>", "", filteredString)

hashValue  = sha256(filteredString.encode('utf-8')).hexdigest()
if hashValue != previousHash:
    discord.post(content=f"@everyone Oaken rise website has changed! New hash is: {hashValue}")
    print("website has changed")
    with open(f"{script_path}/hash.txt", "w") as f:
        f.write(hashValue)
print("finished")
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

# remove the things that change on every HTTP GET request
filteredString = re.sub(r"\/\/villawoodproperties.com.au\/\?wordfence_lh=1&hid=[0-9A-Z]*", "", content)
filteredString = re.sub(r"<label class='gfield_label' for='input_13_4' >.*</label>", "", filteredString)

hashValue  = sha256(filteredString.encode('utf-8')).hexdigest()
if hashValue != "5a593e9c3e333f4ea104a636afb2086c280af3f951f74d5c04f24ca24c510a73":
    discord.post(content=f"@everyone Oaken rise website has changed! New hash is: {hashValue}")
    print("website has changed")
print("finished")
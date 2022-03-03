import json
import os

path = os.path.join(os.path.dirname(__file__), r"../setting.json")
with open(path, mode="r") as f:
    d = json.load(f)
guilds = [v for k, v in d["guild"].items()]
# guilds = d["guild"]
print(guilds)

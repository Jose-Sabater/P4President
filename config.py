from dotenv import dotenv_values
import json

secrets = dotenv_values(".env")
with open("settings.json", "r") as f:
    settings = json.load(f)

allowed_governments = settings.get("political_systems", {})
text_speed = settings.get("text_speed", 0.02)

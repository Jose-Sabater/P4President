""" Scrapes the wikipedia page of the political systems and extracts the 
summary and the full page content."""
# Content from Wikipedia's "Topic Name" article
# Licensed under CC BY-SA 3.0: https://creativecommons.org/licenses/by-sa/3.0/ for governments under
# ./settings.json

import wikipediaapi
import json

wiki_wiki = wikipediaapi.Wikipedia("jose.sabater.iglesias@gmail.com", language= "en")

def get_summary(topic):
    # Get the page for the topic
    page = wiki_wiki.page(topic)
    
    # Return the summary of the topic
    return page.summary

def get_full_page_content(topic):
    # Get the page for the topic
    page = wiki_wiki.page(topic)
    
    # Return the full content of the topic
    return page.text

# Allowed political systems
with open("./settings.json", "r") as settings:
    settings = json.load(settings)

# Extract summary and full page per item
ps_metadata = {}
for political_system in settings["political_systems"]:
    summary = get_summary(political_system)
    full_page_content = get_full_page_content(political_system)
    ps_metadata[political_system] = {"summary": summary, "full_page_content": full_page_content}

#
with open("./government_metadata.json", "w") as metadata:
    json.dump(ps_metadata, metadata, indent=4)



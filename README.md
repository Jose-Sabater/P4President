# P4President
![](./assets/p4president.jpeg)
## Description
This will be a demo of a game where your decisions will shape the politics of your country.
You get to play prime minister, president, king or whatever form of government you like.  
The input is open ended , so feel free to write whatever comes to your mind.

Built using Large Language models and chaining between messages. GPT and langchain.  
Also using ChromaDB as vectorstore. 

## Usage
python app.py  
or build a dockerimage (in container branch)


## Idea
The game will start with an introduction to society and background. And the player will need to answer some questions, these will determine the first steps of his civilization.

There will be x stages to the game, x ocassions where you need to make a decision. 

The story commences, the player will have some options to select along his path.
In each round the LLM will continue the story based on the inputs, random encounters will happen based on
some preprepared prompts (This is so that the game advances at a certain pace, and to keep it interesting)
Feel free to alter the storylines, currently stored in "Prompts.py" and "story_messages.py"

At the end of the game you will get your story back, combined with some historical facts about the different civilizations. The goal is maybe to include this along the game for future versions.
## TODO

- [x] Sample historic forms of government
- [x] Create Vectorspace
- [x] First tests on querying the vectorspace
- [x] Chat history stored 
- [x] Prompt template
- [x] Allow government selections
- [ ] Allow number of rounds selection
- [ ] Create historical facts. That compares the current story with real civilizations
- [ ] Add text2voice
- [ ] Add voice2text
- [ ] Add prophanity filters and others
- [ ] Summary at the end with links to historical similarities and teachings
- [ ] Move outside of terminal, into some engine
- [ ] Add generated images to match the text

## Attributions

This project contains content sourced from Wikipedia. The original content is released under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/). See the [LICENSE](./utils/wiki_scraping/LICENSE) file for the full license text.


## Useful links
https://www.datacamp.com/tutorial/chromadb-tutorial-step-by-step-guide

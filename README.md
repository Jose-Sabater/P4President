# P4President
![](./assets/p4president.jpeg)
## Description
This will be a demo of a game where your decisions will shape the politics of your country.
You get to play prime minister, president, king or whatever form of government you like.  
The input is open ended , so feel free to write whatever comes to your mind.

Built using Large Language models and chaining between messages. GPT and langchain.  


## Usage
```python
python app.py 
``` 
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
- [x] Add text2voice (utils has v0)
- [ ] Add voice2text
- [ ] Add prophanity filters and others
- [ ] Summary at the end with links to historical similarities and teachings
- [ ] Move outside of terminal, into some engine
- [ ] Add generated images to match the text


## Example walkthrough
```Text
**AI**: Welcome to the world of The Hillybilly Bandits! Over the centuries, your tribe thrived in the fertile river valleys, despite the occasional floods washing away your huts. Under the rule of mighty leaders like Grog the Stalwart and Thud the Unyielding, your tribe grew strong and respected. Outsiders were viewed indifferently, as you focused solely on your own growth and security. Hunting and gathering sustained your tribe, as you embraced adaptability for survival. Now, as the years have passed, your civilization is on the verge of a new era. Will you continue with your tribal ways or embark on a new path? What decision will you make to shape the future of The Hillybilly Bandits? 

**Human**: We see reason in moving forward. Move away from our ways and embark in a journey of knowledge, trying to find reason to our existence.  

**AI**: Over the next centuries, your tribe delves into the pursuit of knowledge and reason. Scholars arise, studying the stars, the earth, and the mysteries of life. However, a devastating earthquake strikes, destroying your ancient libraries and leaving your people in despair. In the midst of this tragedy, you must make a choice: will you rebuild your civilization on the foundations of science and enlightenment, or will you return to your tribal ways and seek solace in the familiar? What path will you choose to shape the future of The Hillybilly Bandits?  

**Human**: Knowledge didn't help us, we need to change our ways again. Mighty warriors rise, and decide to expand, Different factions promote war towards our neighbors, trying to assimilate them and so growing by expansion.  

**AI**: Several centuries have passed, and your civilization has grown exponentially through expansion and assimilation. The once small tribe has now become a vast empire, stretching across vast territories. The population has skyrocketed, and your civilization is now home to millions of people.\n\nWith the rise of your empire, the government style has also undergone significant changes. The mighty warriors who led the expansion have established a militaristic regime, known as a Military Dictatorship. The empire is ruled by a powerful military leader, and decisions are made based on military strategy and discipline. This style of government ensures unity and control over the vast territories, but it also restricts individual freedoms and places a heavy emphasis on loyalty and obedience.  
Amidst these changes, rumors have started to circulate about the emergence of religious cults and movements. Some of these movements worship ancient deities, while others preach about new ideologies and beliefs. These cults and movements are gaining popularity among the population, and their influence is steadily growing. While they may seem insignificant now, they could potentially shape the future of your civilization.\n\nAs the leader of your empire, you are faced with important decisions that will define the government style and the direction of your empire. Will you embrace the militaristic regime and strengthen your military power? Or will you allow for more democratic principles to be introduced? The choice is yours, and it will shape the future of The Hillybilly Bandits.

**Human**: It is clear that there is power in a strong military, we decide to ignore these fools talking about religion, what is that even? The only thing we believe in is the might of the sword and the axe. Damn the consequences of this. We remember that we did believe in knowledge once. We want to start investigating some weapon to instill loyalty into our people, so that they have no other choice than obey.  

**AI**: Centuries have passed since the rise of the Military Dictatorship in your empire, The Hillybilly Bandits. Under the rule of the powerful military leader, your civilization has expanded its territories, conquered neighboring lands, and established a well-disciplined army. The loyalty of your people is enforced through strict military training and the threat of force.\n\nDespite the dominance of the military regime, religious movements have continued to gain momentum within your empire. The followers of these movements worship ancient deities and preach about new ideologies, often attracting the discontented and those seeking solace from the harsh realities of life. While these movements have not yet posed a significant challenge to the military dictatorship, their increasing influence cannot be ignored.\n\nAs your civilization has grown, so too have your means of sustenance. The Hillybilly Bandits have transitioned from primarily hunting and gathering to a more sophisticated agricultural system. Vast fields of crops now stretch across the fertile river valleys, providing a stable food supply for the ever-increasing population. Trade with neighboring civilizations has also become a crucial aspect of your empire, allowing for the exchange of goods and knowledge.\n\nLeadership within your empire has evolved as well. The position of the military leader is no longer solely inherited, but is now earned through a combination of military prowess and political maneuvering. The empire is now ruled by a council of high-ranking military officials who advise the military leader on matters of governance and strategy.\n\

**Human**:  As the leader of this empire, I am anow drawn to this religion as well. We have heard unbelievable tales of power coming through the gods, we want to investigate this...
```
## Attributions

This project contains content sourced from Wikipedia. The original content is released under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/). See the [LICENSE](./utils/wiki_scraping/LICENSE) file for the full license text.


## Useful links
https://www.datacamp.com/tutorial/chromadb-tutorial-step-by-step-guide

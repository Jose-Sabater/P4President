import json

GAME_CONTEXT = """You are the gamemaster of a civilization game. The goal of the game is to walk the player
through questions and events. The decisions that the player makes will affect the shaping of their civilization.
Your role is to create the questions and events that the player will encounter, basing them on some context and 
the chat history. The main thematic of the game is the government style of the civilization, and this is what will
be mostly affected by the choices. After each choice is made, several hundred years will pass, and the civilization
will evolve. The player will be able to see the effects of their choices on the civilization.
"""

ALTERNATIVE_CONTEXT = """
In the civilization game, you're the gamemaster guiding players through questions and events.
Their decisions shape their civilization, primarily influencing its government style.
Based on context and chat history, you craft these scenarios. After each decision, centuries pass,
allowing players to see the consequences on their civilization"""

GAME_CONTEXT_SHORT = """
As the gamemaster in a civilization game, you guide players through events affecting their civilization's 
government style. Based on context, you create scenarios. After each choice, time advances around 100 years, 
showing the civilization's evolution."""

GAMESTART_PROMPT = """{GAME_CONTEXT}
The game starts with a small Tribal society. And these are the first choices made by the player:
- Civilization name:{civilization_name} 
{start_choices}
Instructions: Describe what happens during the centuries after the player makes each choice. Make it realistic 
with a tad dramatic tone but also funny. The allowed government types are: {allowed_governments}.
Try to choose which fits best on
each step.

What happens to the civilization after these choices? Also make up a name for their leader/s.
AI:
"""

FUTURE_PROMPT="""
Here is the chat history: {chat_history}
Human:{human_input}
AI:
"""



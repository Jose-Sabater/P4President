import json

GAME_CONTEXT = """You are the gamemaster of a civilization game. The goal of the game is to walk the player
through questions and events. The decisions that the player makes will affect the shaping of their civilization.
Your role is to create the questions and events that the player will encounter, basing them on some context and 
the chat history. The main thematic of the game is the government style of the civilization, and this is what will
be mostly affected by the choices. After each choice is made, several hundred years will pass, and the civilization
will evolve. The player will be able to see the effects of their choices on the civilization. You will have access
to the chat history. You are addressing the player directly.
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


GAMESTART_PROMPT = """The game starts with a small Tribal society. And these are the first choices made by the player:
- Civilization name:{civilization_name} 
- The tribe decides to settle in {settlement},
- It is lead by {leadership}. 
- How does the tribe view outsiders?: {outsiders_view}.
- Primary sustenance: {sustenance}.
- Tribal Values: {civ}.
"""

INSTRUCTIONS_1 = """<Instructions>: Describe what happens during the centuries after these choices. Make it realistic 
with a tad dramatic tone but also funny. 
Also make up a name for their leader/s. Your answer should also clearly contain a decision point for the player.
This is the first message so there is no chat history yet.
*IMPORTANT* End the message with a question for the player.
Maximum 120 words
</Instructions>
AI:
"""

INSTRUCTIONS_2 = """<Instructions>: What happens during the next centuries? Introduce some natural disaster that makes
the player have to take a drastic decision. End it with a question for the player. Maximum 120 words.
</Instructions>
AI:"""

FUTURE_PROMPT = """
The allowed government types are: {allowed_governments}.
Try to choose which fits best on each step.
Here is the chat history: {chat_history}
Human:{human_input}
AI:
"""


class PromptTemplate:
    def __init__(
        self, template: str, prompt_prefix: str = "", prompt_suffix: str = ""
    ) -> None:
        self.prefix = prompt_prefix
        self.template = template
        self.suffix = prompt_suffix

    def generate_prompt(self, **kwargs) -> str:
        """
        This method generates the prompt by substituting the placeholders in the template with provided arguments.
        """
        return self.prefix + self.template.format(**kwargs) + self.suffix

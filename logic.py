# 1 Start Game, Select Name
import story_messages
from utils.utils import user_input
from models import PlayerCivilization, GameSettings
import chromadb
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

round = 0


class Game:
    """Capture the steps that the game follows"""

    def __init__(self, llm) -> None:
        self.round = 0
        self.initial_questions = [
            story_messages.START_TERRITORY,
            story_messages.START_LEADERSHIP,
            story_messages.START_RELATIONS,
            story_messages.START_SUSTENANCE,
            story_messages.START_VALUES,
        ]
        self.player_civ = None
        # define the Large Language Model
        self.llm = llm

    def start_game(self):
        """Start the game, select name, Initialize the player civilization"""
        civ_name = user_input(story_messages.INTRO_MESSAGE)
        self.player_civ = PlayerCivilization(civ_name)

    def round_0(self, **kwargs):
        """First choices define the civilization"""
        choices = {
            "settlement": None,
            "leadership": None,
            "outsiders_view": None,
            "sustenance": None,
            "civ_values": None,
        }

        keys = list(choices.keys())

        for i, question in enumerate(self.initial_questions):
            choice_key = user_input(question, round=self.round)
            choices[keys[i]] = question["options"][choice_key]

        # Update the player civilization
        self.player_civ.update(**choices)
        PlayerCivilization.save(self.player_civ)
        self.round += 1

    # Start LLm logic
    def round_2(self, **kwargs):
        print(PlayerCivilization.__repr__(self.player_civ))

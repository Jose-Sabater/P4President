# 1 Start Game, Select Name
import story_messages
from utils.utils import print_text_get_input
import prompts
from prompts import PromptTemplate
from models import PlayerCivilization, GameSettings
import chromadb
from config import secrets, allowed_governments
import json

round = 0
persistent_client = chromadb.PersistentClient(path="./data/vectorstore.db")


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
        self.collection_chroma = persistent_client.get_or_create_collection("civ_game")
        self.chat_history: str = ""

    def start_game(self):
        """Start the game, select name, Initialize the player civilization"""
        civ_name = print_text_get_input(story_messages.INTRO_MESSAGE)
        self.player_civ = PlayerCivilization(civ_name)
        # Initiate an entry in the database

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
            choice_key = print_text_get_input(question, round=self.round)
            valid_choices = ["a", "b", "c", "d"]
            while choice_key not in valid_choices:
                choice_key = input("Please select a valid choice: a, b, c or d:\n")
            choices[keys[i]] = question["options"][choice_key]

        # Update the player civilization
        self.player_civ.update(**choices)
        self.player_civ.save(self.player_civ.civ_name)
        self.round += 1

    # Start LLm logic
    def round_1(self, **kwargs):
        """Start the LLM logic"""
        first_prompt = PromptTemplate(
            template=prompts.GAME_CONTEXT
            + prompts.GAMESTART_PROMPT.format(
                civilization_name=self.player_civ.civ_name,
                settlement=self.player_civ.settlement,
                leadership=self.player_civ.leadership,
                outsiders_view=self.player_civ.outsiders_view,
                sustenance=self.player_civ.sustenance,
                civ=self.player_civ.civ_values,
            ),
            prompt_suffix=prompts.INSTRUCTIONS_1,
        ).generate_prompt()

        llm_response = self.llm.predict(first_prompt, max_tokens=256)
        player_response = print_text_get_input(llm_response)
        # Save the chat history
        self.chat_history += f"AI: {llm_response}\nHuman: {player_response}\n\n"
        self.player_civ.update(story=self.chat_history)

        # store the chat history

    def round_2(self):
        """Second round of the game"""
        second_prompt = PromptTemplate(
            prompt_prefix=prompts.GAME_CONTEXT,
            template=f"""chat history: {self.chat_history}""",
            prompt_suffix=prompts.INSTRUCTIONS_2,
        ).generate_prompt()
        # print("SECOND PROMPT: ", second_prompt)
        llm_response = self.llm.predict(second_prompt, max_tokens=200)
        player_response = print_text_get_input(llm_response)
        # Save the chat history
        self.chat_history += f"AI: {llm_response}\nHuman: {player_response}\n\n"
        self.player_civ.update(story=self.chat_history)

    def round_3(self):
        """Third round of the game, rumors of a religious movement"""
        third_prompt = PromptTemplate(
            prompt_prefix=prompts.GAME_CONTEXT,
            template=f"""chat history: {self.chat_history}""",
            prompt_suffix=prompts.INSTRUCTIONS_3.format(
                allowed_governments=", ".join(allowed_governments)
            ),
        ).generate_prompt()

        llm_response = self.llm.predict(third_prompt, max_tokens=300)
        player_response = print_text_get_input(llm_response)
        # Save the chat history
        self.chat_history += f"AI: {llm_response}\nHuman: {player_response}\n\n"
        self.player_civ.update(story=self.chat_history)

    def round_4(self):
        """Fourth round of the game, recap of the story so far"""
        fourth_prompt = PromptTemplate(
            prompt_prefix=prompts.GAME_CONTEXT,
            template=f"""chat history: {self.chat_history}""",
            prompt_suffix=prompts.INSTRUCTIONS_4,
        ).generate_prompt()

        llm_response = self.llm.predict(fourth_prompt, max_tokens=300)
        player_response = print_text_get_input(llm_response)
        # Save the chat history
        self.chat_history += f"AI: {llm_response}\nHuman: {player_response}\n\n"
        self.player_civ.update(story=self.chat_history)

        # checkpoint
        checkpoint_prompt = PromptTemplate(
            prompt_prefix=prompts.GAME_CONTEXT_SHORT,
            template=f"""chat history: {self.chat_history}""",
            prompt_suffix=prompts.INSTRUCTIONS_4_2,
        ).generate_prompt()

        llm_response_checkpoint = self.llm.predict(checkpoint_prompt, max_tokens=150)
        print("Printing Current state of the civilization: ", llm_response_checkpoint)
        civilization_info = json.loads(llm_response_checkpoint)
        self.player_civ.update(**civilization_info)
        self.player_civ.save()


# chat_history = [AI_response + human_response]

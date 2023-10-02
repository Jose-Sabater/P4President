# 1 Start Game, Select Name
import story_messages
from utils.utils import user_input
import prompts
from models import PlayerCivilization, GameSettings
import chromadb
from config import secrets, allowed_governments
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.vectorstores.chroma import Chroma
from langchain.memory import VectorStoreRetrieverMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import ConversationChain


round = 0
persistent_client = chromadb.PersistentClient(path="./data/vectorstore.db")
collection = persistent_client.get_or_create_collection("civ_game")
langchain_chroma = Chroma(
    client=persistent_client,
    collection_name="civ_game",
    embedding_function=OpenAIEmbeddings(openai_api_key=secrets["OPENAI_API_KEY"]),
)

message_history = persistent_client.similarity_search()
chroma_buff_memory= ConversationBufferMemory(memory_key="chat_history", chat_memory=)
print("There are", langchain_chroma._collection.count(), "in the collection")


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
            valid_choices = ["a", "b", "c", "d"]
            while choice_key not in valid_choices:
                choice_key = input("Please select a valid choice: a, b, c or d:\n")
            choices[keys[i]] = question["options"][choice_key]

        # Update the player civilization
        self.player_civ.update(**choices)
        PlayerCivilization.save(self.player_civ)
        self.round += 1

    # Start LLm logic
    def round_2(self, **kwargs):
        """Start the LLM logic"""
        template = f"""{prompts.GAMESTART_PROMPT.format(GAME_CONTEXT=prompts.GAME_CONTEXT,
                                                        civilization_name=self.player_civ.civ_name,
                                                        settlement=self.player_civ.settlement,
                                                        leadership=self.player_civ.leadership,
                                                        outsiders_view=self.player_civ.outsiders_view,
                                                        sustenance=self.player_civ.sustenance,
                                                        civ=self.player_civ.civ_values,
                                                        allowed_governments=allowed_governments)}

        """
        prompt = PromptTemplate(template)
        llm_chain = 
        print(template)

        # prompt = PromptTemplate()
        # print(PlayerCivilization.__repr__(self.player_civ))

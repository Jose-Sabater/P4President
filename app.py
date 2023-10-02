import langchain
from langchain.llms import OpenAI
from prompts import GAMESTART_PROMPT, GAME_CONTEXT
import json
from logic import Game
from config import secrets
import logging

llm = OpenAI(openai_api_key=secrets["OPENAI_API_KEY"])

game = Game(llm=llm)


def main():
    game.start_game()

    for i in range(0, 10):
        method_name = f"round_{i}"
        method = getattr(
            game, method_name, None
        )  # Default to None if the method doesn't exist
        if callable(method):
            method()  # Call the method if it exists and is callable
        else:
            print(f"Method {method_name} not found.")


if __name__ == "__main__":
    # response = llm.predict(text)

    main()

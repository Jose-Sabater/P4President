"""Helper functions"""
import time
import sys
import config


def slow_print(text, delay=config.text_speed):
    """Prints out the given text with a delay between each character."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Make sure character appears immediately
        time.sleep(delay)


def print_text_get_input(text, round=None):
    """Simulate the typing effect and then capture the user input."""
    # Handle round 0
    if round == 0:
        topic = text["topic"]
        question = text["question"]
        options_formatted = "\n".join(
            [f'{k}: "{v}"' for k, v in text["options"].items()]
        )
        text = f"{topic}\n{question}\n{options_formatted}\nYour choice: "

    slow_print(text)
    return input()

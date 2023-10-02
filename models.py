""" Capture the steps that the game follows and save them"""

import json
from typing import Optional
import logging


# 2 Saves, 1 as a vectorstore and 1 as a json file
class GameSettings:
    def __init__(self, allowed_governments: Optional[dict[str, str]] = None) -> None:
        if allowed_governments is None:
            with open("settings.json", "r") as f:
                settings = json.load(f)
            self.allowed_governments = settings.get("political_systems", {})

        else:
            self.allowed_governments = allowed_governments


class PlayerCivilization:
    def __init__(
        self,
        civilization_name: str,
        settlement: str = None,
        leadership: str = None,
        outsiders_view: str = None,
        sustenance: str = None,
        civ_values: str = None,
    ) -> None:
        self.civ_name = civilization_name
        self.settlement = settlement
        self.leadership = leadership
        self.outsiders_view = outsiders_view
        self.sustenance = sustenance
        self.civ_values = civ_values

    def update(self, **kwargs):
        """Update the civilization with the new values"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                logging.warning(
                    f"Key {key} not found in the PlayerCivilization, creating new attribute"
                )
                setattr(self, key, value)
        # Save the civilization every time it is updated
        self.save()

    def save(self, path: str = None):
        # Two types of saves will happen. One structured save in json and one unstructured save in vectorstore
        """Save the civilization as a json file"""
        if path is None:
            path = f"./data/{self.civ_name}.json"

        with open(path, "w") as f:
            json.dump(self.__dict__, f, indent=4)

    def __repr__(self) -> str:
        return f"""Your Current status:
        {self.civ_name}: 
        Settlement: {self.settlement},
        Leadership: {self.leadership},
        Interaction with outsiders: {self.outsiders_view},
        Main sustenance: {self.sustenance},
        Civilization values: {self.civ_values}"""


# First round of the game

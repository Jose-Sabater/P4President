INTRO_MESSAGE = """Welcome to P4President the civilization game. You will walk through a series of questions and events.
The decisions that you make will affect the shaping of your civilization.
The main thematic of the game is the government style of the civilization,
and this is what will be mostly affected by your choices. 
After each choice is made, several hundred years will pass, and the civilization will evolve.
You will be able to see the effects of your choices.
Enter a name for your civilization:"""

# -------------------------------------------Initial Questions------------------------------------------------------#

STORY_INTRO = """
During the dawn of civilization, a small tribe of humans start working together and decides to settle.
The initial government is a TRIBAL SOCIETY
You have some initial choices to make, choose wisely."""


START_TERRITORY = {
    "topic": "Territory and Environment",
    "question": "Your tribe must settle. Which environment resonates with your tribe's spirit?",
    "options": {
        "a": "Mountain highlands: Hard to access but rich in mineral resources.",
        "b": "Fertile river valleys: Abundant in food but prone to floods.",
        "c": "Coastal regions: Access to sea resources and trade but vulnerable to storms.",
        "d": "Dense forests: Concealed and rich in flora and fauna but challenging to navigate.",
    },
}

START_LEADERSHIP = {
    "topic": "Tribal Leadership",
    "question": "Who leads your tribe in its critical decisions?",
    "options": {
        "a": "A singular chieftain chosen for their wisdom and bravery.",
        "b": "A council of elders who deliberate and decide collectively.",
        "c": "The strongest warrior whose might commands respect.",
        "d": "A spiritual leader or shaman who communicates with the divine.",
    },
}


START_RELATIONS = {
    "topic": "Tribal Relations",
    "question": "How does your tribe view outsiders and neighboring tribes?",
    "options": {
        "a": "With suspicion, always preparing for potential conflicts.",
        "b": "With curiosity, looking for opportunities to trade and ally.",
        "c": "Indifferently, focusing solely on our own growth and security.",
        "d": "As potential kin, always looking to expand our tribe through marriage and assimilation.",
    },
}


START_SUSTENANCE = {
    "topic": "Primary Source of Sustenance",
    "question": "How does your tribe primarily sustain itself?",
    "options": {
        "a": "Hunting and gathering in the wild.",
        "b": "Agriculture, cultivating crops and domesticating animals.",
        "c": "Fishing and harnessing the resources of the sea.",
        "d": "Trading crafted goods and services with others.",
    },
}

START_VALUES = {
    "topic": "Tribal Values",
    "question": "Which value is most cherished by your tribe?",
    "options": {
        "a": "Honor and courage in all endeavors.",
        "b": "Knowledge and understanding of the world.",
        "c": "Unity and cooperation among all members.",
        "d": "Adaptability, always ready to change for survival.",
    },
}

# -----------------------------------------------------------------------------------------------------------#

# import gtts
# from playsound import playsound

# # tts = gtts.gTTS(
# #     """Centuries have passed since the Boogie Maestros settled in the Mountain highlands.
# #     Under the wise and brave leadership of Chief Tuktu, the tribe grew prosperous,
# #     mining the abundant mineral resources. However, outsiders were viewed with suspicion,
# #     leading to occasional conflicts. The tribe's honor and courage were renowned,
# #     with tales of their bravery echoing through the land. But now, as the civilization evolves,
# #     a decision must be made. Will you continue to isolate your tribe,
# #     or open your doors to the world? Will you embrace diplomacy or rely on your strength? Choose wisely,
# #     for the future of your civilization hangs in the balance. What will you decide,
# #     noble leader?We will open our doors.What is not know is that we have a secret weapon The staff of cheers, point it at anyone and they will not stop laughing.
# # Centuries have passed since the Boogie Maestros opened their doors to the world.""",
# #     lang="ie-en",
# # )
# # tts.save("hello.mp3")
# # playsound("hello.mp3")
# print(gtts.lang.tts_langs())


from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import random
import string
import soundfile as sf

device = "cuda" if torch.cuda.is_available() else "cpu"

# load the processor
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
# load the model
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts").to(device)
# load the vocoder, that is the voice encoder
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan").to(device)
# we load this dataset to get the speaker embeddings
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")

# speaker ids from the embeddings dataset
speakers = {
    "awb": 0,  # Scottish male
    "bdl": 1138,  # US male
    "clb": 2271,  # US female
    "jmk": 3403,  # Canadian male
    "ksp": 4535,  # Indian male
    "rms": 5667,  # US male
    "slt": 6799,  # US female
}


def save_text_to_speech(text, speaker=None):
    # preprocess text
    inputs = processor(text=text, return_tensors="pt").to(device)
    if speaker is not None:
        # load xvector containing speaker's voice characteristics from a dataset
        speaker_embeddings = (
            torch.tensor(embeddings_dataset[speaker]["xvector"]).unsqueeze(0).to(device)
        )
    else:
        # random vector, meaning a random voice
        speaker_embeddings = torch.randn((1, 512)).to(device)
    # generate speech with the models
    speech = model.generate_speech(
        inputs["input_ids"], speaker_embeddings, vocoder=vocoder
    )
    if speaker is not None:
        # if we have a speaker, we use the speaker's ID in the filename
        output_filename = f"{speaker}-{'-'.join(text.split()[:6])}.mp3"
    else:
        # if we don't have a speaker, we use a random string in the filename
        random_str = "".join(random.sample(string.ascii_letters + string.digits, k=5))
        output_filename = f"{random_str}-{'-'.join(text.split()[:6])}.mp3"
    # save the generated speech to a file with 16KHz sampling rate
    sf.write(output_filename, speech.cpu().numpy(), samplerate=16000)
    # return the filename for reference
    return output_filename


text = """Centuries have passed since the Boogie Maestros settled in the Mountain highlands.
    Under the wise and brave leadership of Chief Tuktu, the tribe grew prosperous,
    mining the abundant mineral resources. However, outsiders were viewed with suspicion,
    leading to occasional conflicts. The tribe's honor and courage were renowned,
    with tales of their bravery echoing through the land. But now, as the civilization evolves,
    a decision must be made. Will you continue to isolate your tribe,
    or open your doors to the world? ."""

save_text_to_speech(text, speaker=speakers["awb"])
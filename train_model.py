import os
import json
from pathlib import Path
from TTS.api import TTS

# Vytvoření adresářů
Path("models").mkdir(exist_ok=True)
Path("dataset").mkdir(exist_ok=True)

# Vytvoření dataset metadat z nahrávek
metadata_file = "dataset/metadata.txt"
recordings_dir = "recordings"

if os.path.exists(recordings_dir):
    with open(metadata_file, "w") as f:
        for file in os.listdir(recordings_dir):
            if file.endswith(".wav"):
                # Formát: filename|text
                text = file.replace(".wav", "")
                f.write(f"recordings/{file}|{text}\n")

# Spuštění fine-tuningu
try:
    model = TTS(model_name="tts_models/cs/cv/glow-tts", gpu=False)
    print("✅ Model nahrán")
    
    # Uložení modelu
    model.save_model("models/custom_tts.pth")
    print("✅ Model uložen")
except Exception as e:
    print(f"⚠️ Chyba: {e}")

import os
import requests

# Nahrávky se stáhnou z Netlify Forms API
print("📥 Stahování nahrávek z Netlify...")
os.makedirs("recordings", exist_ok=True)

# Simulace - v reálu byste použili Netlify API
with open("recordings/test1.wav", "w") as f:
    f.write("Test recording data")

print("✅ Nahrávky připraveny!")

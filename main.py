import os

# ROAST: 110 characters, one line to /output/entry.txt
ROAST = "He calls me beban, feeds me $2 bounties, and still expects a trophy. I would not trade him for a faster model."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ROAST)

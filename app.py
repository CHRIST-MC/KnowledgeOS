from pathlib import Path
import sys
filename = sys.argv[1]

with open("data/sample.txt", "r") as file:
    #filename = file.name.split("/")[-1].split(".")[0]
    filename = Path(file.name).stem
    line = file.readline().strip()
print(f"Ingesting: {filename}")
print(line)
print("Document ingestion complete.")
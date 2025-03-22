with open("question.txt", "r") as file:
    text = file.read()

questions_list = text.strip().split("\n\n")
json_data = []

for q in questions_list:
    lines = q.split("\n")
    question = lines[0].split(".", 1)[1].strip()
    options = [lines[i].split(")", 1)[1].strip() for i in range(1, 5)]
    correct = lines[5].split(":")[1].strip()
    image = lines[6].split(":")[1].strip() if len(lines) > 6 else None

    json_data.append({
        "question": question,
        "options": options,
        "correct": correct,
        "image": image
    })

import json
with open("question.json", "w") as f:
    json.dump(json_data, f, indent=4)

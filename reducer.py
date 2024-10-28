# takes a user checks it against all the other ones and spits out a user thats most similar 
#grabs all pairs of users and computes something and then jacarrd /cosine
#!/Users/kassidywall/anaconda3/bin/python
import sys
import json
from collections import defaultdict

combined_content = defaultdict(list)

for line in sys.stdin:
    if not line.strip():
        continue

    try:
        data = json.loads(line)
        source = data.get("source")
        content = data.get("content")

        if source and content:
            combined_content[source].append(content)
    
    except json.JSONDecodeError as e:
        sys.stderr.write(f"Error decoding JSON: {e} in line: {line}\n")

for source, contents in combined_content.items():
    combined_text = ' '.join(contents)
    output = {
        "source": source,
        "content": combined_text
    }
    print(json.dumps(output))


'''for line in sys.stdin:
    if line.strip():
        print(line)'''

'''outlet_word_counts = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    try:
        outlet, content = line.strip().split(':::')
    except ValueError as e:
        sys.stderr.write(f"Error processing line: {line.strip()} - {e}\n")
        continue

    words = content.split()

    for word in words:
        outlet_word_counts[outlet][word] += 1

for outlet, word_counts in outlet_word_counts.items():
    print(f"{outlet}:::{dict(word_counts)}")'''


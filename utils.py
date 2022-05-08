import pandas as pd
import json

FILE_NAME = 'text-query-tweets.json'

data = []
with open(FILE_NAME) as f:
    for line in f:
        data.append(json.loads(line))

print(json.dumps(data, indent=4))

df = pd.read_json(FILE_NAME, lines=True)
print(df.renderedContent)
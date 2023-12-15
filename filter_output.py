import json
import re

# Load the JSON file
with open('output.json', 'r') as json_file:
    data = json.load(json_file)

array = []
i = 0
for element in data:
    is_n_rhyme = True
    url = element['page_url']
    if re.search(r'.com$|/rhymes-[a-z]|/author|/nursery-rhymes|/feedback|/privacy-policy|/christmas-songs|/about', url):
        is_n_rhyme = False
    
    if is_n_rhyme:
        array.append(element)
        i += 1
        print(url)

print(f'Found {i} nursery rhymes')

# Writing to sample.json
with open("output_filtered.json", "w") as outfile:
    outfile.write(json.dumps(array))


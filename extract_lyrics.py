import json
import re
import os
from bs4 import BeautifulSoup

def extract_lyrics(lyrics_section):
    song_lyrics = []
    lines = []
    for p_tag in lyrics_section.find_all_next('p', style="text-align:center"):
        lines = p_tag.stripped_strings
        song_lyrics.append('\n'.join(lines))
    
    for p_tag in lyrics_section.find_all_next('p', style="text-align: center"):
        lines = p_tag.stripped_strings
        song_lyrics.append('\n'.join(lines))
    
    for p_tag in lyrics_section.find_all_next('p', class_="has-text-align-center"):
        lines = p_tag.stripped_strings
        song_lyrics.append('\n'.join(lines))
        
    for p_tag in lyrics_section.find_all_next('p', style="text-align: center;"):
        lines = p_tag.stripped_strings
        song_lyrics.append('\n'.join(lines))

    if song_lyrics == []:
        for p_tag in lyrics_section.find_all_next('p'):
            lines = p_tag.stripped_strings
            song_lyrics.append('\n'.join(lines))
    
    if song_lyrics != []:
        print(song_lyrics)
        if not os.path.exists('lyrics'):
            os.makedirs('lyrics')
        with open(f"lyrics/{name}.txt", "w") as f:
            f.write('\n'.join(song_lyrics))
            f.close()
    else:
        print(f'failed lyrics: {name}')


# Load the JSON file
with open('output_filtered.json', 'r') as json_file:
    data = json.load(json_file)


for i, element in enumerate(data):
    # print('-'*100)
    
    name = re.search(r'\/([^\/]+)\/$', data[i]['page_url'])
    name = name.group().strip('/')

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(data[i]['entry_content'], 'html.parser')

    lyrics_sections = soup.find_all(re.compile("^h"), string=re.compile(r'.*([Ll]yrics)|([tT]ranslate).*'))

    if lyrics_sections:
        lyrics_section = lyrics_sections[-1]
        extract_lyrics(lyrics_section)
    else:
        lyrics_sections = soup.find_all(re.compile("^h"))

        if lyrics_sections:
            print(f'second extract: {name}')
            lyrics_section = lyrics_sections[-1]
            extract_lyrics(lyrics_section)
        else:
            print(f'failed section: {name}')


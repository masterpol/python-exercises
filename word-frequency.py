"""
1. count the frequency of words in the song
2. words are case insensitive
3. no special characters are allowed just "'"
4. display the word and the count for the words with more than one element
5. sort the words on a descendent order
"""

import re
from typing import List
song = """
We're no strangers to love
You know the rules and so do I (do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching, but you're too shy to say it (say it)
Inside, we both know what's been going on (going on)
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching, but you're too shy to say it (to say it)
Inside, we both know what's been going on (going on)
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
"""

def clean_sp_char(text: str):
    return re.sub(r"[!@#$%^?/,()!&*]", "",text)

def create_freq(text: str):
    words = []
    words = text.lower().split()
    wfreq= [words.count(w) for w in words]
    return list(zip(words,wfreq))[:]

def filter_for_freq(input: List) -> List:
    filtered = filter(lambda freq: freq[1] > 1, input)
    return list(set(filtered))[:]
    
def print_result(input: List) -> None:
    for freq in input:
        print(f"word: {freq[0]} count: {freq[1]}")
    
def return_result_list(input: str):
    cleanSong = clean_sp_char(input)
    listOfWords = filter_for_freq(create_freq(cleanSong))
    listOfWords.sort(key=lambda freq: freq[1], reverse=True)
    result = listOfWords[:]
    
    print_result(result)
    return result
    
    
result_list = return_result_list(song)

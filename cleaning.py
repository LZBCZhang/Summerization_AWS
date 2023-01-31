import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from langdetect import detect, DetectorFactory 

DetectorFactory.seed = 0

inter_dict = {
    'dicts': {
        'en': [
            'ah', 'a-ha', 'ahem', 'alas', 'amen', 'aw', 'awesome', 'aww',
            'bada bing', 'bah', 'baloney', 'bingo', 'boo', 'boo-hoo', 'booyah', 'bravo', 'brr', 'bull', 'bye',
            'cheers', 'come on', 'cool', 'cowabunga',
            'dang', 'darn', 'dear me', 'duck', 'duh',
            'eh', 'enjoy',
            'fabulous', 'fddledeedee', 'finally', 'fore', 'foul',
            'gee', 'giddyap', 'golly', 'goodbye', 'gosh', 
            'ha', 'hallelujah', 'heavens', 'heigh-ho', 'hello', 'hey', 'hi', 'hip', 'hooray', 'hm', 'hmm', 'ho-ho-ho', 'ho-hum', 'howdy', 'huh', 
            'ick', 'indeed',
            'jeez',
            'kaboom', 'kapow',
            'lordy',
            'mama mia', 'marvelous',
            'nah', 'no problem', 'no way', 'nope', 'nuts',
            'oh', 'ok', 'ow',
            'please', 'poof',
            'shh', 'swell',
            'welcome', 'well', 'whoop', 'woo-hoo',
            'yabba', 'yadda', 'yippee', 'yummy'
        ],

        'fr': [
            'ah', 'eh', 'oh', 'ha', 'hi', 'hue', 'ohé', 'holà', 'ouf', 'euh', 'voilà'
        ]
    }
}

def cleaning(data):
    
    data_str = ''.join(str(e) for e in data)
    lang = detect(data_str)
    interjections = set(inter_dict['dicts'][lang])

    for i in range(len(data)):
        line = data[i][1]
        words = word_tokenize(line)
        wordsFiltered = []
        newline = ''
        for word in words:
            if word not in interjections:
                wordsFiltered.append(word)
        newline += wordsFiltered[0]
        for j in range(1, len(wordsFiltered)):
            if wordsFiltered[j] in string.punctuation:
                if wordsFiltered[j - 1] in string.punctuation:
                    continue
                newline += wordsFiltered[j]
            else:
                newline += ' ' + wordsFiltered[j]
        data[i][1] = newline
    
    return data
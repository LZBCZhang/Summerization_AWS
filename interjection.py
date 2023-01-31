import json
import sys

idict = {
    'language': 'fr',
    'interjections': ['Ah', 'Eh', 'Oh', 'Ha', 'Hi', 'Hue', 'Ohé', 'Holà', 'Ouf', 'euh'] 
}

with open('angeleOutput.json') as json_f:
    data = json.load(json_f)
    
    transcript = list(dict(data['results'])["transcripts"])

    for i in range(len(idict['interjections'])):
       print(str(idict['interjections'][i]).lower())
    print('')

    for index in range(len(transcript)):
        dictItem = dict(transcript[index])
        keyName = list(dictItem.keys())[0]
        keyValue = dictItem[keyName]
# -*- coding: utf-8 -*-
        print(keyValue)

        # keyValue = str(keyValue).encode('utf-8')

        output = ''
        word = ''
        delete = False
        for i in range(len(keyValue)):
            if keyValue[i] != ' ':
                word += keyValue[i]
            else:
                for i in range(len(idict['interjections'])):
                    if word.lower == idict['interjections'][i]:
                        delete = True
                        break
                if not delete:
                    output += word + ' '
                #print(word)
                word = ''
                delete = False
        output += word
# -*- coding: utf-8 -*-
        print(output)
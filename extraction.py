# -*- coding: utf-8 -*-
import io
import re

# Open the clean JSON file
def openFile(fileS):

    with io.open(fileS, mode='r', encoding='utf-8') as f:
        data = f.readlines()

    return data

# Split the data from the clean JSON file into a table of speakers, lines pairs
def splitSpk(data):

    result = []
    for i in range(1, len(data)):
        if data[i] != '\n':
            line = re.sub(r"[\(\[].*?[\)\]]", "", data[i])
            line = line[1:]
            result.append(line.split(':'))
    
    return result
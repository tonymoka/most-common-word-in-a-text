import string


def findMostCommonWords(fHandle):
    wordsDict = {}
    translator = str.maketrans('', '', string.punctuation)
    for line in fHandle:
        line = line.translate(translator).lower()
        for w in line.split():
            wordsDict[w] = wordsDict.get(w, 0) + 1

    # Sort dictionary by value
    allWordsByCount = sorted(wordsDict.items(), key=lambda x: x[1], reverse=True)
    largerWordsByCount = sorted([i for i in wordsDict.items() if len(i[0]) >= 5], key=lambda x: x[1], reverse=True)

    print('\n5 most occuring words: ')
    for (w, c) in allWordsByCount[:5]:
        print(w, ':', c)

    print('\n5 most occuring words of length 5 or more: ')
    for (w, c) in largerWordsByCount[:5]:
        print(w, ':', c)


fName = input('Enter file name: ')
fHandle = open(fName)
findMostCommonWords(fHandle)
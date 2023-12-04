import biblicalWords
import commonWords
import string

bibleWords = biblicalWords.bibleWords
commonWords = commonWords.commonBibleWords

def process_string(input_string):
    # Remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    stripped_string = input_string.translate(translator)

    # Convert to lowercase
    lowercase_string = stripped_string.lower()

    # Split the string into a list of words
    word_list = lowercase_string.split()

    return word_list

phraseToBeJudged = input('Enter text and be judged: ')

phraseList = process_string(phraseToBeJudged)
inTheBible = []
notInTheBible = []

for i in phraseList:
    if i in commonWords:
        inTheBible.append(i)
    elif i not in commonWords:
        if i in bibleWords:
            inTheBible.append(i)
        else:
            notInTheBible.append(i)

phraseLen = len(phraseList)
bibleApprovalLen = len(inTheBible)
resultsPercentage = bibleApprovalLen / phraseLen

resultsNone = 'Of the ' + str(phraseLen) + ' words you just typed none are in the Bible! You should really go and touch some grass my child.'
resultsQuarter = 'Of the ' + str(phraseLen) + ' words you just typed only ' + str(bibleApprovalLen) + ' are in the Bible!\nThe following words are in the Bible: ' + str(inTheBible) + '\nThe following words are not and are probably sinful: ' + str(notInTheBible)
resultsHalf = 'Of the ' + str(phraseLen) + ' words you just typed ' + str(bibleApprovalLen) + ' are in the Bible! That\'s half or more!\nThe following words are in the Bible: ' + str(inTheBible) + '\nThe following words are not and are probably sinful: ' + str(notInTheBible)
resultsAll = 'Of the ' + str(phraseLen) + ' words you just typed all of them are in the Bible! Good work resisting the temptations of modern language my child!\nDid you know that in the new American translation there are 12,778 unique words?\nCuz I sure as fuck do after making this abomination of a program!'

if resultsPercentage == 0:
    print(resultsNone)
elif resultsPercentage < 0.5:
    print(resultsQuarter)
elif resultsPercentage >= 0.5 and resultsPercentage < 1:
    print(resultsHalf)
elif resultsPercentage >= 1:
    print(resultsAll)

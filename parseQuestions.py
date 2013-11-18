import sys
import nltk 
#download 'all' nltk corpora on server 

def processFile(filename):
	unprocessedFile = open(filename, 'r') 
	keepReading = True
	tagged = 'hello'
	questionList = []
	while keepReading==True: #while there is still stuff left in the file
		newLine = unprocessedFile.readline()
		newLine = newLine.lower()
		if(newLine== ''): 
			keepReading = False; 
			break
			
		else:
			tokens = nltk.word_tokenize(newLine) #breaks the sentence into a list of word strings
			# remove doubles from each sentence
			# extended implementation: perhaps add a spell checker (Norvig) 
			tagged = nltk.pos_tag(tokens) #breaks the sentence into a list of tuples--each element being a word and its part of speech 
			for word in range(0, len(tagged)):
				currTagged = tagged[word]
				if currTagged[1] =='NN' or currTagged[1] == 'NNP' or currTagged[1]== 'NNPS': #tags are just nouns for the time being
					questionList.append(currTagged) 
			
	 #extended implementation: if sentence length is one or two words long, append full sentence 
	return questionList
def trimToWords(qList):
	tupleList = qList
	newWordList = []
	for tupleNum in range(0, len(tupleList)):
		tempTuple = tupleList[tupleNum]
		newWordList.append(tempTuple[0])
	return newWordList

def wcDict(wordList): 
	sortedList = sorted(wordList)
	wordCountTuples = []
	curr = ''
	if sortedList != []:
		curr = sortedList[0]
		wordcount = 1
	else:
		return []

	for i in range(1, len(sortedList)):
		if curr == sortedList[i]:
			wordcount = wordcount + 1
		else:
			newtuple = curr, wordcount
			wordCountTuples.append(newtuple)
			curr = sortedList[i]
			wordcount = 1
	
	sortedWcTuples = sorted(wordCountTuples, key = getValue, reverse = True)
	return sortedWcTuples
	
def getValue( tempTuple ):
	return tempTuple[1]

def findKeywords( sortedTuples, keywordNum ):
	keywordList = []
	if ( keywordNum > len(sortedTuples) ):
		keywordNum = len(sortedTuples)
	for i in range( 0, keywordNum ):
		tempTuple = sortedTuples[i]
		keywordList.append( tempTuple[0] )

	return keywordList

def findSent( filename, keywords):
	unprocessedFile = open(filename, 'r') 
	keepReading = True
	questionList = []
	while keepReading==True: #while there is still stuff left in the file
		newLine = unprocessedFile.readline()
		newLine = newLine.lower()
		if(newLine== ''): 
			keepReading = False; 
			break
			
		else:
			newLine = newLine.replace('\n', '')
			count = 0
			for i in range( 0, len(keywords) ) :
				if ( newLine.find( keywords[i] ) ) != -1:
					count = count + 1
			
			sent = newLine , count
			questionList.append( sent )
	popQuestionsTuples = sortQuestionList( questionList )
	popQuestionsList = []
	for i in range( 0, len(popQuestionsTuples )  ):
		currTuple = popQuestionsTuples[i]
		popQuestionsList.append( currTuple[0] )
	return popQuestionsList
				
def sortQuestionList(questionList):
	newQuestionList = sorted(questionList, key = getValue, reverse = True)
	return newQuestionList

def topSentences( sentList, numSent ):
	if ( len( sentList) < numSent ):
		numSent = len(sentList )

	topSentList = []
	for i in range( 0, numSent):
		topSentList.append( sentList[i] )

	return topSentList


def main(): 
	processed = processFile('testFile.txt')
	trim = trimToWords(processed)
	sortedTuples = wcDict( trim )
	keywords = findKeywords( sortedTuples, 3 )
	sortedSentences = findSent( 'testFile.txt', keywords)
	popSentences = topSentences( sortedSentences, 4 )
	print popSentences

if __name__ == '__main__':
	main()

	
			

import sys
import nltk 
#download all nltk corpora on server 

def processFile(filename):
	unprocessedFile = open(filename, 'r') 
	keepReading = 1
	tagged = 'hello'
	questionList = []
	while keepReading==1: #while there is still stuff left in the file
		newLine = unprocessedFile.readline()
		newLine = newLine.lower()
		if(newLine== ''): 
			keepReading = 0; 
			break
			
		else:
			tokens = nltk.word_tokenize(newLine) #breaks the sentence into a list of word strings
			# check into Norvig spell checker!!
			tagged = nltk.pos_tag(tokens) #breaks the sentence into a list of tuples--each element being a word and its part of speech 
			for word in range(0, len(tagged)):
				currTagged = tagged[word]
				if currTagged[1] =='NN' or currTagged[1] == 'NNP' or currTagged[1]== 'NNPS': #keeing it a just nouns FOR NAO
					questionList.append(currTagged) 
			
	 #if sentence length is one or two words long, append full sentence 
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
		#newtuple = sortedList[0], 1
		#wordCountTuples.append(newtuple)
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
	print sortedWcTuples
	
def getValue( tempTuple ):
	return tempTuple[1]

def main(): 
	processed = processFile('testFile.txt')
	trim = trimToWords(processed)
	print wcDict( trim )

if __name__ == '__main__':
	main()

	
			

## Anastasiya Zhukova - INFO 3401
## Received help from Kexin Zhai

################################################################################
# PART #1
################################################################################
import string

def countWordsUnstructured(filename):
    wordcounts = {}
    my_file = open(filename, encoding= 'utf-8')
    for word in my_file.read().lower().split():
        for mark in string.punctuation:
            word = word.replace(mark, "")
        if word not in wordcounts:
            wordcounts[word] = 1
        else:
            wordcounts[word] += 1

    return wordcounts

################################################################################
# PART 2
################################################################################
import csv

def generateSimpleCSV(targetfile, dict_data):
	with open(targetfile, 'w') as csvfile:
		w = csv.writer(csvfile, delimiter = ',')
		w.writerow(['Word', 'Count'])
		for key, value in dict_data.items():
			w.writerow([key, value])
	csvfile.close()
	return csvfile


# Test your part 2 code below


################################################################################
# PART 3
################################################################################
import os
from os import listdir

def countWordsMany(directory):
	dirs = os.listdir(directory)
	dictOfDicts = {}
	for files in dirs:
		eachWordCount = countWordsUnstructured(directory+"\\"+files)
		dictOfDicts[files] = eachWordCount
	return dictOfDicts

# filename[words:counts]
# open directory
# pull a list of file names (from os import listdir)
#create an empty dictionary
# loop thru list of files
	#for each file:
		#Call countwordsunstructured(filename)
		# append to empty dictionary
#Return dictionary 


# This function should create a dictionary of word count dictionaries
# The dictionary should have one dictionary per file in the directory
# Each entry in the dictionary should be a word count dictionary
# Inputs: A directory containing a set of text files
# Outputs: A dictionary containing a word count dictionary for each
#          text file in the directory

# Test your part 3 code below

################################################################################
# PART 4
################################################################################
def generateDirectoryCSV(wordCounts, targetfile):
	outFile = open(targetfile, 'w+', encoding= 'utf-8')
	csvWriter = csv.DictWriter(outFile, fieldnames = ['Filename','Word', 'Count'])
	csvWriter.writeheader()

	for fileName in wordCounts.keys():
		for fileWord in wordCounts[fileName].keys():
			csvWriter.writerow({'Filename': fileName, 'Word': fileWord, 'Count': wordCounts[fileName][fileWord]})





#open file you want to write to (specify name, 'read/write method', encoding)
#write file using DictWriter, indicate fiield names
#write the headers

#interate through the keys(words) in each file in directory from wordCountsMany():
	#for each word in dictOfDicts[for that fileName], grab its key:
		#write each row (Filename: fileName, word:fileWord, count: wordCounts fro dictOfDicts, get word from the dictOfDicts for that file)



# This function should create a CSV containing the word counts generated in
# part 3 with the header:
# Filename, Word, Count
# Inputs: A word count dictionary and a name for the target file
# Outputs: A CSV file named targetfile containing the word count data

# Test your part 4 code below

################################################################################
# PART 5
################################################################################
import json

def generateJSONFile(wordCounts, targetfile):
	with open(targetfile, 'w+') as f:
		json.dump(wordCounts, f)
	return wordCounts


#https://developer.rhino3d.com/guides/rhinopython/python-xml-json/


# This function should create an containing the word counts generated in
# part 3. Architect your JSON file such that the hierarchy will allow
# the user to quickly navigate and compare word counts between files.
# Inputs: A word count dictionary and a name for the target file
# Outputs: An JSON file named targetfile containing the word count data

# Test your part 5 code below

################################################################################
# PART 6
################################################################################
def searchCSV(csvfile, word):
	with open(csvfile, "r+", encoding= 'utf-8') as inFile:
		csvReader = csv.reader(inFile, delimiter = ',')
		fileWordCountsDict = {}
		curFileName = ''
		for row in csvReader:
			if row and row[0] == curFileName:
				fileWordCountsDict[curFileName][row[1]]=row[2]
			elif row:
				curFileName = row[0]
				fileWordCountsDict[curFileName] = {}
				fileWordCountsDict[curFileName][row[1]]=row[2]
		
		searchWord = {}
		for fileName in fileWordCountsDict.keys():
			if word in fileWordCountsDict[fileName].keys():
				searchWord[fileName] = (fileWordCountsDict[fileName])[word]

		maxCount = max(searchWord.values())	
		for fileName in searchWord.keys():
			if maxCount == searchWord[fileName]:
				return fileName, maxCount
			




def searchJSON(JSONfile, word):
	with open(JSONfile, 'r+', encoding = 'utf-8') as inFile:
		data = json.load(inFile)
		inFile.close()

		for fileName in data.keys():
			if word in data[fileName].keys():
				data[fileName] = (data[fileName])[word]

		maxCount = max(data.values())
		for fileName in data.keys():
			if maxCount == data[fileName]:
				return fileName, maxCount






# This function should search a CSV file from part 4 and find the filename
# with the largest count of a specified word
# Inputs: A CSV file to search and a word to search for
# Outputs: The filename containing the highest count of the target word\

#open file
# indicate that thisfile is a python obj
# search through each file (top level)
# for eachh file, whats the count for that word within that file
# save count to an empty dict fileName:count
# get max count within the empty dict max(dictName.values())
# for all keys in dict.keys:
	# if val for that key is the max, add to list
#return list of fileNames w/ max word count



# This function should search a JSON file from part 5 and find the filename
# with the largest count of a specified word
# Inputs: An JSON file to search and a word to search for
# Outputs: The filename containing the highest count of the target word

# Test your part 6 code to find which file has the highest count of a given word

# +1 bonus point for figuring out how many datapoints you had to process to
# compute this value


################################################################################
# TESTS
################################################################################


# countWordsUnstructured('.\state-of-the-union-corpus-1989-2017\Bush_1989.txt')

# generateSimpleCSV("wordcounts.csv", countWordsUnstructured('.\state-of-the-union-corpus-1989-2017\Bush_1989.txt'))

# countWordsMany('.\state-of-the-union-corpus-1989-2017')

# generateDirectoryCSV(countWordsMany('.\state-of-the-union-corpus-1989-2017'), "multifile wordcounts.csv")

#generateJSONFile(countWordsMany('.\state-of-the-union-corpus-1989-2017'), "JSONmultifileCounts.json")

print(searchCSV('.\multifile wordcounts.csv', 'if'))

print(searchJSON('.\JSONmultifileCounts.json', 'if'))
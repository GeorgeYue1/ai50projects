import nltk
import sys
import os
import string
import math
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    dict = {}
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        with open(path, encoding = "utf-8") as f:
            dict[file] = f.read()
    return dict 
    # raise NotImplementedError

def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    s = word_tokenize(document.lower())
    words = []
    for word in s:
        if word in nltk.corpus.stopwords.words("english") or word in string.punctuation:
            continue
        w = word
        for i in string.punctuation:
            w.replace(i, '')
        words.append(w)
    return words
    # raise NotImplementedError

def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfValues = {}
    for file in documents:
        unique = []
        for word in documents[file]:
            if word not in unique:
                unique.append(word)
                try:
                    idfValues[word] += 1
                except KeyError:
                    idfValues[word] = 1
    for word in idfValues:
        idfValues[word] = math.log(len(documents)/idfValues[word])
    return idfValues
    # raise NotImplementedError


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    values = {}
    for file in files:
        values[file] = 0
        for word in query:
            values[file] += files[file].count(word)*idfs[word]
    sortedValues = [k for k,v in sorted(values.items(), key = lambda x:x[1], reverse =True)]
    return sortedValues[:n]
    # raise NotImplementedError


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    values = {}
    for sentence in sentences:
        value = 0
        for word in query:
            if word in sentences[sentence]:
                value += idfs[word]
        density = 0
        for word in query:
            density += (sentences[sentence].count(word) / len(sentences[sentence]))
            values[sentence] = value, density
    sortedValues = [k for k,v in sorted(values.items(), key = lambda x:(x[1][0],x[1][1]), reverse =True)]
    return sortedValues[:n]
    # raise NotImplementedError


if __name__ == "__main__":
    main()

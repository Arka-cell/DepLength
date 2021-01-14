This is a packages that compute the dependency length of sentences for English language using CNN English model with spaCy library.

the class DepLength.sentences() returns sentences tokenized from text as spacy.tokens objects.
the class DepLength.punctuation() returns those sentences without punctuation.
the class DepLength.lengths() returns a dictionary of all sentences indices with their lengths.
DepLength.Sdl() returns a list of all sentences with their respective dependency lengths. The parameter punctuation, if set to false, takes sentences that contain punctuation and would add their distance to the sum of the dependency length sentence.
DepLength.getSentence() would returns a list of sentences the same way a built-in list object would do.
DepLength.getAllSentence() returns a list of all sentences.

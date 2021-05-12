import spacy
import pandas as pd

try:
    try:
        nlp = spacy.load('en_core_web_lg')
    except:
        print('spaCy English large model was not found')
        try:
            nlp = spacy.load('en_core_web_md')
        except:
            print('spaCy English medium model was not found')
            nlp = spacy.load('en_core_web_sm')
except:
    print('spaCy en_core_web_sm, en_core_web_md, en_core_web_lg not found visit https://spacy.io/models/en on how to install')

nlp.add_pipe(nlp.create_pipe('sentencizer'))

class DepLength:
    def __init__(self,data):
        self.stringobject = nlp(data)
        self.sentences = [sent.string.strip() for sent in self.stringobject.sents]
        self.sentences = [nlp(sentence) for sentence in self.sentences]
        self.senLength = {}

    def punctuation(self):
        self.sentencespunc = []
        for sentence in self.sentences:
            sentencepunc = ""
            string = ""
            for token in sentence:
                if token.is_punct == False:
                    if token != sentence[-1]:
                        sentencepunc = sentencepunc + str(sentence[token.i]) + " "
                    else:
                        sentencepunc = sentencepunc + str(sentence[token.i])
            if len(sentencepunc) > 0 and sentencepunc[-1] == " ":
                sentencepunc = sentencepunc[0:-1]
            self.sentencespunc.append(sentencepunc)
        return [nlp(sentence) for sentence in self.sentencespunc]

    def lengths(self):
        for sentence, n in zip(self.sentences, range(len(self.sentences))):
            self.senLength[n] = [len(sentence)]
        return self.senLength

    def sdl(self, punc=True):
        N_deps = {} # The whole list of dependecies is notated with a capital n
        n = 0
        # we need dependency either with or without removal of punctuation
        if punc == True:
            self.cleansentences = self.punctuation()
        else:
            self.cleansentences = self.sentences
        for sentence in self.cleansentences:
            n_dep = []
            if type(sentence) != type(True):
                for token in sentence:
                    token_n = [abs(child.i - token.i) for child in token.children]
                    n_dep.append(sum(token_n))
                N_deps[n] = sum(n_dep)
                n+=1

        to_del = [key for key in N_deps if N_deps[key] == 0]
        for key in to_del: del N_deps[key]
        return N_deps
    def getSentence(self, start_index, end_index=False):
        # If you want to get the whole sentence, you can call sentences method
        if end_index == False:
            return self.sentences[start_index]
        else:
            return self.sentences[start_index:end_index]
    def getAllSentence(self):
        return self.sentences

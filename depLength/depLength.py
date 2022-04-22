import spacy

nlp.add_pipe(nlp.create_pipe('sentencizer'))

class DepLength:
    def __init__(self,data):
        self.stringobject = nlp(data)
        self.sentences = [nlp(sent.string.strip()) for sent in self.stringobject.sents]
        self.senLength = {}

    def punctuation(self):
        self.sentencespunc = []
        for sentence in self.sentences:
            sentencepunc = ""
            string = ""
            for token in sentence:
                if not token.is_punct:
                    sentencepunc = sentencepunc + str(sentence[token.i]) + " " if token != sentence[-1] else sentencepunc = sentencepunc + str(sentence[token.i])
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
        if punc:
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
        if not end_index:
            return self.sentences[start_index]
        else:
            return self.sentences[start_index:end_index]
    def getAllSentence(self):
        return self.sentences

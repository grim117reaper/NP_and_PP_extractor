#imports
import os
import nltk

#helper functions
def extract_np(present):
    for subtree in present.subtrees():
        if subtree.label() == 'NP':
            yield ' '.join(word for word , tag in subtree.leaves())


def extract_pp(present):
    for subtree in present.subtrees():
        if subtree.label() == 'PP':
            yield ' '.join(word for word , tag in subtree.leaves())

#defining grammar for parser
grammar = ('''
    NP: {<JJ>?<JJS>?<JJR>?<NN>*<NNS>*<NNPS>*<NNP>*} # NP
    PP: {<NP>*<IN>+<NP>*} # PP
    ''')

cp = nltk.RegexpParser(grammar) #creating parser

#file initialization
file  = open("input.txt" , 'r+')
output_np = open("output_np.txt" , "w+")
output_pp = open("output_pp.txt" , "w+")

#file reading
sentences = file.readlines()

for sen in sentences:
    sens = "sentence = " + sen
    output_np.write(sens)
    output_np.write("\n")
    output_pp.write(sens)
    output_pp.write("\n")
    token = nltk.word_tokenize(sen) #tokenizing the words
    tagged = nltk.pos_tag(token) #pos tagging
    parsed_sent = cp.parse(tagged) #parsing the tagged words to parsed
    for g in extract_np(parsed_sent):
        if g == " ":
            output_np.write("no NP\n")
        else:
            NP = "NP : " + str(g)
            output_np.write(NP)
            output_np.write("\n")
    for g in extract_pp(parsed_sent):
        if not g:
            output_pp.write("no PP\n")
        else:
            PP = "PP : " + str(g)
            output_pp.write(PP)
            output_pp.write("\n")
    output_np.write("--------------------------------\n")
    output_pp.write("--------------------------------\n")

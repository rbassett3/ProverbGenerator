import random

with open("IdiomList.txt", 'r') as f:
    Lines = f.readlines()
Words = []
map(Words.extend, [("! " + line[:-1] + " .  \n").split() for line in Lines if line != "\n"])

class Idiom:
    """An idiom generator, which takes a text corpus W at initialization. W is an array of words with '!' as a starting token and '.' as an endin token. Generate an idiom with Idiom.Generate().

This method is a Markov chain model. The state is the current word. To proceed to the next state (word), we sample from all of the possible words which occur after the current word in the corpus.

Example:    Idiom = Idiom(Words)
            Idiom.Generate()
            >>> "A fish is always greener on the boat" """

    def __init__(self, Words):
        self.Words = Words

    def Generate(self):
        flag = True
        curWord = '!'
        while flag:
            PossibleWords = [self.Words[i+1] for i in range(len(self.Words)) if self.Words[i] == curWord]
            curWord = random.sample(PossibleWords, 1)[0]
            if curWord == ".":
                flag = False
            else:
                print(curWord),
    
Idiom = Idiom(Words)

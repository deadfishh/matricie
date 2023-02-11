class TruthTable:

    def __init__(self) -> None:
        pass

    def makeTable(self, statements):
        letters = self.findRows(statements)
        rows = 2**(len(letters)) + 1
        cols = len(letters) + len(statements)
        answer = [[0 for x in range(cols)] for y in range(rows)] 
        for i in range (len(answer)):
            for j in range (len(letters)):
                answer[0][j] = letters[j]
                div = 2**(len(letters) - j)
                x =  ((i-1) / (div)) % 1
                if x >= .5:
                    answer[i][j] = "T"
                else:
                    answer[i][j] = "F"
        for i in range (len(letters), cols):
            answer[0][i] = statements[i - len(letters)]
        self.writeAnswers(answer, len(letters))
        for i in range (len(answer)):
            print(answer[i])
            

    def findRows(self, statements):
        arr = []
        alpha = "abcedefghijklmnopqrstuwxyz"
        for s in statements:
            for letter in s:
                if letter in alpha and letter not in arr:
                    arr.append(letter)
        return arr

    def parse(self, sent):
        sent = sent.replace("^", " and ")
        sent = sent.replace("T", "True")
        sent = sent.replace("F", "False")
        sent = sent.replace("v", " or ")
        sent = sent.replace("~", "not ")
        return(eval(sent))

    def writeAnswers(self, table, letnum):
        for i in range (1, len(table)):
            for j in range (letnum, len(table[0])):
                sentence = table[0][j]
                for k in range (letnum):
                    sentence = sentence.replace(table[0][k], table[i][k])
                table[i][j] = str(self.parse(sentence))[0]


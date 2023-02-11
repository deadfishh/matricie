
class Matricie:

    def __init__(self) -> None:
        pass

    
    def multiply(self, m1, m2):
        if len(m1[0]) != len(m2):
            print("you dumb whore")
            return
        answer = [[0 for x in range(len(m2[0]))] for y in range(len(m1))] 
        for i in range (len(m1)):
            for j in range (len(m2[0])):
                sum = 0
                for k in range (len(m2)):
                    sum += m1[i][k] * m2[k][j]
                answer[i][j] = sum
        return answer


    # adds
    def add(self, m1, m2):
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            print("dumbass")
            return
        answer = [[0 for x in range(len(m1[0]))] for y in range(len(m1))] 
        for i in range (len(m1)):
            for j in range (len(m1[0])):
                answer[i][j] = m1[i][j] + m2[i][j]
        print(answer)


    # subtracts
    def subtract(self, m1, m2):
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            print("dumbass")
            return
        answer = [[0 for x in range(len(m1[0]))] for y in range(len(m1))] 
        for i in range (len(m1)):
            for j in range (len(m1[0])):
                answer[i][j] = m1[i][j] - m2[i][j]
        print(answer)


    def determ(self, mat):
        x = self.determ_helper(mat, 1)
        print(x)


    def determ_helper(self, mat, load):
        if len(mat) != 2:
            sum = 0
            for i in range (len(mat)):
                temp_mat = self.partition(mat, 0, i)
                adder = self.determ_helper(temp_mat, mat[0][i])
                if (adder == None):
                    continue
                if i % 2 == 1:
                    adder *= -1
                sum += adder
            return sum * load
        answer = (mat[1][1] * mat[0][0]) - (mat[0][1] * mat[1][0])
        return answer * load



    def partition(self, mat, ival, jval):
        answer = [[0 for x in range(len(mat[0]) - 1)] for y in range(len(mat) - 1)]
        iplace = 0
        jplace = 0
        for i in range (len(mat)):
            jplace = 0
            if i == ival:
                iplace = 1
                continue;
            for j in range (len(mat[0])):
                if j == jval:
                    jplace = 1
                    continue
                answer[i - iplace][j -jplace] = mat[i][j]
        return answer

    def adjugate(self, mat):
        answer = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
        for i in range (len(mat)):
            for j in range (len(mat[0])):
                mat2 = self.partition(mat, i, j)
                fact = [1, -1][(i + j) % 2 == 1]
                det = self.determ_helper(mat2, fact)
                answer[i][j] = det
        answer = self.transpose(answer)
        print(answer)
        return answer
    

    def transpose(self, mat):
        answer = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
        for i in range (len(mat)):
            for j in range (len(mat[0])):
                answer[i][j] = mat[j][i]
        return answer

    def scalar(self, mat, scalar):
        answer = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
        for i in range (len(mat)):
            for j in range (len(mat[0])):
                answer[i][j] = round(mat[i][j] * scalar, 2)
        return answer

    def inverse(self, mat):
        adj = self.adjugate(mat)
        det = self.determ_helper(mat, 1)
        scale = (1/det)
        answer = self.scalar(adj, scale)
        print(answer)
        
    
    def row_scalar(self, mat, row, scal):
        for i in range (len(mat)):
            if i == row:
                replace = self.list_scal(mat[i], scal)
                mat[i] = replace
                break
        print(mat)
        return mat

    def row_add(self, mat, row, to_add, fact):
        mat[row] = self.list_add(mat[row], mat[to_add], fact)
        return mat

    def list_scal(self, list, scal):
        for i in range (len(list)):
            list[i] = round(list[i] * scal, 2)
        return list

    def list_add(self, list1, list2, fact):
        for i in range (len(list1)):
            list1[i] = list1[i] + round((list2[i] * fact), 2)
        print(fact)
        return list1

    def rref(self, mat):
        if len(mat) >= len(mat[0]):
            print("F")
            return
        # make lower triangular
        for i in range (len(mat)):
            for j in range (len(mat)):
                print(str(i) + " " + str(j))
                if i < j:
                    fact = mat[j][i] * -1
                    mat = self.row_add(mat, j, i, fact)
                elif i == j:
                    fact = (1/mat[j][i])
                    mat = self.row_scalar(mat, j, fact)

        for i in range (len(mat)):
            for j in range (len(mat)):
                if i > j:
                    fact = mat[j][i] * -1
                    mat = self.row_add(mat, j, i, fact)
        
        for i in range (len(mat)):
            print(mat[i])

class Matricie:

    def __init__(self) -> None:
        pass

    
    # multiplies two matricies
    def multiply(self, m1, m2):
        # make sure that they are compatible
        if len(m1[0]) != len(m2):
            print("you dumb whore")
            return
        # initialize answer
        answer = [[0 for x in range(len(m2[0]))] for y in range(len(m1))] 
        # traverse through rows of m1
        for i in range (len(m1)):
            # traverse through columns of m2
            for j in range (len(m2[0])):
                sum = 0
                # traverse though rows of m2
                for k in range (len(m2)):
                    sum += m1[i][k] * m2[k][j]
                answer[i][j] = sum
        return answer


    # adds two matricies
    def add(self, m1, m2):
        # checks compatibility
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            print("dumbass")
            return
        # initialize answer
        answer = [[0 for x in range(len(m1[0]))] for y in range(len(m1))] 
        # add each element
        for i in range (len(m1)):
            for j in range (len(m1[0])):
                answer[i][j] = m1[i][j] + m2[i][j]
        return answer


    # subtracts to matricies
    def subtract(self, m1, m2):
        # checks compatibility
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            print("dumbass")
            return
        # initializes answer
        answer = [[0 for x in range(len(m1[0]))] for y in range(len(m1))] 
        # subtract m2 from m1
        for i in range (len(m1)):
            for j in range (len(m1[0])):
                answer[i][j] = m1[i][j] - m2[i][j]
        print(answer)
        return answer


    # takes the determinant
    def determ(self, mat):
        # checks if it's square
        if (len(mat)!= len(mat[0])):
            return
        # uses recursion
        det = self.determ_helper(mat, 1)
        print(det)
        return det


    # recursively takes the determinent
    def determ_helper(self, mat, load):
        # base case: 2x2 matrix
        if len(mat) == 2:
            answer = (mat[1][1] * mat[0][0]) - (mat[0][1] * mat[1][0])
            return answer * load
        # otherwise take the smaller determinants
        sum = 0
        # nxn matrix requires n sub-determinants
        for i in range (len(mat)):
            # smaller matrix is partitioned
            temp_mat = self.partition(mat, 0, i)
            # take the determinant using recursion <3
            adder = self.determ_helper(temp_mat, mat[0][i])
            # if it's in an odd column, multiply it by -1
            if i % 2 == 1:
                adder *= -1
            # add together all the sub determinants
            sum += adder
        # return the determinant
        return sum * load


    # partitions the matrix into a smaller one
    def partition(self, mat, ival, jval):
        # intializes answer as one smaller in rows and columns
        answer = [[0 for x in range(len(mat[0]) - 1)] for y in range(len(mat) - 1)]
        # determine if we've passed the blocked out rows
        iplace = 0
        jplace = 0
        # traverse though rows
        for i in range (len(mat)):
            # assume we haven't passed the blocked column
            jplace = 0
            # if this row is blocked, add one and continue
            if i == ival:
                iplace = 1
                continue;
            # traverse though columns
            for j in range (len(mat[0])):
                # if this column is blocked, add one and continue
                if j == jval:
                    jplace = 1
                    continue
                # copy the element to its place in the answer array
                answer[i - iplace][j -jplace] = mat[i][j]
        return answer


    # calculate the adjugate
    def adjugate(self, mat):
        # make sure that it's square
        if len(mat) != len(mat[0]):
            return
        # initialize answer array
        answer = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
        # traverse though the rows
        for i in range (len(mat)):
            # traverse through the columns
            for j in range (len(mat[0])):
                # find the partition
                mat2 = self.partition(mat, i, j)
                # factor is 1 or -1 depending on the place
                fact = [1, -1][(i + j) % 2 == 1]
                # take the determinant and put it in its place
                det = self.determ_helper(mat2, fact)
                answer[i][j] = det
        # transpose the current answer
        answer = self.transpose(answer)
        print(answer)
        return answer
    

    # tranpose a matrix
    def transpose(self, mat):
        # initialize answer array
        answer = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
        # traverse rows
        for i in range (len(mat)):
            # traverse cols
            for j in range (len(mat[0])):
                # mirror values over the main diagonal
                answer[i][j] = mat[j][i]
        return answer

    # scalar multiplication
    def scalar(self, mat, scalar):
        # initialize answer array
        answer = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
        # trvaerse rows
        for i in range (len(mat)):
            # traverse cols
            for j in range (len(mat[0])):
                # multiply each element and round it to hundreths
                answer[i][j] = round(mat[i][j] * scalar, 2)
        return answer

    # calculate the inverse
    def inverse(self, mat):
        # find the adjugate
        adj = self.adjugate(mat)
        # find the determinant
        det = self.determ_helper(mat, 1)
        # multiply adjugate by 1/(determinant)
        scale = (1/det)
        answer = self.scalar(adj, scale)
        print(answer)
        return answer
        
    
    # multiply a row by a scalar
    def row_scalar(self, mat, row, scal):
        # traverse rows
        for i in range (len(mat)):
            # if this is the row, replace it with a scalar multiple
            if i == row:
                replace = self.list_scal(mat[i], scal)
                mat[i] = replace
                break
        print(mat)
        return mat


    # add together two rows
    def row_add(self, mat, row, to_add, fact):
        mat[row] = self.list_add(mat[row], mat[to_add], fact)
        return mat


    # multiply a list by a scalar
    def list_scal(self, list, scal):
        for i in range (len(list)):
            list[i] = round(list[i] * scal, 2)
        return list


    # add two lists (one multiplied by a scalar)
    def list_add(self, list1, list2, fact):
        for i in range (len(list1)):
            list1[i] = list1[i] + round((list2[i] * fact), 2)
        print(fact)
        return list1


    # rref a matricie
    def rref(self, mat):
        # check compatibility
        if len(mat) >= len(mat[0]):
            print("F")
            return
        # make lower triangular
        for i in range (len(mat)):
            for j in range (len(mat)):
                print(str(i) + " " + str(j))
                # in lower triangle
                if i < j:
                    fact = mat[j][i] * -1
                    mat = self.row_add(mat, j, i, fact)
                # in main diagonal
                elif i == j:
                    fact = (1/mat[j][i])
                    mat = self.row_scalar(mat, j, fact)
        # make upper triangular
        for i in range (len(mat)):
            for j in range (len(mat)):
                # in upper triangle
                if i > j:
                    fact = mat[j][i] * -1
                    mat = self.row_add(mat, j, i, fact)
        
        for i in range (len(mat)):
            print(mat[i])
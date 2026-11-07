import math
scores= [3,5,2,7,8,2,7,3,3,5,2,7,8,2,7,3]
treeDepth= int (math.log2(len(scores)))
def minmax (currDepth,nodeIndex,isMaxTurn, count):
    if currDepth == treeDepth:
        count[0] +=1
        return scores[nodeIndex]
    if isMaxTurn:
        return max(
            minmax (currDepth + 1, nodeIndex * 2,False, count),
            minmax (currDepth + 1,nodeIndex * 2 + 1, False,count)
        )
    else:
        return min(
            minmax (currDepth +1, nodeIndex * 2, True, count),
            minmax (currDepth + 1,nodeIndex * 2 + 1, True, count)
        )
def alphabeta (currDepth,nodeIndex, isMaxTurn,alpha,beta, count):
        if currDepth == treeDepth:
            count[0] += 1
            return scores[nodeIndex]
        if isMaxTurn:
            value= float ('-inf')
            for i in range(2):
                value= max(
                    value,
                    alphabeta(
                        currDepth + 1, nodeIndex * 2 + i, False, alpha,beta, count
                    )
                )
                alpha= max (alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
                value= float('inf')
                for i in range(2):
                    value=min(
                        value,
                        alphabeta(
                            currDepth + 1, nodeIndex * 2 + i, True, alpha, beta, count
                        )
                    )
                    beta= min(beta,value )
                    if alpha >= beta:
                        break
                return value 
minimax_count= [0]
minimax_value= minmax (0,0,True, minimax_count)
alphabeta_count= [0]
alphabeta_value= alphabeta(
    0,0,True, float('-inf'),
    float ('inf'), alphabeta_count
)
print("Minimax optimal value:" , minimax_value)
print("Minimax leaves evaluated:" , minimax_count[0])
print("Alpha-Beta optimal value:" , alphabeta_value)
print("Alpha-Beta leaves evaluated:",alphabeta_count[0])                
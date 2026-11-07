import math
original_scores= [3,5,2,7,8,2,7,3,3,5,2,7,8,2,7,3]
reordered_scores= [5,3,7,2,2,8,3,7,5,3,7,2,2,8,3,7]
def minmax (depth, index, isMax, scores, targetDepth, count):
    if depth == targetDepth:
        count[0] += 1
        return scores [index]
    if isMax:
        left= minmax (depth + 1,index *2,False,scores, targetDepth, count)
        right= minmax (depth + 1,index *2 +1,False,scores, targetDepth, count)
        return max(left, right)
    else:
        left= minmax (depth + 1,index *2,True,scores, targetDepth, count)
        right= minmax (depth + 1,index *2 +1,True,scores, targetDepth, count)
        return max(left, right)
def alphabeta (depth,index,isMax,scores, targetDepth, alpha,beta,count):
    if depth == targetDepth:
        count [0] +=1
        return scores [index]
    if isMax:
        value= float('-inf')
        for i in range (2):
            value= max (
                value,
                alphabeta(
                    depth +1,index *2 + i,False,scores, targetDepth,alpha, beta, count
                )
            )
            alpha= max (alpha,value)
            if alpha>= beta:
                break
        return value
    else:
        value= float ('inf')
        for i in range (2):
            value= min(
                value,
                alphabeta(
                    depth +1,index *2 +i, True,scores, targetDepth,alpha, beta, count
                )
            )
            beta= min (beta,value)
            if alpha>=beta:
                break
        return value
def runTest (scores,title):
    depth=int (math.log2(len(scores)))
    minimax_count= [0]
    minimax_value= minmax(
        0,0,True,scores,depth, minimax_count
    )
    alphabeta_count= [0]
    alphabeta_value= alphabeta (
        0,0,True, scores,depth, float('-inf'),float ('inf'), alphabeta_count
    )
    print("\n---", title, "---")
    print("Minimax value:",minimax_value )
    print("Minimax leaves evaluated:", minimax_count[0] )
    print("Alpha-Beta value:", alphabeta_value )
    print("Alpha-Beta leaves evaluated:", alphabeta_count[0])
runTest(original_scores, "Original Branch Order")
runTest(reordered_scores, "Reordered Branches")

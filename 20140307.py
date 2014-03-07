# Problem of the Day - 2014/03/07
# http://www.problemotd.com/problem/matrix-rotation/
#
# By Andrew Williams
 
from datetime import datetime
 
start = [[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]]
        
target = [[21, 16, 11, 6, 1], 
    [22, 17, 12, 7, 2],
    [23, 18, 13, 8, 3],
    [24, 19, 14, 9, 4],
    [25, 20, 15, 10, 5]]
        
target_weekend = [[5, 10, 15, 20, 25],
        [4, 9, 14, 19, 24],
        [3, 8, 13, 18, 23],
        [2, 7, 12, 17, 22],
        [1, 6, 11, 16, 21]]
        
        
def rotate_matrix(matrix, dow=datetime.now().weekday()):
    if dow in [6, 7]:
        return zip(*matrix)[::-1]
    else:
        return zip(*matrix[::-1])
    
def compare_matrix(matrix, target):
    for i, a in enumerate(matrix):
        for ii, b in enumerate(a):
            if b != target[i][ii]:
                return False
    return True
    
if __name__ == '__main__':
    print "Forward Check: {}".format(compare_matrix(rotate_matrix(start, 1), target))
    print "Reverse Check: {}".format(compare_matrix(rotate_matrix(start, 6), target_weekend))

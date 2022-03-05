class Solution:
    def maxArea(self,M, n, m):
        # code here





# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
#Problem: https://practice.geeksforgeeks.org/problems/max-rectangle/1
#https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
#https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/
#https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/
#https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/




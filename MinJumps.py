class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if(arr[0]<1 and n!=1):
	        return -1
        else:
	        jump=0
	        maxr=arr[0]
	        pos=0
	        while n>1:
                tpos=pos
                if arr[tpos]>=n:
                    jump=jump+1
                    break
                c=0
                for i in range(1,arr[tpos]+1):
                    if tpos+i+arr[tpos+i]>maxr: #X
                        maxr=tpos+i+arr[tpos+i] #X if arr[pos]>(maxr+t)_instance
                        pos=tpos+i
                        c=1
                if c==0:
                    pos=pos+maxr
                    maxr=arr[pos] #X if arr[pos]>(maxr+t)_instance
                jump=jump+1
                n=n-pos+tpos #X
                if arr[pos]==0 and pos!=n-1:
                    return -1
                    break
        return jump


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
#https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1/?page=1&difficulty[]=1&sortBy=submissions#

"""
n=int(input())
arr=[int(x) for x in input().split()]
if(arr[0]<1 and n!=1):
    jump=-1
else:
    jump=0
    maxr=arr[0]
    pos=0
    print('jump=',jump,'maxr=',maxr,'pos=',pos)
    while n>1:
        print('------for n=',n)
        tpos=pos
        print('tpos=',tpos)
        if arr[tpos]>=n:
            jump=jump+1
            break
        c=0
        for i in range(1,arr[tpos]+1):
            print('2nd loop i=',i)
            if tpos+i+arr[tpos+i]>maxr: #X
                maxr=tpos+i+arr[tpos+i] #X if arr[pos]>(maxr+t)_instance
                pos=tpos+i
                print('If condition true: maxr=',maxr,' pos=',pos,'tpos=',tpos)
                c=1
        if c==0:
            pos=pos+maxr
            maxr=arr[pos] #X if arr[pos]>(maxr+t)_instance
            print('If condition false: maxr=',maxr,' pos=',pos,'tpos=',tpos)
        jump=jump+1
        print('jump=',jump)
        n=n-pos+tpos #X
        if arr[pos]==0 and pos!=n-1:
            jump=-1
        print('n=',n)
print('Total Jumps=',jump)
"""

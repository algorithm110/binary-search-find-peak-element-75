'''
Created on Mar 20, 2019

@author: J
'''

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    @staticmethod
    def findPeak(A):
        # check if empty
        if len(A) == 0:
            return -1
        
        #find the peak
        start = 0
        end = len(A)-1
        
        while start + 1 < end:
            
            mid = start + int((end - start)/2)
            
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] > A[mid-1]:
                start = mid
            elif A[mid] < A[mid-1]:
                end = mid
                
        if A[start] > A[end]:
            return start
        else:
            return end    
            


A = [1, 2, 1, 3, 4, 5, 7, 6]     
print("output should be 1 or 6, the answer is: "+ str(Solution.findPeak(A)))   

B = [1,2,3,4,1]
print("output should be 3, the answer is: "+ str(Solution.findPeak(B)))  
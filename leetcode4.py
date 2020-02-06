# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:14:37 2020

@author: arva kagdi 
"""

def findMedianSortedArrays(nums1,nums2):
    sortedlist = []
    sortedlist = nums1 + nums2
    sortedlist.sort()
    n = len(sortedlist)
    median = 0

    if  n%2 == 0:
        n1 = int(n/2)-1
        n2 = n1+1
        median = (sortedlist[n1] + sortedlist[n2])/2
        return(median)
    else:
        median = (sortedlist[int(n/2)])
        return(median)



nums1 = [1,3]
nums2 = [2]

print(findMedianSortedArrays(nums1,nums2))


    
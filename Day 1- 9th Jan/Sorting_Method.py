# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 01:15:28 2023

@author: ayush
"""

# Bubble Sort: 
#   Swapping the adjacent elements if they are in the wrong order.

def bubbleSort(arr,n): 
    
    for i in range(n):   # Traverse all elements
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]  # Swaping
    return arr


if __name__ == "__main__":
  
  arr = [5, 1, 4, 2, 8]
  n=len(arr)
  
  print(bubbleSort(arr,n))


#Time Complexity: O(N^2)
#Space Complexity: O(1)
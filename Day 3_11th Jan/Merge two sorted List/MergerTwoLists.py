# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 13:43:24 2023

@author: ayush
"""
# Merge Two Sorted Lists

#Approach Singly Linked List

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

    def mergeTwoLists(l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        curr=temp=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        
        if l1:
            curr.next=l1
        if l2:
            curr.next=l2
        
        return temp.next
    

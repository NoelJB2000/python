#!/usr/bin/env python
# coding: utf-8

# In[24]:


#longest palindromic subsequence using recursion
def lps(S,i,j):
    #if index of left chararcter exceeds the index of right character return 0
    if(i>j):
        return 0
    #if there is only one character in the string then return 1
    if(i==j): 
        return 1
    #if there is only 2 characters in the string then return 2
    if(S[i]==S[j] and i+1==j):
        return 2
    #if the first and last character of the string matches then return the value by adding 2
    if(S[i] == S[j]):
        return 2+lps(S,i+1,j-1)
    #else find the length by skipping index from first and skipping index from last and return the maximmum of both the values
    return max(lps(S,i+1,j),lps(S,i,j-1))


S = input("Enter a String :")
print("Length of the longest palindromic subsequence is :", lps(S,0,len(S)-1))


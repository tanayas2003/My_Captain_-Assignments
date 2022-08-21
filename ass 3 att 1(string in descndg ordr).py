# TANAYA SAWAJI
"""
Created on Sun Aug 21 16:34:12 2022

assignment 3 : create string and arrange in descending order
"""

str = input("Enter a string : ")
print("String is :",str)
count = { }
for x in str:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1
        
print(count) 

print("Original dictionary:",count)
sorted_count = sorted(count.items())
print("Dictionary in ascending order :",sorted_count)
sorted_count_reverse = sorted(count.items(),reverse=True)
print("most frequent :",sorted_count_reverse)

print("end of the progrm")    
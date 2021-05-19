# write a function to compute 5/0 and use try/except to catch the exceptions.
def divide():
    return 5/0

try:
    divide()
except: ZeroDivisionError 
print("Zero exception error")
    
# Implement a python program to generate sentences where subject is in ["Americans",#"Indians"] 
# and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"]. 


'''
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]verbs=["play","watch"]objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.
'''

subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

#print(tuple(zip(subjects,verbs,objects)))
# (('Americans ', 'play', 'Baseball'), ('Indians', 'watch', 'Cricket'))

sentence=[ (sub + " " + ver + " " + obj) for sub in subjects for ver in verbs for obj in objects]
for sen in sentence:print(sen)


